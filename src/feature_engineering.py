"""
Feature Engineering Module
Project: Student Skills and Placement Tracker
"""

import os
import pandas as pd
import numpy as np

def create_engineered_features(df):
    """
    Creates domain-specific aggregate features and readiness indices.
    
    Parameters:
        df (pd.DataFrame): Dataframe containing raw or cleaned student features.
        
    Returns:
        pd.DataFrame: Dataframe augmented with engineered features.
    """
    df_feat = df.copy()
    
    # 1. Technical Skill Average
    tech_cols = ['programming_score', 'dsa_score', 'sql_score', 'web_dev_score', 'ml_score', 'cloud_score']
    df_feat['technical_skill_avg'] = np.round(df_feat[tech_cols].mean(axis=1), 2)
    
    # 2. Soft Skill Average
    soft_cols = ['communication_score', 'leadership_score', 'teamwork_score', 'interview_score']
    df_feat['soft_skill_avg'] = np.round(df_feat[soft_cols].mean(axis=1), 2)
    
    # 3. Academic Score Index (0 to 100 scale, with backlog penalty)
    cgpa_val = df_feat['cgpa'].fillna(df_feat['cgpa'].median())
    att_val = df_feat['attendance_percentage'].fillna(df_feat['attendance_percentage'].median())
    backlogs_val = df_feat['backlogs'].fillna(0)
    
    academic_raw = (cgpa_val * 10.0 * 0.7) + (att_val * 0.3) - (backlogs_val * 10.0)
    df_feat['academic_score_index'] = np.round(np.clip(academic_raw, 0, 100), 2)
    
    # 4. Experience & Profile Score (0 to 100 scale)
    projects_score = df_feat['number_of_projects'] * 8.0 + df_feat['project_quality_score'] * 0.3
    internship_boost = df_feat['internship_experience'] * 20.0 + df_feat['internship_count'] * 8.0
    cert_boost = df_feat['number_of_certifications'] * 6.0 + df_feat['hackathons_attended'] * 4.0
    
    exp_raw = projects_score + internship_boost + cert_boost
    df_feat['experience_score'] = np.round(np.clip(exp_raw, 0, 100), 2)
    
    # 5. Overall Readiness Index (Domain-weighted benchmark)
    df_feat['overall_readiness_index'] = np.round(
        0.30 * df_feat['academic_score_index'] +
        0.35 * df_feat['technical_skill_avg'] +
        0.20 * df_feat['soft_skill_avg'] +
        0.15 * df_feat['experience_score'],
        2
    )
    
    print(f"[Feature Engineering] Added 5 domain aggregate features.")
    return df_feat

def check_feature_correlations(df, threshold=0.90):
    """
    Checks for highly correlated feature pairs to prevent severe multicollinearity.
    """
    num_df = df.select_dtypes(include=[np.number])
    corr_matrix = num_df.corr().abs()
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    
    high_corr_pairs = [
        (column, index, upper.loc[index, column])
        for column in upper.columns
        for index in upper.index
        if upper.loc[index, column] > threshold and index != 'placement_status' and column != 'placement_status'
    ]
    
    if high_corr_pairs:
        print(f"[Multicollinearity Warning] Highly correlated feature pairs (> {threshold}):")
        for f1, f2, val in high_corr_pairs:
            print(f"  - {f1} & {f2}: correlation = {val:.2f}")
    else:
        print(f"[Feature Engineering] No extreme multicollinearity (> {threshold}) detected.")
        
    return high_corr_pairs

if __name__ == "__main__":
    proc_path = "C:/Users/shyam/student-skills-placement-tracker/data/processed/student_placement_processed.csv"
    if os.path.exists(proc_path):
        df_proc = pd.read_csv(proc_path)
        df_feat = create_engineered_features(df_proc)
        check_feature_correlations(df_feat)
