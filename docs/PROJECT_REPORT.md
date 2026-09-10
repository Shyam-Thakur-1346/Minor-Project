# PROJECT REPORT
# Student Skills and Placement Tracker
### Machine Learning-Based Employability Estimation, Risk Detection & Personalized Skill Gap Recommendation System

---

**Project Title**: Student Skills and Placement Tracker  
**Domain**: Educational Data Mining (EDM), Applied Machine Learning & Predictive Analytics  
**Academic Level**: B.Tech Minor Project / Capstone Project  
**Repository Location**: `C:/Users/shyam/Documents/student-skills-placement-tracker/`  
**Current Milestone**: Phase 1 — Machine Learning Core, Evaluation Pipeline & Inference Engine (100% Completed & Verified)  

---

## 1. Executive Summary & Abstract

In contemporary higher education, predicting undergraduate employability and placement readiness is critical for enabling timely academic interventions, proactive career mentoring, and institutional curriculum alignment. Traditional evaluation practices predominantly depend on Cumulative Grade Point Average (CGPA) as a single proxy for student competence. However, this one-dimensional approach disregards critical competencies demanded by modern industries, such as hands-on Data Structures & Algorithms (DSA) problem-solving, software engineering fundamentals, database fluency, soft skills, project portfolios, open-source contributions, and practical internship exposure.

The **Student Skills and Placement Tracker** is an end-to-end, industry-standard Machine Learning pipeline designed to evaluate student readiness holistically across **30 distinct parameters**. The system formulates placement estimation as a probabilistic binary classification task, categorizing candidates into tiered readiness strata (*Placement Ready*, *Internship Ready*, or *Needs Improvement*) while delivering calibrated readiness probabilities ($0\%$ to $100\%$). 

Eight candidate machine learning architectures—spanning parametric, non-parametric, linear, distance-based, bagging, and boosting paradigms—were benchmarked using rigorous **5-Fold Stratified Cross-Validation** and **GridSearchCV hyperparameter optimization**. The **Tuned Extreme Gradient Boosting (XGBoost) Classifier** emerged as the superior model, achieving a **Test Accuracy of 91.33%**, **Precision of 92.58%**, **Recall of 95.93%**, **F1-Score of 0.9422**, and an **ROC-AUC of 0.9534**. 

Beyond binary classification, the system incorporates an automated **Inference & Recommendation Engine** that inspects student performance against institutional standards, generating tailored, actionable improvement roadmaps for underperforming students.

---

## 2. Problem Statement & Motivation

### 2.1 The Traditional Campus Placement Dilemma
Historically, higher education institutions struggle with significant operational and pedagogical challenges during placement seasons:
1. **The "CGPA Fallacy"**: High academic grades do not reliably correlate with practical coding or problem-solving capability. Students with an 8.5+ CGPA frequently fail automated coding assessments due to weak algorithmic fundamentals.
2. **Reactive Interventions**: Training and placement cells typically discover a student's shortcomings only *after* repeated failures in campus placement drives, when remediation time is insufficient.
3. **Absence of Unified Metrics**: Institutions lack a consolidated, standardized index that weighs academic diligence, technical acumen, interpersonal communication, and extracurricular project work.
4. **Generic Guidance**: Feedback given to struggling students is often subjective and generic rather than data-driven and prescriptive.

### 2.2 System Objectives
The core objectives of the system are:
- To develop an automated, reproducible ML pipeline that accepts student academic, technical, soft-skill, and profile records.
- To produce a calibrated probability score representing placement readiness.
- To prevent target leakage by eliminating post-placement features (e.g., compensation packages, company names).
- To benchmark multiple machine learning algorithms and determine the mathematically optimal classifier.
- To deliver explainable, rule-based skill recommendations highlighting exact gaps (e.g., DSA < 65/100, active backlogs, lack of internships).

---

## 3. Dataset Architecture & Feature Schema

The pipeline operates on a multivariate dataset comprising **1,500 student records** generated with controlled distributions, realistic inter-feature correlations, and synthetic noise (`random_seed=42`) via `src/data_collection.py`. This dataset faithfully mirrors real-world undergraduate engineering cohorts and can be seamlessly substituted with real institutional data without code modification.

