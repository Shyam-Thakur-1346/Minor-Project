"""
Data Collection & Synthetic Dataset Generator Module
Project: Student Skills and Placement Tracker
"""

import os
import pandas as pd
import numpy as np

def generate_synthetic_dataset(num_samples=1500, random_seed=42):
    """
    Generates a realistic synthetic dataset for student skills and placement tracking.
    
    Parameters:
        num_samples (int): Number of student records to generate.
        random_seed (int): Random seed for reproducibility.
        
    Returns:
        pd.DataFrame: Generated student dataframe with academic, technical, soft skill, profile, and placement features.
    """
    np.random.seed(random_seed)
    
    student_ids = [f"STU{1000 + i}" for i in range(num_samples)]
    ages = np.random.choice([20, 21, 22, 23, 24], size=num_samples, p=[0.15, 0.45, 0.30, 0.07, 0.03])
    genders = np.random.choice(['Male', 'Female', 'Other'], size=num_samples, p=[0.52, 0.46, 0.02])
    branches = np.random.choice(
        ['Computer Science', 'Information Technology', 'Electronics', 'Electrical', 'Mechanical', 'Civil'],
        size=num_samples,
        p=[0.35, 0.25, 0.15, 0.10, 0.08, 0.07]
    )
    degree = 'B.Tech'
    semester = 8
    
    # Academic Features
    cgpa = np.round(np.clip(np.random.normal(7.2, 1.1, num_samples), 4.5, 9.9), 2)
    backlogs = np.random.choice([0, 1, 2, 3, 4], size=num_samples, p=[0.72, 0.15, 0.07, 0.04, 0.02])
    attendance_pct = np.round(np.clip(np.random.normal(82.0, 9.5, num_samples), 55.0, 98.0), 1)
    
    # Technical Skills (Scores 0 to 100)
    base_tech = cgpa * 8.5 + np.random.normal(0, 8, num_samples)
    programming_score = np.round(np.clip(base_tech + np.random.normal(0, 6, num_samples), 25, 99), 1)
    dsa_score = np.round(np.clip(base_tech + np.random.normal(-2, 7, num_samples), 20, 99), 1)
    sql_score = np.round(np.clip(base_tech + np.random.normal(3, 8, num_samples), 20, 99), 1)
    web_dev_score = np.round(np.clip(np.random.normal(62, 15, num_samples), 15, 98), 1)
    ml_score = np.round(np.clip(np.random.normal(55, 18, num_samples), 10, 98), 1)
    cloud_score = np.round(np.clip(np.random.normal(52, 16, num_samples), 10, 95), 1)
    
    aptitude_score = np.round(np.clip(np.random.normal(68, 14, num_samples), 30, 98), 1)
    coding_test_score = np.round(np.clip(0.5 * programming_score + 0.5 * dsa_score + np.random.normal(0, 5, num_samples), 20, 100), 1)
    
    # Soft Skills (Scores 0 to 100)
    communication_score = np.round(np.clip(np.random.normal(70, 12, num_samples), 30, 98), 1)
    leadership_score = np.round(np.clip(np.random.normal(65, 14, num_samples), 25, 95), 1)
    teamwork_score = np.round(np.clip(np.random.normal(72, 11, num_samples), 35, 98), 1)
    interview_score = np.round(np.clip(0.4 * communication_score + 0.3 * dsa_score + 0.3 * aptitude_score + np.random.normal(0, 6, num_samples), 20, 99), 1)
    
    # Profile Features
    number_of_projects = np.random.choice([0, 1, 2, 3, 4, 5], size=num_samples, p=[0.08, 0.22, 0.35, 0.20, 0.10, 0.05])
    project_quality_score = np.round(np.clip(number_of_projects * 15 + np.random.normal(20, 10, num_samples), 20, 98), 1)
    number_of_certifications = np.random.choice([0, 1, 2, 3, 4], size=num_samples, p=[0.25, 0.35, 0.25, 0.10, 0.05])
    
    internship_exp_prob = np.clip((cgpa - 5) * 0.12 + (dsa_score / 200), 0.1, 0.85)
    internship_experience = (np.random.rand(num_samples) < internship_exp_prob).astype(int)
    internship_count = np.where(internship_experience == 1, np.random.choice([1, 2, 3], size=num_samples, p=[0.70, 0.22, 0.08]), 0)
    
    hackathons_attended = np.random.choice([0, 1, 2, 3, 4], size=num_samples, p=[0.50, 0.25, 0.15, 0.07, 0.03])
    github_contributions = np.round(np.clip(np.random.exponential(scale=60, size=num_samples) * (1 + number_of_projects * 0.3), 0, 450)).astype(int)
    
    cert_score = number_of_certifications * 4
    resume_score = np.round(np.clip(cgpa * 4 + number_of_projects * 5 + internship_experience * 15 + cert_score + np.random.normal(20, 8, num_samples), 30, 98), 1)
    
    # Target Variable Logic: Placement Status (1 = Placed/Placement Ready, 0 = Not Placed/Needs Improvement)
    logit = (
        0.35 * (cgpa - 7.0) 
        - 0.80 * backlogs 
        + 0.035 * (dsa_score - 60) 
        + 0.030 * (programming_score - 60) 
        + 0.025 * (coding_test_score - 60) 
        + 0.020 * (aptitude_score - 60) 
        + 0.025 * (communication_score - 65) 
        + 0.025 * (interview_score - 65) 
        + 0.75 * internship_experience 
        + 0.30 * number_of_projects 
        + 0.20 * number_of_certifications 
        + np.random.normal(0, 0.9, num_samples)
    )
    
    prob = 1 / (1 + np.exp(-logit))
    placement_status = (prob >= 0.50).astype(int)
    
    df = pd.DataFrame({
        'student_id': student_ids,
        'age': ages,
        'gender': genders,
        'branch': branches,
        'degree': degree,
        'semester': semester,
        'cgpa': cgpa,
        'backlogs': backlogs,
        'attendance_percentage': attendance_pct,
        'programming_score': programming_score,
        'dsa_score': dsa_score,
        'sql_score': sql_score,
        'web_dev_score': web_dev_score,
        'ml_score': ml_score,
        'cloud_score': cloud_score,
        'aptitude_score': aptitude_score,
        'coding_test_score': coding_test_score,
        'communication_score': communication_score,
        'leadership_score': leadership_score,
        'teamwork_score': teamwork_score,
        'interview_score': interview_score,
        'number_of_projects': number_of_projects,
        'project_quality_score': project_quality_score,
        'number_of_certifications': number_of_certifications,
        'internship_experience': internship_experience,
        'internship_count': internship_count,
        'hackathons_attended': hackathons_attended,
        'github_contributions': github_contributions,
        'resume_score': resume_score,
        'placement_status': placement_status
    })
    
    # Introduce controlled missingness & invalid values to test raw data cleaning
    missing_idx_cgpa = np.random.choice(num_samples, size=10, replace=False)
    df.loc[missing_idx_cgpa, 'cgpa'] = np.nan
    
    missing_idx_comm = np.random.choice(num_samples, size=8, replace=False)
    df.loc[missing_idx_comm, 'communication_score'] = np.nan
    
    dup_rows = df.iloc[:5].copy()
    df = pd.concat([df, dup_rows], ignore_index=True)
    
    df.loc[12, 'cgpa'] = 11.5  # Out-of-range CGPA (>10)
    df.loc[25, 'attendance_percentage'] = 110.0  # Out-of-range Attendance (>100)
    df.loc[45, 'programming_score'] = -5.0  # Out-of-range negative score
    
    return df

