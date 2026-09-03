"""
PowerPoint Presentation Generator Script for Minor Project Panel
Project: Student Skills and Placement Tracker
"""

import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_presentation(output_pptx="C:/Users/shyam/student-skills-placement-tracker/Student_Placement_Tracker_Minor_Project_PPT.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    # Theme colors
    PRIMARY = RGBColor(24, 43, 73)      # Dark Navy
    ACCENT = RGBColor(0, 150, 136)      # Teal / Cyan Accent
    TEXT_DARK = RGBColor(40, 40, 40)   # Dark Gray Body Text
    WHITE = RGBColor(255, 255, 255)     # White
    BG_LIGHT = RGBColor(245, 247, 250)  # Light Card Gray
    MUTED = RGBColor(100, 110, 120)    # Subtitle Gray

    blank_slide_layout = prs.slide_layouts[6]
    
    def add_header(slide, title_text, category_text="STUDENT SKILLS & PLACEMENT TRACKER"):
        # Header title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.9))
        tf = title_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p0 = tf.paragraphs[0]
        p0.text = category_text.upper()
        p0.font.size = Pt(11)
        p0.font.bold = True
        p0.font.color.rgb = ACCENT
        
        p1 = tf.add_paragraph()
        p1.text = title_text
        p1.font.size = Pt(24)
        p1.font.bold = True
        p1.font.color.rgb = PRIMARY

    # -------------------------------------------------------------
    # SLIDE 1: Title Slide
    # -------------------------------------------------------------
    slide1 = prs.slides.add_slide(blank_slide_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = PRIMARY
    bg1.line.color.rgb = PRIMARY
    
    t_box = slide1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(4.0))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    
    p = tf1.paragraphs[0]
    p.text = "MINOR PROJECT PRESENTATION"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT
    
    p = tf1.add_paragraph()
    p.text = "Student Skills & Placement Tracker"
    p.font.size = Pt(38)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    p = tf1.add_paragraph()
    p.text = "Machine Learning-Based Employability Estimation & Personalised Skill Gap Analysis"
    p.font.size = Pt(20)
    p.font.color.rgb = RGBColor(200, 220, 245)
    
    p = tf1.add_paragraph()
    p.text = "\nPhase 1: Complete Machine Learning Pipeline & Core Model Implementation"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT

    # -------------------------------------------------------------
    # SLIDE 2: Problem Statement
    # -------------------------------------------------------------
    slide2 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide2, "Problem Statement & Industry Context")
    
    # Left Card: Traditional Limitations
    c1 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2))
    c1.fill.solid()
    c1.fill.fore_color.rgb = BG_LIGHT
    c1.line.color.rgb = RGBColor(220, 225, 230)
    
    tf = c1.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "Traditional Evaluation Failures"
    p.font.bold = True
    p.font.size = Pt(18)
    p.font.color.rgb = PRIMARY
    
    bullets1 = [
        "Over-Reliance on CGPA: Ignores practical programming capabilities, DSA problem-solving, and soft skills.",
        "Reactive Counseling: Placement cells identify unprepared students AFTER they fail campus interviews.",
        "One-Size-Fits-All Approach: Colleges lack personalized skill recommendations tailored to individual student gaps.",
        "No Quantitative Employability Index: Difficulty in measuring student readiness across technical, soft, and profile domains."
    ]
    for b in bullets1:
        p = tf.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_DARK
        
    # Right Card: The Solution Needed
    c2 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.6), Inches(5.2))
    c2.fill.solid()
    c2.fill.fore_color.rgb = RGBColor(235, 245, 250)
    c2.line.color.rgb = ACCENT
    
    tf = c2.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "Our Proposed ML Solution"
    p.font.bold = True
    p.font.size = Pt(18)
    p.font.color.rgb = PRIMARY
    
    bullets2 = [
        "Data-Driven Employability Estimation: Evaluates 30 multi-dimensional student academic, technical, soft skill, and profile metrics.",
        "Probabilistic Readiness Gauge: Outputs calibrated placement probabilities (0% - 100%) and readiness tiers.",
        "Early Risk Detection: Identifies at-risk students prior to placement drives for targeted intervention.",
        "Actionable Skill Gap Roadmap: Recommends specific technical/soft skill improvements based on institutional benchmarks."
    ]
    for b in bullets2:
        p = tf.add_paragraph()
        p.text = "✔ " + b
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_DARK

    # -------------------------------------------------------------
    # SLIDE 3: Motivation & Key Benefits
    # -------------------------------------------------------------
    slide3 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide3, "Motivation & Project Stakeholder Benefits")
    
    col_width = Inches(3.6)
    gap = Inches(0.4)
    left_start = Inches(0.8)
    
    cards_data = [
        ("For Students", ACCENT, [
            "Provides an objective Placement Readiness Score (0-100%).",
            "Identifies specific missing skills (e.g., DSA score < 65, missing internships).",
            "Offers clear roadmap for placement & internship preparation."
        ]),
        ("For Placement Cell / Faculty", PRIMARY, [
            "Automated batch tracking across academic departments.",
            "Identifies at-risk students early for remedial bootcamps.",
            "Improves overall college campus placement conversion rate."
        ]),
        ("For Recruiters & Institution", RGBColor(120, 80, 200), [
            "Ensures candidate skill matching with company job profiles.",
            "Boosts college institutional reputation and recruitment statistics.",
            "Enables data-driven curriculum enhancements."
        ])
    ]
    
    for idx, (title, color, items) in enumerate(cards_data):
        pos_left = left_start + idx * (col_width + gap)
        card = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, pos_left, Inches(1.6), col_width, Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = BG_LIGHT
        card.line.color.rgb = color
        card.line.width = Pt(2)
        
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.25)
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.bold = True
        p.font.size = Pt(18)
        p.font.color.rgb = color
        
        for item in items:
            p = tf.add_paragraph()
            p.text = "• " + item
            p.font.size = Pt(13)
            p.font.color.rgb = TEXT_DARK

    # -------------------------------------------------------------
    # SLIDE 4: Project Objectives & Scope
    # -------------------------------------------------------------
    slide4 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide4, "Project Objectives & Scope Breakdown")
    
    # Left Card: Completed ML Core
    c1 = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2))
    c1.fill.solid()
    c1.fill.fore_color.rgb = RGBColor(240, 250, 245)
    c1.line.color.rgb = RGBColor(40, 160, 100)
    
    tf = c1.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "Phase 1: ML Core (COMPLETED 100%)"
    p.font.bold = True
    p.font.size = Pt(17)
    p.font.color.rgb = RGBColor(20, 120, 70)
    
    done_items = [
        "Problem Definition & ML Formulation (Binary Classification + Probability).",
        "Synthetic Data Generation (N=1,500, fixed seed=42).",
        "Data Cleaning & Preprocessing (Imputation, Scaling, OneHotEncoding).",
        "EDA & Visualizations (Target dist., CGPA boxplots, correlation heatmap).",
        "Feature Engineering (5 Aggregate Indices).",
        "Trained & Evaluated 8 ML Models with 5-Fold Stratified CV.",
        "Hyperparameter Tuning via GridSearchCV.",
        "Serialized Final Pipeline (.pkl) & Prediction Engine."
    ]
    for d in done_items:
        p = tf.add_paragraph()
        p.text = "✔ " + d
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK

    # Right Card: Future Scope
    c2 = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.6), Inches(5.2))
    c2.fill.solid()
    c2.fill.fore_color.rgb = RGBColor(255, 248, 240)
    c2.line.color.rgb = RGBColor(230, 140, 40)
    
    tf = c2.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "Phase 2: App & Web Integration (UPCOMING)"
    p.font.bold = True
    p.font.size = Pt(17)
    p.font.color.rgb = RGBColor(180, 90, 10)
    
    future_items = [
        "Backend REST API Development (FastAPI / Flask framework).",
        "Student & Admin Frontend Dashboard (React / Streamlit).",
        "Institutional Database Integration (PostgreSQL / MongoDB).",
        "Real College Placement Dataset Fine-Tuning.",
        "Historical Student Readiness Tracking across semesters.",
        "Automated Resume Parsing & ATS Scoring Module."
    ]
    for f in future_items:
        p = tf.add_paragraph()
        p.text = "⏳ " + f
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_DARK

    # -------------------------------------------------------------
    # SLIDE 5: Dataset & Feature Schema
    # -------------------------------------------------------------
    slide5 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide5, "Dataset Design & Feature Schema (30 Features)")
    
    cat_boxes = [
        ("Academic Features (5)", PRIMARY, ["cgpa (0-10)", "backlogs (count)", "attendance_percentage", "branch (CS, IT, ECE, etc.)", "degree & semester"]),
        ("Technical Skills (8)", ACCENT, ["programming_score", "dsa_score", "sql_score", "web_dev_score", "ml_score", "cloud_score", "aptitude_score", "coding_test_score"]),
        ("Soft Skills (4)", RGBColor(120, 80, 200), ["communication_score", "leadership_score", "teamwork_score", "interview_score"]),
        ("Profile Features (8)", RGBColor(210, 100, 30), ["number_of_projects", "project_quality_score", "certifications_count", "internship_experience (0/1)", "internship_count", "hackathons_attended", "github_contributions", "resume_score"])
    ]
    
    width = Inches(5.6)
    height = Inches(2.4)
    coords = [(Inches(0.8), Inches(1.6)), (Inches(6.8), Inches(1.6)), (Inches(0.8), Inches(4.3)), (Inches(6.8), Inches(4.3))]
    
    for idx, (title, color, items) in enumerate(cat_boxes):
        pos_x, pos_y = coords[idx]
        card = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, pos_x, pos_y, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = BG_LIGHT
        card.line.color.rgb = color
        
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.2)
        p = tf.paragraphs[0]
        p.text = title
        p.font.bold = True
        p.font.size = Pt(15)
        p.font.color.rgb = color
        
        p = tf.add_paragraph()
        p.text = "Features: " + ", ".join(items)
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_DARK

    # -------------------------------------------------------------
    # SLIDE 6: Data Cleaning & Preprocessing Pipeline
    # -------------------------------------------------------------
    slide6 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide6, "Data Cleaning & Leakage-Free Preprocessing")
    
    box = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    box.fill.solid()
    box.fill.fore_color.rgb = BG_LIGHT
    box.line.color.rgb = RGBColor(200, 210, 220)
    
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.3)
    
    p = tf.paragraphs[0]
    p.text = "Key Data Pipeline Steps (src/preprocessing.py)"
    p.font.bold = True
    p.font.size = Pt(17)
    p.font.color.rgb = PRIMARY
    
    steps = [
        ("1. Data Cleaning & Range Validation", "Identified and removed 5 duplicate rows. Cleaned invalid out-of-range values (e.g. CGPA > 10, attendance > 100%, negative scores) by setting them to NaN for robust median imputation."),
        ("2. Categorical Standardisation", "Standardised string fields ('gender', 'branch') by stripping whitespace and title-casing values."),
        ("3. Stratified Train-Test Split", "Divided dataset into 80% Training (1,200 records) and 20% Testing (300 records) using stratified sampling to preserve target class proportions."),
        ("4. ColumnTransformer Pipeline", "Built scikit-learn ColumnTransformer with median imputation + StandardScaler for numerical features and most-frequent imputation + OneHotEncoder for categorical features."),
        ("5. Data Leakage Prevention", "Fit all preprocessing scalers and encoders ONLY on training data. Strict exclusion of post-placement features (e.g. salary, company offer).")
    ]
    for title, desc in steps:
        p = tf.add_paragraph()
        p.text = "• " + title + ": "
        p.font.bold = True
        p.font.size = Pt(13)
        p.font.color.rgb = ACCENT
        
        p_desc = tf.add_paragraph()
        p_desc.text = "   " + desc
        p_desc.font.size = Pt(12)
        p_desc.font.color.rgb = TEXT_DARK

    # -------------------------------------------------------------
    # SLIDE 7: Feature Engineering & Domain Readiness Indices
    # -------------------------------------------------------------
    slide7 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide7, "Feature Engineering: Domain Aggregate Indices")
    
    fe_box = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    fe_box.fill.solid()
    fe_box.fill.fore_color.rgb = BG_LIGHT
    fe_box.line.color.rgb = RGBColor(200, 210, 220)
    
    tf = fe_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.3)
    
    p = tf.paragraphs[0]
    p.text = "Engineered Composite Features (src/feature_engineering.py)"
    p.font.bold = True
    p.font.size = Pt(17)
    p.font.color.rgb = PRIMARY
    
    fe_features = [
        ("technical_skill_avg", "Average score across 6 technical domains (Programming, DSA, SQL, Web Dev, ML, Cloud)."),
        ("soft_skill_avg", "Average score across Communication, Leadership, Teamwork, and Mock Interview scores."),
        ("academic_score_index", "Composite academic score (0-100 scale): (CGPA * 7.0) + (Attendance * 0.3) - (Backlogs * 10.0)"),
        ("experience_score", "Profile score combining portfolio projects, project quality, internships, hackathons, and certifications."),
        ("overall_readiness_index", "Domain-weighted benchmark index: 30% Academic + 35% Technical + 20% Soft Skills + 15% Experience.")
    ]
    for feat, explanation in fe_features:
        p = tf.add_paragraph()
        p.text = "🔹 " + feat + ": "
        p.font.bold = True
        p.font.size = Pt(13)
        p.font.color.rgb = PRIMARY
        
        p_exp = tf.add_paragraph()
        p_exp.text = "    " + explanation
        p_exp.font.size = Pt(12)
        p_exp.font.color.rgb = TEXT_DARK

    # -------------------------------------------------------------
    # SLIDE 8: Exploratory Data Analysis (EDA)
    # -------------------------------------------------------------
    slide8 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide8, "Exploratory Data Analysis (EDA) Insights")
    
    eda_cards = [
        ("Target Distribution", "• 73.7% Placement Ready (Class 1)\n• 26.3% Needs Improvement (Class 0)\n• Represents realistic campus placement baseline distribution."),
        ("CGPA & Academic Separation", "• Clear threshold separation around 7.0 CGPA.\n• Students with > 7.5 CGPA and 0 backlogs show significantly higher placement readiness."),
        ("Technical Skill Impact", "• DSA score and Automated Coding test score have highest feature correlation with placement readiness.\n• Programming score > 65 is key threshold."),
        ("Profile & Internship Exposure", "• Students with at least 1 industrial internship have 2.8x higher probability of placement readiness.")
    ]
    for idx, (title, text) in enumerate(eda_cards):
        pos_x = Inches(0.8) if idx % 2 == 0 else Inches(6.8)
        pos_y = Inches(1.6) if idx < 2 else Inches(4.3)
        card = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, pos_x, pos_y, Inches(5.6), Inches(2.4))
        card.fill.solid()
        card.fill.fore_color.rgb = BG_LIGHT
        card.line.color.rgb = ACCENT
        
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.2)
        p = tf.paragraphs[0]
        p.text = title
        p.font.bold = True
        p.font.size = Pt(15)
        p.font.color.rgb = PRIMARY
        
        p = tf.add_paragraph()
        p.text = text
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK

    # -------------------------------------------------------------
    # SLIDE 9: ML Methodology & Models Tested
    # -------------------------------------------------------------
    slide9 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide9, "Machine Learning Methodology & Algorithms Tested")
    
    m_box = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    m_box.fill.solid()
    m_box.fill.fore_color.rgb = BG_LIGHT
    m_box.line.color.rgb = RGBColor(200, 210, 220)
    
    tf = m_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.3)
    
    p = tf.paragraphs[0]
    p.text = "Evaluation Strategy & Candidate Models"
    p.font.bold = True
    p.font.size = Pt(17)
    p.font.color.rgb = PRIMARY
    
    bullets = [
        "Baseline Model: Dummy Classifier (predicts most frequent class, baseline accuracy = 73.67%).",
        "Tested Algorithms (8 Models): Baseline, Logistic Regression, K-Nearest Neighbors, Decision Tree, Random Forest, Gradient Boosting, XGBoost, Support Vector Machine.",
        "5-Fold Stratified Cross Validation: Ensures model robustness across data folds without class distribution distortion.",
        "Hyperparameter Optimization: Applied GridSearchCV on top candidate models (Random Forest, Gradient Boosting, XGBoost).",
        "Evaluation Metrics Evaluated: Accuracy, Precision, Recall, F1-Score, ROC-AUC, and Cross-Validation F1 mean & std."
    ]
    for b in bullets:
        p = tf.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_DARK

    # -------------------------------------------------------------
    # SLIDE 10: Model Comparison & Experimental Results
    # -------------------------------------------------------------
    slide10 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide10, "Experimental Results & Model Comparison")
    
    # Table layout
    rows, cols = 12, 6
    table_shape = slide10.shapes.add_table(rows, cols, Inches(0.8), Inches(1.5), Inches(11.7), Inches(5.2))
    table = table_shape.table
    
    headers = ["Model", "Accuracy", "Precision", "Recall", "F1 Score", "ROC-AUC"]
    for col_idx, h in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = PRIMARY
        for p in cell.text_frame.paragraphs:
            p.font.bold = True
            p.font.size = Pt(12)
            p.font.color.rgb = WHITE
            p.alignment = PP_ALIGN.CENTER
            
    data = [
        ["XGBoost (Tuned) 🏆", "0.9133", "0.9258", "0.9593", "0.9422", "0.9534"],
        ["K-Nearest Neighbors", "0.9000", "0.8996", "0.9729", "0.9348", "0.9102"],
        ["XGBoost (Base)", "0.9000", "0.9170", "0.9502", "0.9333", "0.9437"],
        ["Gradient Boosting (Tuned)", "0.9000", "0.9244", "0.9412", "0.9327", "0.9494"],
        ["Gradient Boosting (Base)", "0.9000", "0.9244", "0.9412", "0.9327", "0.9494"],
        ["Random Forest (Base)", "0.8967", "0.9060", "0.9593", "0.9319", "0.9553"],
        ["Random Forest (Tuned)", "0.8967", "0.9095", "0.9548", "0.9316", "0.9549"],
        ["Support Vector Machine", "0.8867", "0.9561", "0.8869", "0.9202", "0.9594"],
        ["Logistic Regression", "0.8833", "0.9650", "0.8733", "0.9169", "0.9636"],
        ["Decision Tree", "0.8567", "0.9238", "0.8778", "0.9002", "0.8247"],
        ["Baseline (Dummy)", "0.7367", "0.7367", "1.0000", "0.8484", "0.5000"]
    ]
    
    for row_idx, row_data in enumerate(data, start=1):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.text = text
            if row_idx == 1:
                cell.fill.solid()
                cell.fill.fore_color.rgb = RGBColor(230, 245, 240)
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(11)
                p.alignment = PP_ALIGN.CENTER if col_idx > 0 else PP_ALIGN.LEFT
                if row_idx == 1:
                    p.font.bold = True
                    p.font.color.rgb = RGBColor(0, 120, 90)

    # -------------------------------------------------------------
    # SLIDE 11: Best Model Selection & Feature Importance
    # -------------------------------------------------------------
    slide11 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide11, "Best Model Selection & Interpretability")
    
    c1 = slide11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2))
    c1.fill.solid()
    c1.fill.fore_color.rgb = BG_LIGHT
    c1.line.color.rgb = ACCENT
    
    tf = c1.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "Selected Model: Tuned XGBoost"
    p.font.bold = True
    p.font.size = Pt(17)
    p.font.color.rgb = PRIMARY
    
    reasons = [
        "Highest F1-Score: Achieved 0.9422 F1-score on untouched test set.",
        "High Recall (0.9593): Crucial for catching at-risk students who need improvement.",
        "Strong Generalisation (ROC-AUC 0.9534): High discrimination stability across decision thresholds.",
        "Hyperparameters: n_estimators=100, learning_rate=0.1, max_depth=3."
    ]
    for r in reasons:
        p = tf.add_paragraph()
        p.text = "✔ " + r
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_DARK

    c2 = slide11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.6), Inches(5.2))
    c2.fill.solid()
    c2.fill.fore_color.rgb = BG_LIGHT
    c2.line.color.rgb = PRIMARY
    
    tf = c2.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "Top Feature Importance Drivers"
    p.font.bold = True
    p.font.size = Pt(17)
    p.font.color.rgb = PRIMARY
    
    drivers = [
        "1. DSA Score (Data Structures & Algorithms proficiency)",
        "2. CGPA (Academic performance baseline)",
        "3. Coding Test Score (Automated evaluation score)",
        "4. Technical Skill Average (Composite domain score)",
        "5. Internship Experience (Industrial exposure)",
        "6. Communication Score (Soft skill readiness)"
    ]
    for d in drivers:
        p = tf.add_paragraph()
        p.text = "⭐ " + d
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_DARK

    # -------------------------------------------------------------
    # SLIDE 12: Inference & Recommendation Engine
    # -------------------------------------------------------------
    slide12 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide12, "Inference & Personalised Skill Gap Recommendation")
    
    box = slide12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    box.fill.solid()
    box.fill.fore_color.rgb = BG_LIGHT
    box.line.color.rgb = ACCENT
    
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.3)
    
    p = tf.paragraphs[0]
    p.text = "Prediction Output Structure (src/predict.py)"
    p.font.bold = True
    p.font.size = Pt(17)
    p.font.color.rgb = PRIMARY
    
    inf_items = [
        ("1. Placement Readiness Probability", "Calibrated confidence score (e.g. 99.8% Placement Ready vs 1.9% Needs Improvement)."),
        ("2. Categorical Readiness Tier", "Tiers: Placement Ready (P >= 75%), Internship Ready (50% <= P < 75%), Needs Improvement (P < 50%)."),
        ("3. Domain Score Breakdown", "Calculates individual student Academic Index, Technical Average, Soft Skill Average, and Experience Score."),
        ("4. Personalised Skill Gap Analysis", "Identifies specific failing metrics against institutional benchmark standards (e.g. DSA score < 65, active backlogs > 0, missing internship experience).")
    ]
    for title, desc in inf_items:
        p = tf.add_paragraph()
        p.text = title + ": "
        p.font.bold = True
        p.font.size = Pt(13)
        p.font.color.rgb = PRIMARY
        
        p_desc = tf.add_paragraph()
        p_desc.text = "   " + desc
        p_desc.font.size = Pt(12)
        p_desc.font.color.rgb = TEXT_DARK

    # -------------------------------------------------------------
    # SLIDE 13: Work Completed (Current Milestone)
    # -------------------------------------------------------------
    slide13 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide13, "Work Completed (Phase 1 Deliverables)")
    
    box = slide13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    box.fill.solid()
    box.fill.fore_color.rgb = RGBColor(240, 250, 245)
    box.line.color.rgb = RGBColor(40, 160, 100)
    
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.3)
    
    p = tf.paragraphs[0]
    p.text = "100% Machine Learning Core Completed & Verified"
    p.font.bold = True
    p.font.size = Pt(17)
    p.font.color.rgb = RGBColor(20, 120, 70)
    
    delivs = [
        "Dataset & Generator: 1,500 student raw dataset created and saved to data/raw/placement_data_raw.csv.",
        "6 Jupyter Notebooks: Created 01_data_collection.ipynb through 06_model_evaluation.ipynb.",
        "Source Code Architecture: Created modular Python files inside src/ (data_collection, preprocessing, feature_engineering, train, evaluate, predict).",
        "Serialized Model Artifacts: Saved final_model.pkl, preprocessor.pkl, and feature_info.pkl inside models/.",
        "Visual Evaluation Reports: Generated 7 high-resolution charts in reports/figures/ and saved model_results.csv.",
        "Master Verification: Executed main.py from scratch successfully with zero errors."
    ]
    for d in delivs:
        p = tf.add_paragraph()
        p.text = "✔ " + d
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_DARK

    # -------------------------------------------------------------
    # SLIDE 14: Future Work & Roadmap
    # -------------------------------------------------------------
    slide14 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide14, "Future Work & Integration Roadmap (Phase 2)")
    
    fw_box = slide14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    fw_box.fill.solid()
    fw_box.fill.fore_color.rgb = BG_LIGHT
    fw_box.line.color.rgb = PRIMARY
    
    tf = fw_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.3)
    
    p = tf.paragraphs[0]
    p.text = "Next Phase: Full-Stack Web Application Integration"
    p.font.bold = True
    p.font.size = Pt(17)
    p.font.color.rgb = PRIMARY
    
    steps_future = [
        ("1. Backend REST API Layer", "Develop FastAPI or Flask web service exposing POST /api/predict-readiness endpoint."),
        ("2. Frontend Web Interface", "Build interactive React / Streamlit dashboard featuring student input forms, probability gauge meters, and skill gap checklists."),
        ("3. Institutional Database Integration", "Connect PostgreSQL / MongoDB database to store multi-semester student progress data."),
        ("4. Real College Data Calibration", "Ingest real institutional placement records for production fine-tuning.")
    ]
    for title, desc in steps_future:
        p = tf.add_paragraph()
        p.text = title + ": "
        p.font.bold = True
        p.font.size = Pt(13)
        p.font.color.rgb = ACCENT
        
        p_desc = tf.add_paragraph()
        p_desc.text = "   " + desc
        p_desc.font.size = Pt(12)
        p_desc.font.color.rgb = TEXT_DARK

    # -------------------------------------------------------------
    # SLIDE 15: Conclusion & Q&A
    # -------------------------------------------------------------
    slide15 = prs.slides.add_slide(blank_slide_layout)
    bg15 = slide15.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg15.fill.solid()
    bg15.fill.fore_color.rgb = PRIMARY
    bg15.line.color.rgb = PRIMARY
    
    t_box = slide15.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(11.3), Inches(3.5))
    tf15 = t_box.text_frame
    tf15.word_wrap = True
    
    p = tf15.paragraphs[0]
    p.text = "THANK YOU!"
    p.font.size = Pt(44)
    p.font.bold = True
    p.alignment = PP_ALIGN.CENTER
    p.font.color.rgb = WHITE
    
    p = tf15.add_paragraph()
    p.text = "Student Skills and Placement Tracker — Minor Project Presentation"
    p.font.size = Pt(20)
    p.alignment = PP_ALIGN.CENTER
    p.font.color.rgb = RGBColor(200, 220, 245)
    
    p = tf15.add_paragraph()
    p.text = "\nQuestions & Evaluation Panel Discussion"
    p.font.size = Pt(22)
    p.font.bold = True
    p.alignment = PP_ALIGN.CENTER
    p.font.color.rgb = ACCENT
    
    prs.save(output_pptx)
    print(f"PowerPoint Presentation successfully created and saved to {output_pptx}")

if __name__ == "__main__":
    create_presentation()