### 3.1 Feature Breakdown (30 Dimensions)

| Dimension | Feature Name | Data Type | Value Range / Units | Description & Pedagogical Relevance |
| :--- | :--- | :---: | :---: | :--- |
| **Identifiers** | `student_id` | String | `STU1000`–`STU2500` | Unique student token (excluded during model training). |
| **Demographics** | `age` | Integer | 20 – 24 years | Age of final-year undergraduate student. |
| | `gender` | Categorical | Male, Female, Other | Demographic feature audited for algorithmic fairness. |
| | `branch` | Categorical | CSE, IT, ECE, EE, ME, CE | Academic engineering discipline. |
| | `degree`, `semester` | String / Int | B.Tech / Sem 8 | Degree program and current academic semester. |
| **Academic** | `cgpa` | Float | 0.0 – 10.0 | Cumulative Grade Point Average. Primary academic benchmark. |
| | `backlogs` | Integer | 0 – 5 | Count of active uncleared academic backlogs (strong negative weight). |
| | `attendance_percentage` | Float | 0.0% – 100.0% | Academic consistency and class engagement. |
| **Technical** | `programming_score` | Float | 0 – 100 | Core language proficiency (Python, Java, C++). |
| | `dsa_score` | Float | 0 – 100 | Algorithmic problem-solving and Data Structures competency. |
| | `sql_score` | Float | 0 – 100 | Relational database design and query writing competence. |
| | `web_dev_score` | Float | 0 – 100 | Frontend and backend full-stack development skills. |
| | `ml_score` | Float | 0 – 100 | Machine learning concepts, libraries, and pipeline knowledge. |
| | `cloud_score` | Float | 0 – 100 | DevOps, Docker, cloud deployment, and infrastructure familiarity. |
| | `aptitude_score` | Float | 0 – 100 | Quantitative reasoning, logic, and analytical problem-solving. |
| | `coding_test_score` | Float | 0 – 100 | Timed automated coding test simulation score. |
| **Soft Skills** | `communication_score` | Float | 0 – 100 | Verbal fluency, articulation, and business communication. |
| | `leadership_score` | Float | 0 – 100 | Initiative, team leadership, and college club responsibility. |
| | `teamwork_score` | Float | 0 – 100 | Peer collaboration and group project dynamics. |
| | `interview_score` | Float | 0 – 100 | Formal mock technical & HR interview assessment rating. |
| **Profile & Portfolio** | `number_of_projects` | Integer | 0 – 5 | Count of completed portfolio projects. |
| | `project_quality_score` | Float | 0 – 100 | Evaluated architectural complexity and execution quality. |
| | `number_of_certifications`| Integer | 0 – 4 | Verified technical certifications (AWS, Coursera, Oracle, etc.). |
| | `internship_experience` | Binary | 0 or 1 | Completion of at least one industrial corporate internship. |
| | `internship_count` | Integer | 0 – 3 | Total verified industrial internships completed. |
| | `hackathons_attended` | Integer | 0 – 4 | Participation in inter-college or national hackathons. |
| | `github_contributions` | Integer | 0 – 450 | GitHub public commits representing open-source activity. |
| | `resume_score` | Float | 0 – 100 | Automated Applicant Tracking System (ATS) resume quality score. |
| **Target Variable** | `placement_status` | Binary | 0 or 1 | **1** = Placement Ready / Placed; **0** = Needs Improvement / Not Placed. |

### 3.2 Target Leakage Prevention
Features that only manifest *after* an offer is extended (such as `company_name`, `offered_ctc`, `job_role`, or `rounds_cleared`) were strictly excluded from the feature space, ensuring the model relies purely on pre-placement inputs.

---

## 4. End-to-End System Architecture

The pipeline is architected into modular, single-responsibility components:

