"""
Data Cleaning & Preprocessing Pipeline Module
Project: Student Skills and Placement Tracker
"""

import os
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def clean_raw_data(df):
    """
    Cleans raw dataset by handling duplicates, invalid value ranges, and standardizing categories.
    
    Parameters:
        df (pd.DataFrame): Raw student dataframe.
        
    Returns:
        pd.DataFrame: Cleaned student dataframe.
    """
    df_clean = df.copy()
    
    # 1. Remove duplicate records
    initial_rows = len(df_clean)
    df_clean = df_clean.drop_duplicates().reset_index(drop=True)
    dropped_dups = initial_rows - len(df_clean)
    if dropped_dups > 0:
        print(f"[Cleaning] Removed {dropped_dups} duplicate rows.")
        
    # 2. Fix out-of-bounds invalid values
    # CGPA valid range: 0.0 to 10.0
    cgpa_outliers = (df_clean['cgpa'] < 0.0) | (df_clean['cgpa'] > 10.0)
    if cgpa_outliers.sum() > 0:
        print(f"[Cleaning] Correcting {cgpa_outliers.sum()} invalid CGPA values (>10 or <0) to NaN for imputation.")
        df_clean.loc[cgpa_outliers, 'cgpa'] = np.nan
        
    # Attendance valid range: 0.0 to 100.0
    att_outliers = (df_clean['attendance_percentage'] < 0.0) | (df_clean['attendance_percentage'] > 100.0)
    if att_outliers.sum() > 0:
        print(f"[Cleaning] Correcting {att_outliers.sum()} invalid attendance percentage values to NaN.")
        df_clean.loc[att_outliers, 'attendance_percentage'] = np.nan
        
    # Score columns valid range: 0.0 to 100.0
    score_cols = [
        'programming_score', 'dsa_score', 'sql_score', 'web_dev_score',
        'ml_score', 'cloud_score', 'aptitude_score', 'coding_test_score',
        'communication_score', 'leadership_score', 'teamwork_score', 'interview_score',
        'project_quality_score', 'resume_score'
    ]
    for col in score_cols:
        if col in df_clean.columns:
            invalid_scores = (df_clean[col] < 0.0) | (df_clean[col] > 100.0)
            if invalid_scores.sum() > 0:
                print(f"[Cleaning] Correcting {invalid_scores.sum()} invalid score values in column '{col}' to NaN.")
                df_clean.loc[invalid_scores, col] = np.nan
                
    # 3. Clean categorical text columns
    cat_cols = ['gender', 'branch', 'degree']
    for col in cat_cols:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].astype(str).str.strip().str.title()
            
    return df_clean

def get_preprocessor_pipeline(numerical_features, categorical_features):
    """
    Constructs a ColumnTransformer for preprocessing numeric and categorical columns.
    
    Parameters:
        numerical_features (list): List of numeric column names.
        categorical_features (list): List of categorical column names.
        
    Returns:
        ColumnTransformer: Scikit-learn ColumnTransformer instance.
    """
    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    cat_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', num_pipeline, numerical_features),
            ('cat', cat_pipeline, categorical_features)
        ],
        remainder='drop'
    )
    
    return preprocessor

def split_and_save_data(df, target_col='placement_status', test_size=0.2, random_state=42, output_dir="C:/Users/shyam/student-skills-placement-tracker/data/processed"):
    """
    Splits dataframe into stratified train and test sets and saves them to disk.
    
    Returns:
        tuple: (X_train, X_test, y_train, y_test)
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Drop identifier columns not used in modeling
    drop_cols = [target_col, 'student_id'] if 'student_id' in df.columns else [target_col]
    X = df.drop(columns=drop_cols)
    y = df[target_col]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    X_train.to_csv(os.path.join(output_dir, "X_train.csv"), index=False)
    X_test.to_csv(os.path.join(output_dir, "X_test.csv"), index=False)
    y_train.to_csv(os.path.join(output_dir, "y_train.csv"), index=False)
    y_test.to_csv(os.path.join(output_dir, "y_test.csv"), index=False)
    
    df.to_csv(os.path.join(output_dir, "student_placement_processed.csv"), index=False)
    
    print(f"[Preprocessing] Data split successfully:")
    print(f"  - Train set shape: {X_train.shape}, Target distribution: {dict(y_train.value_counts())}")
    print(f"  - Test set shape: {X_test.shape}, Target distribution: {dict(y_test.value_counts())}")
    
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    raw_path = "C:/Users/shyam/student-skills-placement-tracker/data/raw/placement_data_raw.csv"
    if os.path.exists(raw_path):
        df_raw = pd.read_csv(raw_path)
        df_clean = clean_raw_data(df_raw)
        X_tr, X_te, y_tr, y_te = split_and_save_data(df_clean)
