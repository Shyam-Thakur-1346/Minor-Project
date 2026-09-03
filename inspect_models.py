"""
Helper Script: Inspect Contents of Serialized .pkl Model Files
Project: Student Skills and Placement Tracker
"""

import os
import joblib
import pandas as pd

models_dir = "C:/Users/shyam/student-skills-placement-tracker/models"

final_model_path = os.path.join(models_dir, "final_model.pkl")
preprocessor_path = os.path.join(models_dir, "preprocessor.pkl")
feature_info_path = os.path.join(models_dir, "feature_info.pkl")

print("================================================================================")
print("              INSPECTING SERIALIZED MODEL (.pkl) ARTIFACTS")
print("================================================================================\n")

# 1. Inspect final_model.pkl
print(">>> 1. CONTENTS OF 'final_model.pkl':")
if os.path.exists(final_model_path):
    final_model = joblib.load(final_model_path)
    print(f"    - Type: {type(final_model)}")
    print(f"    - Pipeline Steps: {list(final_model.named_steps.keys())}")
    print(f"    - Classifier Architecture: {final_model.named_steps['classifier']}")
else:
    print("    - File not found.")

print("\n--------------------------------------------------------------------------------")

# 2. Inspect preprocessor.pkl
print(">>> 2. CONTENTS OF 'preprocessor.pkl':")
if os.path.exists(preprocessor_path):
    preprocessor = joblib.load(preprocessor_path)
    print(f"    - Type: {type(preprocessor)}")
    print(f"    - Transformers in ColumnTransformer:")
    for name, trans, cols in preprocessor.transformers_:
        print(f"        * Transformer [{name}]: {trans}")
        print(f"          Target Columns ({len(cols)}): {cols[:5]}...")
else:
    print("    - File not found.")

print("\n--------------------------------------------------------------------------------")

# 3. Inspect feature_info.pkl
print(">>> 3. CONTENTS OF 'feature_info.pkl':")
if os.path.exists(feature_info_path):
    feature_info = joblib.load(feature_info_path)
    print(f"    - Type: {type(feature_info)}")
    print(f"    - Best Model Selected: {feature_info.get('best_model_name')}")
    print(f"    - Numerical Features Count: {len(feature_info.get('numerical_cols', []))}")
    print(f"    - Categorical Features Count: {len(feature_info.get('categorical_cols', []))}")
    print(f"    - Saved Test Metrics:")
    for metric, val in feature_info.get('test_metrics', {}).items():
        print(f"        * {metric}: {val}")
else:
    print("    - File not found.")

print("\n================================================================================\n")