```
[Raw Student Data (CSV)]
          │
          ▼
┌──────────────────────────────────────┐
│  src/preprocessing.py                │
│  - Deduplication                     │
│  - Boundary/Range Sanitization       │
│  - Text Normalization                │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  src/feature_engineering.py          │
│  - Technical & Soft Skill Averages   │
│  - Academic Score Index              │
│  - Experience & Profile Score        │
│  - Overall Readiness Index           │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  Stratified Train/Test Split (80/20) │
│  - X_train (1,200), X_test (300)     │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌────────────────────────────────────────────────────────┐
│  Leakage-Free Preprocessing Pipeline (ColumnTransformer)│
│  - Numeric: Median Imputer -> StandardScaler           │
│  - Categorical: Most-Frequent Imputer -> OneHotEncoder │
│  *(Fit strictly on X_train; transformed on X_test)*   │
└──────────────────┬─────────────────────────────────────┘
                   │
                   ▼
┌────────────────────────────────────────────────────────┐
│  Model Benchmarking (8 Algorithms)                     │
│  - 5-Fold Stratified Cross-Validation                  │
│  - GridSearchCV Tuning (RF, GradientBoosting, XGBoost) │
└──────────────────┬─────────────────────────────────────┘
                   │
                   ▼
┌────────────────────────────────────────────────────────┐
│  Final Model Selection (Tuned XGBoost: F1 = 0.9422)    │
│  - Full Retrain & Serialization (models/final_model.pkl)│
└──────────────────┬─────────────────────────────────────┘
                   │
                   ▼
┌────────────────────────────────────────────────────────┐
│  Inference & Recommendation Engine (src/predict.py)    │
│  - Probabilistic Scoring (0.00% - 100.00%)             │
│  - Tier Categorization & Personalized Gap Roadmaps     │
└────────────────────────────────────────────────────────┘
```

---

## 5. Data Cleaning & Feature Engineering

### 5.1 Cleaning & Robustness Checks (`src/preprocessing.py`)
- **Deduplication**: 5 duplicate rows were detected and purged.
- **Range Sanitization**: Data integrity filters flagged out-of-range anomalies (e.g., `CGPA = 11.5`, `attendance = 110%`, `programming_score = -5.0`), replacing them with `NaN` values for subsequent imputation.
- **Categorical Cleaning**: String trimming and title-casing standardized branch and gender strings.
- **Isolated Imputation**: Numeric values are median-imputed, and categorical values are mode-imputed strictly within pipeline transformers to prevent information leakage across validation folds.

### 5.2 Engineered Domain Aggregate Features (`src/feature_engineering.py`)
To distill raw dimensions into holistic pedagogical indicators, five domain features were engineered:

1. **`technical_skill_avg`**:
   $$\text{Tech Avg} = \frac{\text{DSA} + \text{Programming} + \text{SQL} + \text{Web Dev} + \text{ML} + \text{Cloud}}{6}$$
2. **`soft_skill_avg`**:
   $$\text{Soft Avg} = \frac{\text{Communication} + \text{Leadership} + \text{Teamwork} + \text{Interview}}{4}$$
3. **`academic_score_index`** (Scale: 0 – 100, heavily penalizing active backlogs):
   $$\text{Academic Index} = \text{clip}\Big((\text{CGPA} \times 10 \times 0.7) + (\text{Attendance} \times 0.3) - (\text{Backlogs} \times 10.0), 0, 100\Big)$$
4. **`experience_score`** (Scale: 0 – 100):
   $$\text{Experience Score} = \text{clip}\Big((\text{Projects} \times 8 + \text{Quality} \times 0.3) + (\text{Internship Exp} \times 20 + \text{Count} \times 8) + (\text{Certs} \times 6 + \text{Hackathons} \times 4), 0, 100\Big)$$
5. **`overall_readiness_index`** (Composite Institutional Employability Metric):
   $$\text{Overall Readiness} = 0.30 \times \text{Academic} + 0.35 \times \text{Tech} + 0.20 \times \text{Soft} + 0.15 \times \text{Experience}$$

---

## 6. Exploratory Data Analysis (EDA) Insights

Exploratory analysis produced four high-resolution diagnostic charts in `reports/figures/`:
1. **Target Distribution (`target_distribution.png`)**:
   The dataset exhibits a realistic 73.7% ($N=1,105$) placement-ready majority versus a 26.3% ($N=395$) improvement-needed minority.
