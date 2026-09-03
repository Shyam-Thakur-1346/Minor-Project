# Student Skills and Placement Tracker — Minor Project Presentation Slides

> **Presentation File**: `Student_Placement_Tracker_Minor_Project_PPT.pptx` (Saved in project root)
> **Target Audience**: College Minor Project Evaluation Panel
> **Presenter**: Student Team
> **Project Scope**: Phase 1 — Machine Learning Core & Prediction Engine (100% Completed)

---

## Slide 1: Title Slide
- **Title**: Student Skills & Placement Tracker
- **Subtitle**: Machine Learning-Based Employability Estimation & Personalised Skill Gap Analysis
- **Category**: College Minor Project Presentation (Phase 1: ML Core Completed)

---

## Slide 2: Problem Statement & Industry Context
### Traditional Evaluation Failures
- **Over-Reliance on CGPA**: Ignores practical programming capabilities, DSA problem-solving, and soft skills.
- **Reactive Counseling**: Placement cells identify unprepared students AFTER they fail campus interviews.
- **One-Size-Fits-All Approach**: Colleges lack personalized skill recommendations tailored to individual student gaps.
- **No Quantitative Employability Index**: Difficulty in measuring student readiness across technical, soft, and profile domains.

### Our Proposed ML Solution
- **Data-Driven Employability Estimation**: Evaluates 30 multi-dimensional student academic, technical, soft skill, and profile metrics.
- **Probabilistic Readiness Gauge**: Outputs calibrated placement probabilities (0% - 100%) and readiness tiers.
- **Early Risk Detection**: Identifies at-risk students prior to placement drives for targeted intervention.
- **Actionable Skill Gap Roadmap**: Recommends specific technical/soft skill improvements based on institutional benchmarks.

---

## Slide 3: Motivation & Stakeholder Benefits
- **For Students**: Provides an objective Placement Readiness Score (0-100%), identifies missing skills, offers clear roadmap.
- **For Faculty / Placement Cell**: Automated batch tracking across departments, early risk detection, improves placement statistics.
- **For Recruiters & College**: Skill matching with company job profiles, boosts institutional reputation.

---

## Slide 4: Project Objectives & Scope Breakdown
- **Phase 1: ML Core (COMPLETED 100%)**:
  - Data Collection & Synthetic Generator ($N=1,500$, `seed=42`).
  - Preprocessing & Data Cleaning Pipeline (`ColumnTransformer`, `StandardScaler`, `OneHotEncoder`).
  - Feature Engineering (5 Domain Aggregate Indices).
  - 8 ML Models Trained & Evaluated with 5-Fold Stratified CV.
  - Hyperparameter Tuning via `GridSearchCV`.
  - Final Model Pipeline Serialization (`models/final_model.pkl`).
- **Phase 2: App & Web Integration (UPCOMING)**:
  - Backend REST API Development (FastAPI / Flask).
  - Student & Admin Dashboard (React / Streamlit).
  - Institutional Database (PostgreSQL / MongoDB).

---

## Slide 5: Dataset Design & Feature Schema (30 Features)
- **Academic Features**: CGPA, Backlogs, Attendance Percentage, Branch, Degree, Semester.
- **Technical Skills**: Programming, DSA, SQL, Web Dev, ML, Cloud, Aptitude, Coding Test Score.
- **Soft Skills**: Communication, Leadership, Teamwork, Mock Interview Score.
- **Profile Features**: Projects, Project Quality, Certifications, Internship Experience, Internship Count, Hackathons, GitHub Contributions, Resume Score.
- **Target Leakage Protection**: Excluded post-placement features (e.g. salary, company offer).

---

## Slide 6: Data Cleaning & Preprocessing Pipeline
1. **Deduplication**: 5 duplicate rows dropped.
2. **Range Validation**: Corrected invalid CGPA (>10), attendance (>100%), and negative scores to NaN.
3. **Imputation & Scaling**: Median Imputer + `StandardScaler` for numeric features; Most-Frequent Imputer + `OneHotEncoder` for categorical features.
4. **Data Leakage Isolation**: Fit preprocessor strictly on training data (80/20 Stratified Split).

---

## Slide 7: Feature Engineering & Domain Aggregate Indices
- `technical_skill_avg`: Aggregate score across 6 technical domains.
- `soft_skill_avg`: Aggregate score across soft skills & mock interview.
- `academic_score_index`: $(CGPA \times 7.0) + (\text{Attendance} \times 0.3) - (\text{Backlogs} \times 10.0)$.
- `experience_score`: Composite profile score (projects, quality, internships, hackathons).
- `overall_readiness_index`: Weighted domain index ($30\%$ Academic, $35\%$ Technical, $20\%$ Soft, $15\%$ Experience).

