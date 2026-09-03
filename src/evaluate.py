"""
Model Evaluation and EDA Visualization Module
Project: Student Skills and Placement Tracker
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, classification_report,
    roc_curve, precision_recall_curve
)

# Set global plotting style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10

def generate_eda_figures(df, figures_dir="C:/Users/shyam/student-skills-placement-tracker/reports/figures"):
    """
    Generates and saves exploratory data analysis visualizations.
    """
    os.makedirs(figures_dir, exist_ok=True)
    
    # 1. Target Distribution
    fig, ax = plt.subplots(figsize=(7, 5))
    target_counts = df['placement_status'].value_counts()
    sns.barplot(x=['Needs Improvement (0)', 'Placement Ready (1)'], y=target_counts.values, hue=['Needs Improvement (0)', 'Placement Ready (1)'], palette=['#e74c3c', '#2ecc71'], ax=ax, legend=False)
    ax.set_title('Target Distribution: Student Placement Readiness', fontsize=12, fontweight='bold')
    ax.set_ylabel('Student Count', fontsize=10)
    for i, count in enumerate(target_counts.values):
        ax.text(i, count + 15, f"{count} ({count/len(df)*100:.1f}%)", ha='center', fontweight='bold')
    plt.tight_layout()
    fig.savefig(os.path.join(figures_dir, 'target_distribution.png'), dpi=300)
    plt.close()
    
    # 2. CGPA vs Placement Status Boxplot & KDE
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    sns.boxplot(data=df, x='placement_status', y='cgpa', hue='placement_status', palette=['#e74c3c', '#2ecc71'], ax=axes[0], legend=False)
    axes[0].set_xticks([0, 1])
    axes[0].set_xticklabels(['Needs Improvement', 'Placement Ready'])
    axes[0].set_title('CGPA Distribution by Placement Readiness', fontweight='bold')
    axes[0].set_xlabel('Placement Readiness')
    axes[0].set_ylabel('CGPA')
    
    sns.kdeplot(data=df, x='cgpa', hue='placement_status', palette=['#e74c3c', '#2ecc71'], fill=True, common_norm=False, ax=axes[1])
    axes[1].set_title('CGPA Density Estimation', fontweight='bold')
    axes[1].set_xlabel('CGPA')
    plt.tight_layout()
    fig.savefig(os.path.join(figures_dir, 'cgpa_vs_placement.png'), dpi=300)
    plt.close()
    
    # 3. Core Skill Distributions
    skills = ['dsa_score', 'programming_score', 'communication_score', 'coding_test_score']
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    for idx, skill in enumerate(skills):
        sns.boxplot(data=df, x='placement_status', y=skill, hue='placement_status', palette=['#e74c3c', '#2ecc71'], ax=axes[idx], legend=False)
        axes[idx].set_xticks([0, 1])
        axes[idx].set_xticklabels(['Needs Improvement', 'Placement Ready'])
        axes[idx].set_title(f"{skill.replace('_', ' ').title()} by Placement Readiness", fontweight='bold')
    plt.tight_layout()
    fig.savefig(os.path.join(figures_dir, 'skill_distributions.png'), dpi=300)
    plt.close()
    
    # 4. Correlation Heatmap (Top 12 numeric columns)
    num_cols = df.select_dtypes(include=[np.number]).columns
    corr = df[num_cols].corr()
    top_corr_cols = corr['placement_status'].abs().sort_values(ascending=False).head(13).index
    
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(df[top_corr_cols].corr(), annot=True, fmt=".2f", cmap='Blues', ax=ax, cbar=True)
    ax.set_title('Feature Correlation Heatmap with Placement Status', fontsize=12, fontweight='bold')
    plt.tight_layout()
    fig.savefig(os.path.join(figures_dir, 'feature_correlations.png'), dpi=300)
    plt.close()
    
    print(f"[EDA] Generated 4 key EDA figures in {figures_dir}.")

def evaluate_all_models(models_dict, X_test, y_test):
    """
    Evaluates multiple trained models on the test set and calculates metrics.
    
    Returns:
        pd.DataFrame: Performance metrics summary.
    """
    results = []
    
    for name, model in models_dict.items():
        y_pred = model.predict(X_test)
        
        if hasattr(model, "predict_proba"):
            y_prob = model.predict_proba(X_test)[:, 1]
            roc_auc = roc_auc_score(y_test, y_prob)
        else:
            roc_auc = np.nan
            
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, zero_division=0)
        rec = recall_score(y_test, y_pred, zero_division=0)
        f1 = f1_score(y_test, y_pred, zero_division=0)
        
        results.append({
            'Model': name,
            'Accuracy': round(acc, 4),
            'Precision': round(prec, 4),
            'Recall': round(rec, 4),
            'F1 Score': round(f1, 4),
            'ROC-AUC': round(roc_auc, 4) if not np.isnan(roc_auc) else None
        })
        
    results_df = pd.DataFrame(results)
    return results_df

def plot_model_evaluations(models_dict, X_test, y_test, figures_dir="C:/Users/shyam/student-skills-placement-tracker/reports/figures"):
    """
    Plots confusion matrices and ROC curves for all models.
    """
    os.makedirs(figures_dir, exist_ok=True)
    
    # 1. Confusion Matrices Grid
    n_models = len(models_dict)
    cols = 3
    rows = (n_models + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(15, 4 * rows))
    axes = axes.flatten() if n_models > 1 else [axes]
    
    for idx, (name, model) in enumerate(models_dict.items()):
        y_pred = model.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[idx], cbar=False)
        axes[idx].set_title(f"{name}", fontweight='bold')
        axes[idx].set_xlabel('Predicted')
        axes[idx].set_ylabel('Actual')
        axes[idx].set_xticks([0.5, 1.5])
        axes[idx].set_yticks([0.5, 1.5])
        axes[idx].set_xticklabels(['Needs Impr.', 'Ready'])
        axes[idx].set_yticklabels(['Needs Impr.', 'Ready'])
        
    for j in range(idx + 1, len(axes)):
        fig.delaxes(axes[j])
        
    plt.tight_layout()
    fig.savefig(os.path.join(figures_dir, 'confusion_matrices.png'), dpi=300)
    plt.close()
    
    # 2. ROC Curves Overlay
    fig, ax = plt.subplots(figsize=(8, 6))
    for name, model in models_dict.items():
        if hasattr(model, "predict_proba"):
            y_prob = model.predict_proba(X_test)[:, 1]
            fpr, tpr, _ = roc_curve(y_test, y_prob)
            auc_val = roc_auc_score(y_test, y_prob)
            ax.plot(fpr, tpr, label=f"{name} (AUC = {auc_val:.3f})")
            
    ax.plot([0, 1], [0, 1], 'k--', label='Random Chance')
    ax.set_title('ROC Curves Comparison Across Models', fontweight='bold', fontsize=12)
    ax.set_xlabel('False Positive Rate (1 - Specificity)')
    ax.set_ylabel('True Positive Rate (Recall)')
    ax.legend(loc='lower right', fontsize=9)
    plt.tight_layout()
    fig.savefig(os.path.join(figures_dir, 'roc_curves.png'), dpi=300)
    plt.close()
    
    print(f"[Evaluation] Saved confusion matrices & ROC curves in {figures_dir}.")

def plot_feature_importance(model, feature_names, top_n=15, figures_dir="C:/Users/shyam/student-skills-placement-tracker/reports/figures"):
    """
    Plots feature importance for tree models or coefficient magnitudes for linear models.
    """
    os.makedirs(figures_dir, exist_ok=True)
    
    if hasattr(model, 'feature_importances_'):
        importances = model.feature_importances_
        title = "Top Feature Importances (Best Classifier)"
    elif hasattr(model, 'coef_'):
        importances = np.abs(model.coef_[0])
        title = "Top Absolute Model Coefficients (Logistic Regression)"
    else:
        print("[Evaluation] Model does not support native feature_importances_ or coef_.")
        return
        
    imp_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance': importances
    }).sort_values(by='Importance', ascending=False).head(top_n)
    
    fig, ax = plt.subplots(figsize=(9, 6))
    sns.barplot(data=imp_df, x='Importance', y='Feature', hue='Feature', palette='crest', ax=ax, legend=False)
    ax.set_title(title, fontweight='bold', fontsize=12)
    ax.set_xlabel('Relative Importance Score')
    plt.tight_layout()
    fig.savefig(os.path.join(figures_dir, 'feature_importance.png'), dpi=300)
    plt.close()
    
    print(f"[Evaluation] Saved feature importance plot to {os.path.join(figures_dir, 'feature_importance.png')}.")
    return imp_df