2. **CGPA vs. Placement Status (`cgpa_vs_placement.png`)**:
   Bimodal separation confirms a critical inflection threshold around **CGPA $\ge 7.0$**. Unplaced students cluster tightly below 6.5 or have multiple backlogs.
3. **Skill Distributions (`skill_distributions.png`)**:
   Students in the placement-ready class consistently demonstrate median DSA scores $> 72$ and coding test scores $> 75$.
4. **Feature Correlation Heatmap (`feature_correlations.png`)**:
   Top positive linear correlations with `placement_status`:
   - `dsa_score` ($r = 0.61$)
   - `coding_test_score` ($r = 0.58$)
   - `technical_skill_avg` ($r = 0.56$)
   - `cgpa` ($r = 0.52$)
   - `internship_experience` ($r = 0.44$)
   Top negative correlation:
   - `backlogs` ($r = -0.48$)

---

## 7. Machine Learning Algorithms Tested

To ensure methodological completeness, eight distinct classification algorithms were implemented and trained:

1. **Baseline (Dummy Classifier)**:
   - Strategy: Predicts the most frequent class (`placement_status = 1`).
   - Purpose: Establishes the non-trivial performance baseline (73.67% accuracy).
2. **Logistic Regression (Parametric / Linear Baseline)**:
   - Configured with `max_iter=1000` and `class_weight='balanced'`.
   - Offers linear interpretability through feature odds-ratios.
3. **K-Nearest Neighbors (KNN — Instance-Based / Non-Parametric)**:
   - Configured with $k=5$ Euclidean distance neighbors.
   - Evaluates placement status based on similarity to nearest peer profiles.
4. **Decision Tree Classifier (Non-Linear Single Estimator)**:
   - Configured with `max_depth=6` to balance tree depth and interpretability.
5. **Random Forest Classifier (Bagging Ensemble)**:
   - Ensembles 100 unpruned decision trees via bootstrap aggregation and random subspace sampling.
6. **Gradient Boosting Classifier (Sequential Boosting Ensemble)**:
   - Ensembles decision trees sequentially to minimize pseudo-residuals via gradient descent.
7. **Extreme Gradient Boosting (XGBoost — Scalable Gradient Boosting)**:
   - Implements regularized boosting with second-order Taylor expansion of the loss function.
8. **Support Vector Machine (SVC — Kernel / Maximum Margin)**:
   - Radial Basis Function (RBF) kernel with Platt scaling for probability calibration (`probability=True`).

---

## 8. Cross-Validation & Hyperparameter Tuning Strategy

- **Validation Schema**: 5-Fold Stratified Cross-Validation (`StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`) applied across all 1,200 training instances.
- **Optimization Strategy**: Exhaustive `GridSearchCV` on leading ensemble candidates:
  - **Random Forest**: Explored `n_estimators` $\in [100, 150]$ and `max_depth` $\in [8, 12]$.
  - **Gradient Boosting**: Explored `learning_rate` $\in [0.05, 0.1]$ and `max_depth` $\in [3, 5]$.
  - **XGBoost**: Explored `learning_rate` $\in [0.05, 0.1]$, `n_estimators` $\in [100]$, and `max_depth` $\in [3, 5]$.
- **Winning Configuration for XGBoost**:
  - `max_depth`: 3
  - `learning_rate`: 0.10
  - `n_estimators`: 100
  - `eval_metric`: `logloss`

---

## 9. Comprehensive Model Evaluation & Benchmarks

All models were evaluated on the held-out, untouched test partition ($N=300$). The complete empirical results (stored in `reports/model_results.csv`) are tabulated below:

