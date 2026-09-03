"""
Inference & Prediction Pipeline Module
Project: Student Skills and Placement Tracker
"""

import os
import sys

# Ensure project root is in Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import joblib
import pandas as pd
import numpy as np

from src.feature_engineering import create_engineered_features

class StudentPlacementPredictor:
    """
    Inference class for loading serialized model pipelines and evaluating student placement readiness.
    """
    def __init__(
        self,
        model_path="C:/Users/shyam/student-skills-placement-tracker/models/final_model.pkl",
        feature_info_path="C:/Users/shyam/student-skills-placement-tracker/models/feature_info.pkl"
    ):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}. Train the model first.")
            
        self.model_pipeline = joblib.load(model_path)
        self.feature_info = joblib.load(feature_info_path) if os.path.exists(feature_info_path) else None
        print(f"[Predictor] Successfully loaded model pipeline from {model_path}.")
        
    def _evaluate_improvement_areas(self, student_row):
        """
        Analyzes individual student metrics against benchmark standards to provide personalized recommendations.
        """
        recommendations = []
        
        # 1. Technical Skills Check
        if student_row.get('dsa_score', 100) < 65:
            recommendations.append(f"DSA & Data Structures (Current: {student_row.get('dsa_score', 'N/A')}/100, Benchmark: 65+)")
        if student_row.get('programming_score', 100) < 65:
            recommendations.append(f"Programming Fundamentals (Current: {student_row.get('programming_score', 'N/A')}/100, Benchmark: 65+)")
        if student_row.get('coding_test_score', 100) < 65:
            recommendations.append(f"Hands-on Coding Test Practice (Current: {student_row.get('coding_test_score', 'N/A')}/100, Benchmark: 65+)")
        if student_row.get('aptitude_score', 100) < 60:
            recommendations.append(f"Quantitative & Logical Aptitude (Current: {student_row.get('aptitude_score', 'N/A')}/100, Benchmark: 60+)")
            
        # 2. Soft Skills & Interview
        if student_row.get('communication_score', 100) < 65:
            recommendations.append(f"Communication & Verbal Skills (Current: {student_row.get('communication_score', 'N/A')}/100, Benchmark: 65+)")
        if student_row.get('interview_score', 100) < 65:
            recommendations.append(f"Mock Interview Preparation (Current: {student_row.get('interview_score', 'N/A')}/100, Benchmark: 65+)")
            
        # 3. Profile & Practical Experience
        if student_row.get('internship_experience', 1) == 0:
            recommendations.append("Industrial Internship Experience (Target: Complete at least 1 relevant internship)")
        if student_row.get('number_of_projects', 5) < 2:
            recommendations.append("Portfolio Projects (Target: Build at least 2 full-stack/domain projects)")
        if student_row.get('backlogs', 0) > 0:
            recommendations.append(f"Academic Backlogs (Active backlogs: {student_row.get('backlogs')}. Target: 0 backlogs)")
            
        if not recommendations:
            recommendations.append("Profile is strong across all primary evaluation metrics. Focus on competitive coding and advanced interview prep.")
            
        return recommendations

    def predict_single_student(self, student_dict):
        """
        Predicts placement status, readiness probability, readiness tier, and areas for improvement for a single student.
        
        Parameters:
            student_dict (dict): Dictionary of raw student metrics.
            
        Returns:
            dict: Structured prediction results.
        """
        df_single = pd.DataFrame([student_dict])
        
        # Apply feature engineering
        df_feat = create_engineered_features(df_single)
        
        # Predict class and probability
        pred_class = int(self.model_pipeline.predict(df_feat)[0])
        
        if hasattr(self.model_pipeline, "predict_proba"):
            prob = float(self.model_pipeline.predict_proba(df_feat)[0][1])
        else:
            prob = 1.0 if pred_class == 1 else 0.0
            
        # Classify readiness tier
        if prob >= 0.75:
            readiness_category = "Placement Ready"
            status_summary = "High Probability of Placement / Strong Candidate"
        elif prob >= 0.50:
            readiness_category = "Internship Ready / Moderate Placement Readiness"
            status_summary = "Ready for Internships & Entry-Level Roles; Minor Skill Refinement Recommended"
        else:
            readiness_category = "Needs Improvement"
            status_summary = "Not Currently Placement Ready; Significant Skill Development Required"
            
        areas_to_improve = self._evaluate_improvement_areas(student_dict)
        
        return {
            'student_id': student_dict.get('student_id', 'STU_SAMPLE'),
            'predicted_class': pred_class,
            'placement_readiness_probability': round(prob, 4),
            'confidence_percentage': f"{round(prob * 100, 2)}%",
            'readiness_category': readiness_category,
            'status_summary': status_summary,
            'engineered_scores': {
                'academic_score_index': float(df_feat['academic_score_index'].iloc[0]),
                'technical_skill_avg': float(df_feat['technical_skill_avg'].iloc[0]),
                'soft_skill_avg': float(df_feat['soft_skill_avg'].iloc[0]),
                'experience_score': float(df_feat['experience_score'].iloc[0]),
                'overall_readiness_index': float(df_feat['overall_readiness_index'].iloc[0])
            },
            'areas_for_improvement': areas_to_improve
        }