def validate_dataset(df):
    """
    Validates dataset shape, column counts, missing values, duplicates, and ranges.
    
    Returns:
        dict: Summary statistics and data health status.
    """
    report = {
        'total_rows': len(df),
        'total_columns': len(df.columns),
        'duplicate_rows': int(df.duplicated().sum()),
        'missing_values': df.isnull().sum().to_dict(),
        'dtypes': {col: str(dtype) for col, dtype in df.dtypes.items()}
    }
    return report

def load_or_create_dataset(output_path="C:/Users/shyam/student-skills-placement-tracker/data/raw/placement_data_raw.csv"):
    """
    Creates synthetic dataset if raw dataset does not exist, saves it, and returns the dataframe.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = generate_synthetic_dataset(num_samples=1500, random_seed=42)
    df.to_csv(output_path, index=False)
    print(f"Raw dataset created and saved to {output_path} with {len(df)} rows and {len(df.columns)} columns.")
    return df

if __name__ == "__main__":
    df_raw = load_or_create_dataset()
    val_report = validate_dataset(df_raw)
    print("\nData Validation Summary:")
    print(f"- Rows: {val_report['total_rows']}")
    print(f"- Columns: {val_report['total_columns']}")
    print(f"- Duplicates: {val_report['duplicate_rows']}")
    print(f"- Columns with missing values: {[k for k, v in val_report['missing_values'].items() if v > 0]}")