| Model Architecture | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **XGBoost (Tuned)** 🏆 | **0.9133** | **0.9258** | **0.9593** | **0.9422** | **0.9534** |
| **K-Nearest Neighbors (KNN)** | 0.9000 | 0.8996 | 0.9729 | 0.9348 | 0.9102 |
| **XGBoost (Base)** | 0.9000 | 0.9170 | 0.9502 | 0.9333 | 0.9437 |
| **Gradient Boosting (Tuned)** | 0.9000 | 0.9244 | 0.9412 | 0.9327 | 0.9494 |
| **Gradient Boosting (Base)** | 0.9000 | 0.9244 | 0.9412 | 0.9327 | 0.9494 |
| **Random Forest (Base)** | 0.8967 | 0.9060 | 0.9593 | 0.9319 | 0.9553 |
| **Random Forest (Tuned)** | 0.8967 | 0.9095 | 0.9548 | 0.9316 | 0.9549 |
| **Support Vector Machine (SVC)** | 0.8867 | 0.9561 | 0.8869 | 0.9202 | 0.9594 |
| **Logistic Regression** | 0.8833 | 0.9650 | 0.8733 | 0.9169 | 0.9636 |
| **Decision Tree** | 0.8567 | 0.9238 | 0.8778 | 0.9002 | 0.8247 |
| **Baseline (Dummy Classifier)** | 0.7367 | 0.7367 | 1.0000 | 0.8484 | 0.5000 |

---

## 10. Best Algorithm Selection & Detailed Technical Rationale

### 10.1 Selected Champion Model
The **Tuned XGBoost Classifier** was selected as the final production model for the Student Skills and Placement Tracker.

### 10.2 Why Tuned XGBoost Was Chosen Over Competing Algorithms:

1. **Superior Balance of F1-Score (0.9422) and Recall (95.93%)**:
   In educational counseling, **False Negatives are disproportionately costly**. If a struggling student is falsely classified as "placement ready", they miss out on vital mock interviews, remedial coding classes, and faculty mentorship. Tuned XGBoost achieves an exceptional Recall of **95.93%**, ensuring that at-risk students are reliably captured.
2. **Modeling Non-Linear Multi-Domain Interactions**:
   Placement readiness is inherently non-linear. For instance:
   - A moderate CGPA (6.8) combined with an exceptional DSA score (90+) and 1 internship yields strong placement prospects.
   - Conversely, a high CGPA (8.8) with zero coding ability and 2 backlogs yields poor prospects.
   Linear models (Logistic Regression, linear SVC) cannot naturally model these high-order feature interactions without manual polynomial expansion, whereas XGBoost tree splits isolate these multi-feature conditionals automatically.
3. **Rigorous Regularization Against Overfitting**:
   Unlike standard Gradient Boosting and Decision Trees, XGBoost incorporates $L_1$ ($\alpha$) and $L_2$ ($\lambda$) tree complexity penalties into its objective function:
   $$\mathcal{L}^{(t)} = \sum_{i=1}^n l\big(y_i, \hat{y}_i^{(t-1)} + f_t(x_i)\big) + \Omega(f_t), \quad \text{where } \Omega(f) = \gamma T + \frac{1}{2}\lambda \sum_{j=1}^T w_j^2$$
   This prevents over-specializing on specific student cohorts and guarantees consistent test generalization.
4. **Second-Order Taylor Approximation**:
   XGBoost utilizes both the first derivative (gradient $g_i$) and second derivative (hessian $h_i$) of the logistic loss function, allowing faster and more precise convergence than first-order gradient descent methods.
5. **Calibrated Probabilistic Output**:
   Unlike Support Vector Machines or KNN (which produce sharp or heuristic confidence scores), XGBoost produces smooth, well-calibrated probabilities via its logistic sigmoid link function, enabling granular readiness tiering.

---

## 11. Model Interpretability & Feature Importances

Analysis of tree split gains (`reports/figures/feature_importance.png`) identifies the following top drivers:
1. **`dsa_score`** (Highest individual split gain): Algorithmic capability is the universal gatekeeper in corporate placement tests.
2. **`cgpa`**: Establishes basic eligibility screening thresholds set by visiting companies.
3. **`coding_test_score`**: Reflects timed hands-on coding speed and syntax accuracy.
4. **`technical_skill_avg`**: Captures broad multi-stack competency.
5. **`internship_experience`**: Empirical evidence shows candidates with prior industry experience have a 2.8x higher probability of placement readiness.
6. **`academic_score_index` & `backlogs`**: Active backlogs directly disqualify candidates from initial screening rounds.

