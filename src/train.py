"""
Model Training, Cross-Validation, Hyperparameter Tuning & Pipeline Serialization
Project: Student Skills and Placement Tracker
"""

import os
import sys

# Ensure project root is in Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import joblib
import pandas as pd
import numpy as np

from sklearn.model_selection import StratifiedKFold, cross_validate, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC

from src.preprocessing import clean_raw_data, get_preprocessor_pipeline, split_and_save_data
from src.feature_engineering import create_engineered_features
from src.evaluate import evaluate_all_models, plot_model_evaluations, plot_feature_importance, generate_eda_figures

def train_and_evaluate_all_models(
    raw_data_path="C:/Users/shyam/student-skills-placement-tracker/data/raw/placement_data_raw.csv",
    output_dir="C:/Users/shyam/student-skills-placement-tracker/models",
    reports_dir="C:/Users/shyam/student-skills-placement-tracker/reports"
):
    """
    Complete end-to-end training execution:
    1. Loads raw data, cleans it, applies feature engineering.
    2. Splits data into train and test sets.
    3. Builds preprocessing pipeline.
    4. Evaluates multiple algorithms with 5-Fold Stratified Cross Validation.
    5. Performs Hyperparameter Tuning on top models.
    6. Selects the best model based on F1-Score & ROC-AUC.
    7. Retrains full pipeline and serializes models/ artifacts.
    """
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(reports_dir, exist_ok=True)
    os.makedirs(os.path.join(reports_dir, "figures"), exist_ok=True)
    
    # 1. Load and process data
    print("==================================================")
    print("STEP 1: Data Cleaning & Feature Engineering")
    print("==================================================")
    df_raw = pd.read_csv(raw_data_path)
    df_clean = clean_raw_data(df_raw)
    df_feat = create_engineered_features(df_clean)
    
    # Generate EDA figures
    generate_eda_figures(df_feat, os.path.join(reports_dir, "figures"))
    
    # Train / Test split
    X_train, X_test, y_train, y_test = split_and_save_data(df_feat, target_col='placement_status', random_state=42)
    
    # Identify column types
    categorical_cols = ['gender', 'branch', 'degree']
    numerical_cols = [c for c in X_train.columns if c not in categorical_cols and c != 'student_id']
    
    print(f"\nFeatures overview: {len(numerical_cols)} numerical, {len(categorical_cols)} categorical.")
    
    # Create base preprocessor
    preprocessor = get_preprocessor_pipeline(numerical_cols, categorical_cols)
    
    # 2. Define baseline & candidate classification models
    candidate_models = {
        'Baseline (Dummy)': DummyClassifier(strategy='most_frequent'),
        'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42, class_weight='balanced'),
        'K-Nearest Neighbors': KNeighborsClassifier(n_neighbors=5),
        'Decision Tree': DecisionTreeClassifier(max_depth=6, random_state=42, class_weight='balanced'),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced'),
        'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, random_state=42),
        'XGBoost': XGBClassifier(n_estimators=100, random_state=42, eval_metric='logloss'),
        'Support Vector Machine': SVC(probability=True, random_state=42, class_weight='balanced')
    }
    
    print("\n==================================================")
    print("STEP 2: 5-Fold Stratified Cross-Validation")
    print("==================================================")
    
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_results_summary = []
    trained_base_pipelines = {}
    
    for name, clf in candidate_models.items():
        pipe = Pipeline([
            ('preprocessor', preprocessor),
            ('classifier', clf)
        ])
        
        cv_res = cross_validate(
            pipe, X_train, y_train,
            cv=skf,
            scoring=['accuracy', 'precision', 'recall', 'f1', 'roc_auc'],
            n_jobs=1
        )
        
        pipe.fit(X_train, y_train)
        trained_base_pipelines[name] = pipe
        
        mean_acc = np.mean(cv_res['test_accuracy'])
        mean_prec = np.mean(cv_res['test_precision'])
        mean_rec = np.mean(cv_res['test_recall'])
        mean_f1 = np.mean(cv_res['test_f1'])
        mean_auc = np.mean(cv_res['test_roc_auc'])
        std_f1 = np.std(cv_res['test_f1'])
        
        print(f"[{name:22s}] CV F1: {mean_f1:.4f} (+/- {std_f1:.4f}) | CV ROC-AUC: {mean_auc:.4f} | CV Rec: {mean_rec:.4f}")
        
        cv_results_summary.append({
            'Model': name,
            'CV F1 Score': round(mean_f1, 4),
            'CV F1 Std': round(std_f1, 4),
            'CV ROC-AUC': round(mean_auc, 4),
            'CV Recall': round(mean_rec, 4),
            'CV Precision': round(mean_prec, 4),
            'CV Accuracy': round(mean_acc, 4)
        })
        
    cv_df = pd.DataFrame(cv_results_summary)
    
    print("\n==================================================")
    print("STEP 3: Hyperparameter Tuning for Top Candidates")
    print("==================================================")
    
    param_grids = {
        'Random Forest': {
            'classifier__n_estimators': [100, 150],
            'classifier__max_depth': [8, 12],
            'classifier__class_weight': ['balanced']
        },
        'Gradient Boosting': {
            'classifier__n_estimators': [100],
            'classifier__learning_rate': [0.05, 0.1],
            'classifier__max_depth': [3, 5]
        },
        'XGBoost': {
            'classifier__n_estimators': [100],
            'classifier__learning_rate': [0.05, 0.1],
            'classifier__max_depth': [3, 5]
        }
    }
    
    tuned_pipelines = {}
    
    for name in ['Random Forest', 'Gradient Boosting', 'XGBoost']:
        print(f"[Tuning] Optimizing hyperparameters for {name}...")
        base_pipe = Pipeline([
            ('preprocessor', preprocessor),
            ('classifier', candidate_models[name])
        ])
        
        grid_search = GridSearchCV(
            base_pipe,
            param_grid=param_grids[name],
            cv=skf,
            scoring='f1',
            n_jobs=1,
            verbose=0
        )
        grid_search.fit(X_train, y_train)
        
        print(f"  Best params: {grid_search.best_params_}")
        print(f"  Best CV F1: {grid_search.best_score_:.4f}")
        tuned_pipelines[f"{name} (Tuned)"] = grid_search.best_estimator_
        
    all_evaluated_pipelines = {**trained_base_pipelines, **tuned_pipelines}
    
    print("\n==================================================")
    print("STEP 4: Test Set Evaluation & Model Comparison")
    print("==================================================")
    
    test_metrics_df = evaluate_all_models(all_evaluated_pipelines, X_test, y_test)
    
    results_report = test_metrics_df.sort_values(by='F1 Score', ascending=False).reset_index(drop=True)
    results_report_path = os.path.join(reports_dir, "model_results.csv")
    results_report.to_csv(results_report_path, index=False)
    
    print("\nModel Comparison Table (Sorted by Test F1 Score):")
    print(results_report.to_string(index=False))
    print(f"\n[Reports] Saved detailed results to {results_report_path}")
    
    plot_model_evaluations(all_evaluated_pipelines, X_test, y_test, os.path.join(reports_dir, "figures"))
    
    best_model_row = results_report.iloc[0]
    best_model_name = best_model_row['Model']
    best_pipeline = all_evaluated_pipelines[best_model_name]
    
    print("\n==================================================")
    print(f"STEP 5: Final Model Selection: [{best_model_name}]")
    print("==================================================")
    print(f"Rationale: Selected [{best_model_name}] achieving highest test F1 Score = {best_model_row['F1 Score']:.4f}, "
          f"ROC-AUC = {best_model_row['ROC-AUC']:.4f}, and Recall = {best_model_row['Recall']:.4f}.")
    
    X_full = pd.concat([X_train, X_test], ignore_index=True)
    y_full = pd.concat([y_train, y_test], ignore_index=True)
    
    best_pipeline.fit(X_full, y_full)
    
    fitted_classifier = best_pipeline.named_steps['classifier']
    fitted_preprocessor = best_pipeline.named_steps['preprocessor']
    
    try:
        cat_encoder = fitted_preprocessor.named_transformers_['cat'].named_steps['encoder']
        encoded_cat_names = list(cat_encoder.get_feature_names_out(categorical_cols))
    except Exception:
        encoded_cat_names = categorical_cols
        
    all_feature_names = numerical_cols + encoded_cat_names
    plot_feature_importance(fitted_classifier, all_feature_names, top_n=15, figures_dir=os.path.join(reports_dir, "figures"))
    
    print("\n==================================================")
    print("STEP 6: Saving Model & Preprocessor Artifacts")
    print("==================================================")
    
    final_model_path = os.path.join(output_dir, "final_model.pkl")
    preprocessor_path = os.path.join(output_dir, "preprocessor.pkl")
    feature_info_path = os.path.join(output_dir, "feature_info.pkl")
    
    joblib.dump(best_pipeline, final_model_path)
    joblib.dump(fitted_preprocessor, preprocessor_path)
    
    feature_info = {
        'numerical_cols': numerical_cols,
        'categorical_cols': categorical_cols,
        'all_feature_names': all_feature_names,
        'best_model_name': best_model_name,
        'test_metrics': best_model_row.to_dict()
    }
    joblib.dump(feature_info, feature_info_path)
    
    print(f"  - Saved final pipeline: {final_model_path}")
    print(f"  - Saved preprocessor: {preprocessor_path}")
    print(f"  - Saved feature info: {feature_info_path}")
    
    return best_model_name, best_model_row, final_model_path

if __name__ == "__main__":
    train_and_evaluate_all_models()