if __name__ == "__main__":
    predictor = StudentPlacementPredictor()
    
    sample_student_ready = {
        'student_id': 'STU_TEST_01',
        'age': 21,
        'gender': 'Female',
        'branch': 'Computer Science',
        'degree': 'B.Tech',
        'semester': 8,
        'cgpa': 8.8,
        'backlogs': 0,
        'attendance_percentage': 92.0,
        'programming_score': 88.0,
        'dsa_score': 85.0,
        'sql_score': 80.0,
        'web_dev_score': 78.0,
        'ml_score': 75.0,
        'cloud_score': 70.0,
        'aptitude_score': 82.0,
        'coding_test_score': 86.0,
        'communication_score': 85.0,
        'leadership_score': 75.0,
        'teamwork_score': 88.0,
        'interview_score': 84.0,
        'number_of_projects': 3,
        'project_quality_score': 85.0,
        'number_of_certifications': 2,
        'internship_experience': 1,
        'internship_count': 1,
        'hackathons_attended': 2,
        'github_contributions': 150,
        'resume_score': 85.0
    }
    
    res_ready = predictor.predict_single_student(sample_student_ready)
    print("\n--- SAMPLE PREDICTION (Placement Ready) ---")
    print(f"Student ID: {res_ready['student_id']}")
    print(f"Prediction Category: {res_ready['readiness_category']}")
    print(f"Readiness Probability: {res_ready['confidence_percentage']}")
    print(f"Overall Index: {res_ready['engineered_scores']['overall_readiness_index']}/100")
    print("Areas for Improvement:")
    for area in res_ready['areas_for_improvement']:
        print(f" - {area}")
        
    sample_student_needs_work = {
        'student_id': 'STU_TEST_02',
        'age': 22,
        'gender': 'Male',
        'branch': 'Mechanical',
        'degree': 'B.Tech',
        'semester': 8,
        'cgpa': 6.1,
        'backlogs': 2,
        'attendance_percentage': 68.0,
        'programming_score': 45.0,
        'dsa_score': 40.0,
        'sql_score': 50.0,
        'web_dev_score': 40.0,
        'ml_score': 30.0,
        'cloud_score': 35.0,
        'aptitude_score': 52.0,
        'coding_test_score': 42.0,
        'communication_score': 55.0,
        'leadership_score': 50.0,
        'teamwork_score': 60.0,
        'interview_score': 48.0,
        'number_of_projects': 1,
        'project_quality_score': 40.0,
        'number_of_certifications': 0,
        'internship_experience': 0,
        'internship_count': 0,
        'hackathons_attended': 0,
        'github_contributions': 12,
        'resume_score': 48.0
    }
    
    res_work = predictor.predict_single_student(sample_student_needs_work)
    print("\n--- SAMPLE PREDICTION (Needs Improvement) ---")
    print(f"Student ID: {res_work['student_id']}")
    print(f"Prediction Category: {res_work['readiness_category']}")
    print(f"Readiness Probability: {res_work['confidence_percentage']}")
    print(f"Overall Index: {res_work['engineered_scores']['overall_readiness_index']}/100")
    print("Areas for Improvement:")
    for area in res_work['areas_for_improvement']:
        print(f" - {area}")