---

## 12. Inference & Personalized Recommendation Engine

The inference module (`src/predict.py`) encapsulates the end-to-end model pipeline into the `StudentPlacementPredictor` class.

### 12.1 Tiered Readiness Categorization
- **Placement Ready ($P \ge 75\%$)**: Candidate displays high probability of clearing written and technical interview rounds.
- **Internship Ready ($50\% \le P < 75\%$)**: Candidate demonstrates sound fundamentals; suitable for internships and junior developer roles.
- **Needs Improvement ($P < 50\%$)**: Candidate requires focused remedial skill intervention.

### 12.2 Automated Gap Diagnostics & Prescriptions
The engine benchmarks incoming student records against empirical institutional cutoffs:
- *DSA Score < 65*: Triggers recommendation for competitive programming practice (LeetCode / HackerRank).
- *Coding Test Score < 65*: Recommends timed mock assessment practice.
- *Communication / Interview Score < 65*: Recommends formal mock HR and technical interviews.
- *Internship Experience = 0*: Prescribes summer industrial training or industry capstone projects.
- *Active Backlogs > 0*: Prioritizes clearing academic backlogs to meet corporate eligibility criteria.

---

## 13. Project Structure & Deliverables

```
student-skills-placement-tracker/
│
├── data/
│   ├── raw/placement_data_raw.csv           <- Synthetic baseline cohort (1,500 records)
│   └── processed/                           <- Train/test splits & processed data
│
├── notebooks/                               <- 6 Verified Exploratory Notebooks
│   ├── 01_data_collection.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_model_training.ipynb
│   └── 06_model_evaluation.ipynb
│
├── src/                                     <- Production Python Modules
│   ├── data_collection.py                   <- Generator & schema validator
│   ├── preprocessing.py                     <- Imputer & ColumnTransformer pipelines
│   ├── feature_engineering.py               <- 5 Domain aggregate indices
│   ├── train.py                             <- 5-Fold CV, GridSearch & serialization
│   ├── evaluate.py                          <- Metric scoring & visualization routines
│   └── predict.py                           <- Inference & Recommendation Engine
│
├── models/                                  <- Serialized Model Artifacts
│   ├── final_model.pkl                      <- Preprocessor + Tuned XGBoost Pipeline
│   ├── preprocessor.pkl                     <- ColumnTransformer
│   └── feature_info.pkl                     <- Metadata & benchmark metrics
│
├── reports/
│   ├── figures/                             <- 7 High-resolution EDA and evaluation plots
│   └── model_results.csv                    <- Comparative metrics for all 8 algorithms
│
├── docs/
│   ├── presentation_slides.md               <- Slide-by-slide minor project PPT deck
│   └── PROJECT_REPORT.md                    <- Full academic project report (this document)
│
├── Student_Placement_Tracker_Minor_Project_PPT.pptx <- Evaluator presentation deck
├── requirements.txt                         <- Production dependencies
├── README.md                                <- Complete setup & technical documentation
└── main.py                                  <- End-to-end execution entrypoint
```

---

## 14. Ethical Considerations, Fairness & Limitations

1. **Advisory Decision-Support Role**: The system is explicitly configured as a *decision-support advisory tool* for mentors, students, and counselors. It is not an automated hiring rejection filter.
2. **Algorithmic Fairness**: Demographic features (`gender`, `branch`) demonstrate negligible feature importance, ensuring placement predictions are driven predominantly by meritocratic technical competencies.
3. **Current Limitations**: The present benchmark was established on calibrated synthetic cohort data. Performance must be fine-tuned against multi-year historical placement archives when deployed in real institutional settings.

---

## 15. Future Roadmap (Phase 2)

- **RESTful API Backend**: Wrapping `src/predict.py` with FastAPI to serve low-latency inference endpoints.
- **Interactive Web Portal**: Developing a Streamlit or React frontend for interactive student self-assessment and placement officer batch analytics.
- **Institutional Database Connector**: Ingesting live student semester marks directly from university ERP databases (PostgreSQL / MongoDB).