---

## Slide 8: Exploratory Data Analysis (EDA) Insights
- **Target Distribution**: $73.7\%$ Placement Ready, $26.3\%$ Needs Improvement.
- **CGPA Threshold**: Distinct separation at CGPA $\ge 7.0$ and 0 backlogs.
- **Technical Skill Impact**: DSA score and Automated Coding test score have highest feature correlation with placement readiness.
- **Internships**: Students with $\ge 1$ internship show $2.8\times$ higher placement readiness probability.

---

## Slide 9: Machine Learning Methodology & Algorithms Tested
- **8 Candidate Algorithms**: Baseline (Dummy), Logistic Regression, KNN, Decision Tree, Random Forest, Gradient Boosting, XGBoost, Support Vector Machine (SVC).
- **Validation**: 5-Fold Stratified Cross-Validation (`StratifiedKFold(n_splits=5)`).
- **Tuning**: `GridSearchCV` on Random Forest, Gradient Boosting, and XGBoost.

---

## Slide 10: Experimental Results & Model Comparison

| Rank | Model Name | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 🥇 | **XGBoost (Tuned)** | **0.9133** | **0.9258** | **0.9593** | **0.9422** | **0.9534** |
| 🥈 | **K-Nearest Neighbors** | 0.9000 | 0.8996 | 0.9729 | 0.9348 | 0.9102 |
| 🥉 | **XGBoost (Base)** | 0.9000 | 0.9170 | 0.9502 | 0.9333 | 0.9437 |
| 4 | **Gradient Boosting (Tuned)** | 0.9000 | 0.9244 | 0.9412 | 0.9327 | 0.9494 |
| 5 | **Gradient Boosting (Base)** | 0.9000 | 0.9244 | 0.9412 | 0.9327 | 0.9494 |
| 6 | **Random Forest (Base)** | 0.8967 | 0.9060 | 0.9593 | 0.9319 | 0.9553 |
| 7 | **Random Forest (Tuned)** | 0.8967 | 0.9095 | 0.9548 | 0.9316 | 0.9549 |
| 8 | **Support Vector Machine** | 0.8867 | 0.9561 | 0.8869 | 0.9202 | 0.9594 |
| 9 | **Logistic Regression** | 0.8833 | 0.9650 | 0.8733 | 0.9169 | 0.9636 |
| 10 | **Decision Tree** | 0.8567 | 0.9238 | 0.8778 | 0.9002 | 0.8247 |
| 11 | **Baseline (Dummy)** | 0.7367 | 0.7367 | 1.0000 | 0.8484 | 0.5000 |

---

## Slide 11: Best Model Selection & Interpretability
- **Model Selected**: Tuned XGBoost (`n_estimators=100`, `learning_rate=0.1`, `max_depth=3`).
- **Metric Priority Rationale**: Prioritized Recall ($95.93\%$) and F1-Score ($0.9422$) to minimize False Negatives.
- **Top Feature Drivers**: DSA Score, CGPA, Coding Test Score, Technical Skill Average, Internship Experience.

---

## Slide 12: Inference & Recommendation Engine
- `StudentPlacementPredictor` class loads `final_model.pkl`.
- Calculates Placement Readiness Probability ($0\% - 100\%$).
- Classifies into Category Tiers (Placement Ready, Internship Ready, Needs Improvement).
- Generates rule and benchmark-derived **Actionable Areas for Improvement**.

---

## Slide 13: Work Completed (Phase 1 Deliverables)
- 100% Machine Learning Core completed and verified.
- 6 Jupyter Notebooks created (`01_data_collection.ipynb` to `06_model_evaluation.ipynb`).
- Serialized artifacts saved in `models/`: `final_model.pkl`, `preprocessor.pkl`, `feature_info.pkl`.
- 7 visual figures saved in `reports/figures/`.

---

## Slide 14: Future Roadmap (Phase 2 Integration)
- **Backend**: REST API using FastAPI / Flask.
- **Frontend**: Interactive React / Streamlit dashboard.
- **Database**: PostgreSQL / MongoDB student progress tracking.
- **Calibration**: Real institutional student placement data integration.

---

## Slide 15: Conclusion & Q&A
- Summary highlights & panel discussion Q&A.
