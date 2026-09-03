"""
Student Skills and Placement Tracker - Master Pipeline Entrypoint
Project: Student Skills and Placement Tracker ML Pipeline
"""

import os
import sys

# Ensure root is in path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.data_collection import load_or_create_dataset, validate_dataset
from src.train import train_and_evaluate_all_models
from src.predict import StudentPlacementPredictor

def run_pipeline():
    print("================================================================================")
    print("   STUDENT SKILLS AND PLACEMENT TRACKER - MACHINE LEARNING PIPELINE")
    print("================================================================================\n")
    
    # Step 1: Data Collection / Generation
    print(">>> STEP 1: DATA COLLECTION & VALIDATION")
    df_raw = load_or_create_dataset()
    val_report = validate_dataset(df_raw)
    print(f"    - Raw Dataset Loaded: {val_report['total_rows']} records, {val_report['total_columns']} features.")
    
    # Step 2: Training, Tuning, Evaluation & Model Saving
    print("\n>>> STEP 2: MODEL TRAINING, CROSS-VALIDATION & HYPERPARAMETER TUNING")
    best_name, best_metrics, model_path = train_and_evaluate_all_models()
    
    # Step 3: Verification & Inference Test
    print("\n>>> STEP 3: TESTING SAVED PKL INFERENCE PIPELINE")
    predictor = StudentPlacementPredictor(model_path=model_path)
    
    sample_student = {
        'student_id': 'STU_VERIFY_999',
        'age': 21,
        'gender': 'Male',
        'branch': 'Computer Science',
        'degree': 'B.Tech',
        'semester': 8,
        'cgpa': 8.5,
        'backlogs': 0,
        'attendance_percentage': 90.0,
        'programming_score': 82.0,
        'dsa_score': 80.0,
        'sql_score': 78.0,
        'web_dev_score': 75.0,
        'ml_score': 70.0,
        'cloud_score': 68.0,
        'aptitude_score': 80.0,
        'coding_test_score': 82.0,
        'communication_score': 82.0,
        'leadership_score': 78.0,
        'teamwork_score': 85.0,
        'interview_score': 80.0,
        'number_of_projects': 3,
        'project_quality_score': 80.0,
        'number_of_certifications': 2,
        'internship_experience': 1,
        'internship_count': 1,
        'hackathons_attended': 1,
        'github_contributions': 120,
        'resume_score': 82.0
    }
    
    result = predictor.predict_single_student(sample_student)
    
    print("\n--------------------------------------------------------------------------------")
    print("   FINAL PIPELINE VERIFICATION SUCCESSFUL!")
    print("--------------------------------------------------------------------------------")
    print(f"Selected Model      : {best_name}")
    print(f"Test F1-Score       : {best_metrics['F1 Score']}")
    print(f"Test Accuracy       : {best_metrics['Accuracy']}")
    print(f"Test Precision      : {best_metrics['Precision']}")
    print(f"Test Recall         : {best_metrics['Recall']}")
    print(f"Test ROC-AUC        : {best_metrics['ROC-AUC']}")
    print(f"Saved Model Location: {model_path}")
    print(f"Sample Student Prob : {result['confidence_percentage']} ({result['readiness_category']})")
    print("================================================================================\n")

if __name__ == "__main__":
    run_pipeline()
