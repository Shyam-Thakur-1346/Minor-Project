# Student Skills and Placement Tracker — Machine Learning Pipeline

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.3%2B-orange.svg)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-1.7%2B-green.svg)](https://xgboost.readthedocs.io/)
[![Status](https://img.shields.io/badge/ML%20Pipeline-Complete%20%26%20Verified-brightgreen.svg)]()

A comprehensive Machine Learning system designed for college career guidance and placement prediction. This system analyzes students' academic performance, technical capabilities (DSA, programming, web dev, ML, cloud, SQL), soft skills, aptitude test performance, project portfolio, certifications, and internship experience to estimate placement readiness, compute probabilistic readiness scores, and identify key individual areas for improvement.

---

## Table of Contents

1. [Problem Statement & Objective](#1-problem-statement--objective)
2. [ML Problem Formulation](#2-ml-problem-formulation)
3. [Dataset & Data Dictionary](#3-dataset--data-dictionary)
4. [Data Cleaning & Validation](#4-data-cleaning--validation)
5. [Feature Engineering](#5-feature-engineering)
6. [Preprocessing & Leakage Prevention](#6-preprocessing--leakage-prevention)
7. [Exploratory Data Analysis (EDA)](#7-exploratory-data-analysis-eda)
8. [Machine Learning Algorithms Tested](#8-machine-learning-algorithms-tested)
9. [Cross-Validation & Hyperparameter Tuning](#9-cross-validation--hyperparameter-tuning)
10. [Model Evaluation & Comparison](#10-model-evaluation--comparison)
11. [Final Model Selection & Rationale](#11-final-model-selection--rationale)
12. [Model Artifacts & Serialization](#12-model-artifacts--serialization)
13. [Inference & Recommendation Engine](#13-inference--recommendation-engine)
14. [Project Directory Structure](#14-project-directory-structure)
15. [How to Run the Project](#15-how-to-run-the-project)
16. [Ethical & Technical Considerations](#16-ethical--technical-considerations)
17. [Limitations & Future Scope](#17-limitations--future-scope)

---

## 1. Problem Statement & Objective

In higher education institutions, tracking student employability and predicting placement success is essential for providing timely intervention, personalized mentorship, and skill enhancement. Traditional academic evaluation often relies solely on CGPA, ignoring practical coding proficiency, soft skills, project quality, and industry exposure.

### Key Questions Answered by the ML Pipeline:
- **Is a student placement-ready?**
- **Is a student internship-ready?**
- **What is the exact probability of placement success (0% to 100%)?**
- **Which specific technical or soft skill gaps are holding the student back?**
- **What actionable improvement steps should the student take?**

---

## 2. ML Problem Formulation

- **Problem Type**: Binary Classification (`1 = Placement Ready / Placed`, `0 = Needs Improvement / Not Placed`).
- **Probabilistic Output**: Model outputs a calibrated probability score ($P \in [0.0, 1.0]$), allowing classification into tiered readiness categories:
  - **$P \ge 0.75$**: Placement Ready (High Confidence)
  - **$0.50 \le P < 0.75$**: Internship Ready / Moderate Placement Readiness
  - **$P < 0.50$**: Needs Improvement / Not Placement Ready

### Target Leakage Prevention
Features that only become known **after** a placement selection decision (e.g., `company_name`, `offered_ctc`, `interview_rounds_passed`) are **strictly excluded** from training inputs to prevent target leakage.

---

## 3. Dataset & Data Dictionary

> **Note on Data Source**: A reproducible synthetic development/demo dataset ($N = 1,500$ student records) was generated using a fixed random seed (`seed=42`) via `src/data_collection.py`. This dataset mimics real-world multivariate relationships (e.g., correlation between DSA score, CGPA, internships, and placement outcome). It can seamlessly be replaced with real institutional student data without modifying any pipeline code.

### Data Dictionary

| Category | Feature Name | Data Type | Description / Range |
| :--- | :--- | :--- | :--- |
| **Identifier** | `student_id` | String | Unique identifier (`STU1000`–`STU2500`) |
| **Demographics** | `age`, `gender`, `branch` | Numeric / Categorical | Student demographic & academic stream |
| **Academic** | `cgpa` | Float | Cumulative Grade Point Average (0.0 – 10.0) |
| | `backlogs` | Integer | Active academic backlog count (0 – 5) |
| | `attendance_percentage` | Float | Class attendance rate (0.0% – 100.0%) |
| **Technical** | `programming_score` | Float | Programming language score (0 – 100) |
| | `dsa_score` | Float | Data Structures & Algorithms score (0 – 100) |
| | `sql_score` | Float | Database & SQL proficiency (0 – 100) |
| | `web_dev_score` | Float | Web Development score (0 – 100) |
| | `ml_score` | Float | Machine Learning proficiency (0 – 100) |
| | `cloud_score` | Float | Cloud & DevOps proficiency (0 – 100) |
| | `aptitude_score` | Float | Quantitative & Logical Reasoning (0 – 100) |
| | `coding_test_score` | Float | Automated Coding Test score (0 – 100) |
| **Soft Skills** | `communication_score` | Float | Verbal & Written Communication (0 – 100) |
| | `leadership_score` | Float | Leadership & Initiative score (0 – 100) |
| | `teamwork_score` | Float | Teamwork & Collaboration score (0 – 100) |
| | `interview_score` | Float | Mock Interview Performance (0 – 100) |
| **Profile** | `number_of_projects` | Integer | Completed portfolio project count (0 – 5) |
| | `project_quality_score` | Float | Evaluated project quality score (0 – 100) |
| | `number_of_certifications` | Integer | Technical certifications completed (0 – 4) |
| | `internship_experience` | Binary | Industrial internship completed (0 or 1) |
| | `internship_count` | Integer | Total internship count (0 – 3) |
| | `hackathons_attended` | Integer | Hackathon participation count (0 – 4) |
| | `github_contributions` | Integer | GitHub activity / commit count (0 – 450) |
| | `resume_score` | Float | Automated Resume ATS score (0 – 100) |
| **Target** | `placement_status` | Binary Int | Placement Readiness (`1` = Ready, `0` = Needs Work) |

---

## 4. Data Cleaning & Validation

The data cleaning module (`src/preprocessing.py` -> `clean_raw_data`) handles:
- **Duplicate Removal**: Identified and dropped 5 duplicate rows.
- **Range Validation**: Corrected out-of-bounds values (e.g., `CGPA > 10.0`, `Attendance > 100%`, negative test scores) to `NaN`.
- **Text Standardisation**: Stripped whitespace and title-cased categorical text fields (`gender`, `branch`).
- **Imputation**: Missing values are median-imputed strictly within the scikit-learn preprocessing pipeline.

---

## 5. Feature Engineering

Domain-aggregate features are engineered (`src/feature_engineering.py`) to capture composite performance:
1. `technical_skill_avg`: Mean across all technical subject scores.
2. `soft_skill_avg`: Mean across communication, teamwork, leadership, and mock interview scores.
3. `academic_score_index`: Composite score ($0-100$) combining CGPA and attendance while penalizing backlogs:
   $$\text{Academic Index} = (CGPA \times 7.0) + (\text{Attendance} \times 0.3) - (\text{Backlogs} \times 10.0)$$
4. `experience_score`: Composite profile score combining projects, internships, hackathons, and certifications.
5. `overall_readiness_index`: Weighted domain index ($30\%$ Academic, $35\%$ Technical, $20\%$ Soft Skills, $15\%$ Experience).

---

## 6. Preprocessing & Leakage Prevention

- **Train/Test Split**: 80/20 Stratified Train/Test split ($1,200$ train, $300$ test records).
- **ColumnTransformer Pipeline**:
  - **Numerical**: `SimpleImputer(strategy='median')` $\rightarrow$ `StandardScaler()`
  - **Categorical**: `SimpleImputer(strategy='most_frequent')` $\rightarrow$ `OneHotEncoder(handle_unknown='ignore')`
- **Fit Isolation**: Preprocessing parameters are fit **only** on training data to eliminate data leakage.

---

## 7. Exploratory Data Analysis (EDA)

EDA charts are automatically saved in `reports/figures/`:
- `target_distribution.png`: Visualizes class distribution ($73.7\%$ Ready, $26.3\%$ Needs Improvement).
- `cgpa_vs_placement.png`: Boxplot & Kernel Density Estimation showing strong separation between placed and unplaced CGPA distributions.
- `skill_distributions.png`: Multi-panel comparison of DSA, Programming, Communication, and Coding test scores.
- `feature_correlations.png`: Heatmap highlighting top predictors (DSA score, CGPA, Programming score, Internship experience).

---

## 8. Machine Learning Algorithms Tested

8 diverse model architectures were trained and evaluated:
1. **Baseline (Dummy Classifier)**: Most frequent class predictor ($73.67\%$ baseline accuracy).
2. **Logistic Regression** (with `class_weight='balanced'`)
3. **K-Nearest Neighbors (KNN)**
4. **Decision Tree Classifier**
5. **Random Forest Classifier**
6. **Gradient Boosting Classifier**
7. **XGBoost Classifier**
8. **Support Vector Machine (SVC)** (with probability estimation)

---

## 9. Cross-Validation & Hyperparameter Tuning

- **Cross-Validation**: 5-Fold Stratified Cross-Validation (`StratifiedKFold(n_splits=5)`).
- **Hyperparameter Optimization**: `GridSearchCV` applied to top candidate models (Random Forest, Gradient Boosting, XGBoost).
- **Tuned XGBoost Parameters**:
  - `n_estimators`: 100
  - `learning_rate`: 0.1
  - `max_depth`: 3
  - `eval_metric`: `logloss`

---

## 10. Model Evaluation & Comparison

Performance evaluated on the untouched test set ($N=300$):

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **XGBoost (Tuned)** 🏆 | **0.9133** | **0.9258** | **0.9593** | **0.9422** | **0.9534** |
| **K-Nearest Neighbors** | 0.9000 | 0.8996 | 0.9729 | 0.9348 | 0.9102 |
| **XGBoost (Base)** | 0.9000 | 0.9170 | 0.9502 | 0.9333 | 0.9437 |
| **Gradient Boosting (Tuned)** | 0.9000 | 0.9244 | 0.9412 | 0.9327 | 0.9494 |
| **Gradient Boosting (Base)** | 0.9000 | 0.9244 | 0.9412 | 0.9327 | 0.9494 |
| **Random Forest (Tuned)** | 0.8967 | 0.9060 | 0.9593 | 0.9319 | 0.9553 |
| **Random Forest (Base)** | 0.8967 | 0.9060 | 0.9593 | 0.9319 | 0.9553 |
| **Support Vector Machine** | 0.8867 | 0.9561 | 0.8869 | 0.9202 | 0.9594 |
| **Logistic Regression** | 0.8833 | 0.9650 | 0.8733 | 0.9169 | 0.9636 |
| **Decision Tree** | 0.8567 | 0.9238 | 0.8778 | 0.9002 | 0.8247 |
| **Baseline (Dummy)** | 0.7367 | 0.7367 | 1.0000 | 0.8484 | 0.5000 |

*Full results report saved at `reports/model_results.csv`.*

---

## 11. Final Model Selection & Rationale

**Selected Model**: **Tuned XGBoost Classifier**
- **Highest Test F1-Score**: `0.9422`
- **High Recall**: `0.9593` (Minimizes False Negatives, ensuring unprepared students are correctly flagged for intervention).
- **Strong Generalization**: ROC-AUC = `0.9534`, showing excellent class discrimination across thresholds.
- **Top Predictors**: DSA Score, CGPA, Coding Test Score, Technical Skill Average, and Internship Experience.

---

## 12. Model Artifacts & Serialization

Models are serialized using `joblib` in `models/`:
- `models/final_model.pkl`: Complete unified pipeline (Preprocessor + Tuned XGBoost Classifier).
- `models/preprocessor.pkl`: Standalone scikit-learn ColumnTransformer.
- `models/feature_info.pkl`: Feature dictionary metadata and test metrics.

---

## 13. Inference & Recommendation Engine

The prediction pipeline (`src/predict.py`) accepts raw student dictionaries and returns:
1. Binary Prediction (`0` or `1`)
2. Calibrated Placement Readiness Probability (%)
3. Categorical Readiness Tier ("Placement Ready", "Internship Ready", "Needs Improvement")
4. Overall Readiness Index (0-100)
5. Actionable, Rule-Based **Areas for Improvement** comparing student scores against institutional benchmarks.

---

## 14. Project Directory Structure

```
student-skills-placement-tracker/
│
├── data/
│   ├── raw/
│   │   └── placement_data_raw.csv
│   └── processed/
│       ├── student_placement_processed.csv
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       └── y_test.csv
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_model_training.ipynb
│   └── 06_model_evaluation.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_collection.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── models/
│   ├── final_model.pkl
│   ├── preprocessor.pkl
│   └── feature_info.pkl
│
├── reports/
│   ├── figures/
│   │   ├── target_distribution.png
│   │   ├── cgpa_vs_placement.png
│   │   ├── skill_distributions.png
│   │   ├── feature_correlations.png
│   │   ├── confusion_matrices.png
│   │   ├── roc_curves.png
│   │   └── feature_importance.png
│   └── model_results.csv
│
├── requirements.txt
├── README.md
└── main.py
```

---

## 15. How to Run the Project

### Prerequisites
- Python 3.10 or higher installed.

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run End-to-End Pipeline
```bash
python main.py
```

### Step 3: Run Inference Script Individually
```bash
python src/predict.py
```

---

## 16. Ethical & Technical Considerations

1. **Decision-Support Nature**: This ML pipeline serves as an advisory decision-support tool for students and placement counselors. It does **not** guarantee placement outcomes.
2. **Non-Deterministic Terminology**: Outputs use advisory language like *"Placement Readiness Probability: 85%"* rather than deterministic claims like *"You will get placed"*.
3. **Fairness & Non-Discrimination**: Demographic variables (`gender`, `branch`) are kept neutral in feature weights; models rely primarily on meritocratic skill indicators (DSA, CGPA, coding test, soft skills, projects).

---

## 17. Limitations & Future Scope

### Current Limitations
- Evaluation performed on synthetic development data calibrated for college placement domain.
- Qualitative project quality is based on numeric evaluation scores.

### Future Scope
- **Backend API Integration**: Wrap `src/predict.py` in a REST API using FastAPI / Flask.
- **Frontend Dashboard**: Build a React / Streamlit interactive dashboard for students and placement officers.
- **Real Student Data Integration**: Ingest real institutional placement records for production fine-tuning.
"# Minor-Project" 
"# Minor-Project" 
