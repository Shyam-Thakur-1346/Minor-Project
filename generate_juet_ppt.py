"""
PowerPoint Presentation Generator Script - Lean, Simple, Easy-to-Read Edition
Project: Student Skills and Internship Tracker
Institution: Jaypee University of Engineering & Technology, Guna
Author: Shyam Thakur (Enrollment No: 241B258)

Key Design Principles for this Version:
1. Minimal text, high readability, zero dense jargon.
2. Short, punchy bullet points (scannable in seconds).
3. Clear problem statement and objective.
4. 100% compliant with JUET official format (Presentation format (1).pdf) and PPT_Instructions.pdf.
"""

import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    # 4:3 Standard Aspect Ratio (10 x 7.5 inches)
    prs.slide_width = Inches(10.0)
    prs.slide_height = Inches(7.5)
    
    # -------------------------------------------------------------
    # JUET Official Color Palette & Typography
    # -------------------------------------------------------------
    ORANGE = RGBColor(221, 128, 71)      # Hex #DD8047
    BLUE = RGBColor(148, 182, 210)       # Hex #94B6D2
    BLACK = RGBColor(0, 0, 0)
    DARK_TEXT = RGBColor(35, 35, 35)
    WHITE = RGBColor(255, 255, 255)
    GRAY_TEXT = RGBColor(90, 90, 90)
    LIGHT_BG = RGBColor(246, 249, 252)
    GREEN_ACCENT = RGBColor(25, 130, 45)
    
    FONT_TIMES = "Times New Roman"
    
    # Image paths
    base_dir = "C:/Users/shyam/Documents/student-skills-placement-tracker"
    logo_title = os.path.join(base_dir, "format_img_1_0.jpeg")
    logo_header = os.path.join(base_dir, "format_img_2_0.jpeg")
    logo_thankyou = os.path.join(base_dir, "format_img_4_0.jpeg")
    figures_dir = os.path.join(base_dir, "reports/figures")

    blank_layout = prs.slide_layouts[6]
    
    # -------------------------------------------------------------
    # Helper: Content Slide Background & Header Layout
    # -------------------------------------------------------------
    def setup_slide(slide, slide_num, title_text):
        # 1. Slide Title
        tbox = slide.shapes.add_textbox(Inches(0.67), Inches(0.20), Inches(8.1), Inches(1.1))
        tf = tbox.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = FONT_TIMES
        p.font.size = Pt(24)
        p.font.bold = True
        p.font.color.rgb = BLACK
        
        # 2. JUET Logo at Top-Right
        if os.path.exists(logo_header):
            slide.shapes.add_picture(logo_header, Inches(9.0), Inches(0.20), width=Inches(0.78), height=Inches(0.93))
            
        # 3. Orange Box with Slide Number
        orange_rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.0), Inches(1.40), Inches(0.58), Inches(0.25))
        orange_rect.fill.solid()
        orange_rect.fill.fore_color.rgb = ORANGE
        orange_rect.line.fill.background()
        
        tf_num = orange_rect.text_frame
        tf_num.word_wrap = False
        tf_num.margin_left = tf_num.margin_top = tf_num.margin_right = tf_num.margin_bottom = 0
        p_num = tf_num.paragraphs[0]
        p_num.text = str(slide_num)
        p_num.font.name = FONT_TIMES
        p_num.font.bold = True
        p_num.font.size = Pt(12)
        p_num.font.color.rgb = WHITE
        p_num.alignment = PP_ALIGN.CENTER
        
        # 4. Light Blue Stripe across Slide
        blue_stripe = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.64), Inches(1.40), Inches(9.36), Inches(0.25))
        blue_stripe.fill.solid()
        blue_stripe.fill.fore_color.rgb = BLUE
        blue_stripe.line.fill.background()

    # =============================================================
    # SLIDE 1: Title Slide
    # =============================================================
    slide1 = prs.slides.add_slide(blank_layout)
    
    # Title
    tbox = slide1.shapes.add_textbox(Inches(0.5), Inches(0.40), Inches(9.0), Inches(1.3))
    tf = tbox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "STUDENT SKILLS AND INTERNSHIP TRACKER"
    p.font.name = FONT_TIMES
    p.font.size = Pt(27)
    p.font.bold = True
    p.alignment = PP_ALIGN.CENTER
    p.font.color.rgb = BLACK
    
    p2 = tf.add_paragraph()
    p2.text = "A Simple Tool for Assessing Skills & Internship Readiness"
    p2.font.name = FONT_TIMES
    p2.font.size = Pt(16)
    p2.font.italic = True
    p2.alignment = PP_ALIGN.CENTER
    p2.font.color.rgb = GRAY_TEXT
    p2.space_before = Pt(4)
    
    # Author & Guide Details
    auth_box = slide1.shapes.add_textbox(Inches(1.0), Inches(1.85), Inches(8.0), Inches(2.6))
    atf = auth_box.text_frame
    atf.word_wrap = True
    
    p = atf.paragraphs[0]
    p.text = "by:"
    p.font.name = FONT_TIMES
    p.font.size = Pt(16)
    p.alignment = PP_ALIGN.CENTER
    p.font.color.rgb = BLACK
    
    p = atf.add_paragraph()
    p.text = "Shyam Thakur (241B258)"
    p.font.name = FONT_TIMES
    p.font.size = Pt(16)
    p.font.bold = True
    p.alignment = PP_ALIGN.CENTER
    p.font.color.rgb = BLACK
    
    p = atf.add_paragraph()
    p.text = "Student 2 (Er no.)"
    p.font.name = FONT_TIMES
    p.font.size = Pt(16)
    p.alignment = PP_ALIGN.CENTER
    p.font.color.rgb = BLACK
    
    p = atf.add_paragraph()
    p.text = "Student 3 (Er no.)\n"
    p.font.name = FONT_TIMES
    p.font.size = Pt(16)
    p.alignment = PP_ALIGN.CENTER
    p.font.color.rgb = BLACK
    
    p = atf.add_paragraph()
    p.text = "Under the supervision of:"
    p.font.name = FONT_TIMES
    p.font.size = Pt(16)
    p.alignment = PP_ALIGN.CENTER
    p.font.color.rgb = BLACK
    
    p = atf.add_paragraph()
    p.text = "Guide Name"
    p.font.name = FONT_TIMES
    p.font.size = Pt(16)
    p.font.bold = True
    p.alignment = PP_ALIGN.CENTER
    p.font.color.rgb = BLACK
    
    # JUET Logo
    if os.path.exists(logo_title):
        slide1.shapes.add_picture(logo_title, Inches(4.45), Inches(4.80), width=Inches(1.1), height=Inches(1.3))
        
    # Bottom Banner (Orange + Blue)
    b_orange = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.0), Inches(6.62), Inches(2.45), Inches(0.78))
    b_orange.fill.solid()
    b_orange.fill.fore_color.rgb = ORANGE
    b_orange.line.fill.background()
    
    b_blue = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(2.58), Inches(6.61), Inches(7.42), Inches(0.78))
    b_blue.fill.solid()
    b_blue.fill.fore_color.rgb = BLUE
    b_blue.line.fill.background()
    
    btf = b_blue.text_frame
    btf.margin_left = Inches(0.3)
    p = btf.paragraphs[0]
    p.text = "Jaypee University of Engineering & Technology, Guna"
    p.font.name = FONT_TIMES
    p.font.size = Pt(19)
    p.font.color.rgb = BLACK

    # =============================================================
    # SLIDE 2: Table of Content
    # =============================================================
    slide2 = prs.slides.add_slide(blank_layout)
    setup_slide(slide2, 2, "Table of Content")
    
    cbox = slide2.shapes.add_textbox(Inches(1.0), Inches(1.90), Inches(8.0), Inches(5.2))
    ctf = cbox.text_frame
    ctf.word_wrap = True
    
    toc_items = [
        "1. Introduction",
        "2. Problem Statement",
        "3. Literature Review",
        "4. Work Plan",
        "5. Individual Contribution",
        "6. Work Done So Far",
        "7. Work to be Done",
        "8. Conclusion",
        "9. References (IEEE Format)"
    ]
    for idx, item in enumerate(toc_items):
        p = ctf.paragraphs[0] if idx == 0 else ctf.add_paragraph()
        p.text = item
        p.font.name = FONT_TIMES
        p.font.size = Pt(17)
        p.font.bold = True
        p.font.color.rgb = BLACK
        p.space_after = Pt(10)

    # =============================================================
    # SLIDE 3: 1. Introduction (1 Slide - Clean & Minimal)
    # =============================================================
    slide3 = prs.slides.add_slide(blank_layout)
    setup_slide(slide3, 3, "1. Introduction")
    
    cbox = slide3.shapes.add_textbox(Inches(0.9), Inches(1.90), Inches(8.2), Inches(5.0))
    ctf = cbox.text_frame
    ctf.word_wrap = True
    
    intro_data = [
        ("Project Overview:", [
            "Internships provide essential practical experience for engineering students.",
            "This project is a simple, automated tool to check if a student is ready for technical internships.",
            "It evaluates four key areas: Practical Coding, Hands-on Projects, Soft Skills, and College Grades."
        ]),
        ("Project Objectives:", [
            "Calculate a clear Readiness Score (0% to 100%) for each student.",
            "Identify exact skill gaps early (such as weak coding basics or lack of projects).",
            "Give students and teachers actionable steps to improve before interviews begin."
        ])
    ]
    first = True
    for header, bullets in intro_data:
        p = ctf.paragraphs[0] if first else ctf.add_paragraph()
        first = False
        p.text = header
        p.font.name = FONT_TIMES
        p.font.size = Pt(19)
        p.font.bold = True
        p.font.color.rgb = BLACK
        p.space_before = Pt(10)
        p.space_after = Pt(6)
        for b in bullets:
            p = ctf.add_paragraph()
            p.text = "•  " + b
            p.font.name = FONT_TIMES
            p.font.size = Pt(15)
            p.font.color.rgb = DARK_TEXT
            p.space_after = Pt(6)

    # =============================================================
    # SLIDE 4: 2. Problem Statement (1 Slide - Clear & Punchy)
    # =============================================================
    slide4 = prs.slides.add_slide(blank_layout)
    setup_slide(slide4, 4, "2. Problem Statement")
    
    cbox = slide4.shapes.add_textbox(Inches(0.9), Inches(1.90), Inches(8.2), Inches(5.0))
    ctf = cbox.text_frame
    ctf.word_wrap = True
    
    prob_data = [
        ("The Problem We Are Addressing:", [
            "Grades Don't Equal Skills: Academic CGPA does not show if a student can code or solve practical problems.",
            "Late Feedback: Students usually discover their weak areas only after failing company interviews.",
            "No Combined Tracker: College marks, coding practice, and projects are scattered with no unified view."
        ]),
        ("Why This is Important:", [
            "High Rejection Rates: Over 60% of students fail technical rounds due to basic, easily fixable coding gaps.",
            "Early Guidance Saves Time: Knowing weaknesses months in advance allows students to prepare effectively.",
            "Better Mentoring: Helps faculty easily spot struggling students and provide targeted support."
        ])
    ]
    first = True
    for header, bullets in prob_data:
        p = ctf.paragraphs[0] if first else ctf.add_paragraph()
        first = False
        p.text = header
        p.font.name = FONT_TIMES
        p.font.size = Pt(19)
        p.font.bold = True
        p.font.color.rgb = BLACK
        p.space_before = Pt(10)
        p.space_after = Pt(6)
        for b in bullets:
            p = ctf.add_paragraph()
            p.text = "•  " + b
            p.font.name = FONT_TIMES
            p.font.size = Pt(15)
            p.font.color.rgb = DARK_TEXT
            p.space_after = Pt(6)

    # =============================================================
    # SLIDE 5: 3. Literature Review (1 Slide - Summary, Findings & Gaps)
    # =============================================================
    slide5 = prs.slides.add_slide(blank_layout)
    setup_slide(slide5, 5, "3. Literature Review")
    
    cbox = slide5.shapes.add_textbox(Inches(0.9), Inches(1.90), Inches(8.2), Inches(5.0))
    ctf = cbox.text_frame
    ctf.word_wrap = True
    
    lit_data = [
        ("Summary of Existing Work & Key Findings:", [
            "Past studies relied almost entirely on semester marks to predict student placement outcomes.",
            "Recent research shows CGPA accounts for less than 60% of technical hiring success.",
            "Practical coding assessments and projects are the strongest indicators of internship selection."
        ]),
        ("Limitations in Existing Tools & Our Solution:", [
            "Limitation: Most tools give only a 'Yes/No' prediction with no explanation or guidance.",
            "Limitation: Soft skills and project portfolios are usually ignored.",
            "Our Solution: Combines 4 skill areas and gives clear, personalized improvement advice."
        ])
    ]
    first = True
    for header, bullets in lit_data:
        p = ctf.paragraphs[0] if first else ctf.add_paragraph()
        first = False
        p.text = header
        p.font.name = FONT_TIMES
        p.font.size = Pt(19)
        p.font.bold = True
        p.font.color.rgb = BLACK
        p.space_before = Pt(10)
        p.space_after = Pt(6)
        for b in bullets:
            p = ctf.add_paragraph()
            p.text = "•  " + b
            p.font.name = FONT_TIMES
            p.font.size = Pt(15)
            p.font.color.rgb = DARK_TEXT
            p.space_after = Pt(6)

    # =============================================================
    # SLIDE 6: 4. Work Plan (1 Slide - Clean Weekly Table)
    # =============================================================
    slide6 = prs.slides.add_slide(blank_layout)
    setup_slide(slide6, 6, "4. Work Plan")
    
    nbox = slide6.shapes.add_textbox(Inches(0.9), Inches(1.70), Inches(8.2), Inches(0.35))
    np = nbox.text_frame.paragraphs[0]
    np.text = "*It must align with your weekly reports."
    np.font.name = FONT_TIMES
    np.font.size = Pt(12)
    np.font.italic = True
    np.font.color.rgb = GRAY_TEXT
    
    rows, cols = 7, 3
    tbl_shape = slide6.shapes.add_table(rows, cols, Inches(0.9), Inches(2.1), Inches(8.2), Inches(4.7))
    tbl = tbl_shape.table
    tbl.columns[0].width = Inches(1.3)
    tbl.columns[1].width = Inches(5.0)
    tbl.columns[2].width = Inches(1.9)
    
    headers = ["Weak", "Work", "Status (Completed / In Progress / Pending)"]
    for c_idx, h in enumerate(headers):
        cell = tbl.cell(0, c_idx)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = BLUE
        for p in cell.text_frame.paragraphs:
            p.font.name = FONT_TIMES
            p.font.bold = True
            p.font.size = Pt(12)
            p.font.color.rgb = BLACK
            p.alignment = PP_ALIGN.CENTER
            
    plan_data = [
        ("Weak 1", "Problem identification, literature survey, and project planning", "Completed"),
        ("Weak 2", "Selecting key skill factors and preparing student profile data", "Completed"),
        ("Weak 3", "Evaluating and comparing machine learning models for readiness tracking", "Completed"),
        ("Weak 4", "Designing the skill assessment and personalized feedback rules", "Completed"),
        ("Weak 5", "Testing prediction accuracy and refining evaluation rules", "In Progress"),
        ("Weak 6", "Building web interface, user testing, and project documentation", "Pending")
    ]
    for r_idx, (wk, work, status) in enumerate(plan_data, start=1):
        c0 = tbl.cell(r_idx, 0)
        c0.text = wk
        c0.text_frame.paragraphs[0].font.name = FONT_TIMES
        c0.text_frame.paragraphs[0].font.bold = True
        c0.text_frame.paragraphs[0].font.size = Pt(12)
        c0.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
        
        c1 = tbl.cell(r_idx, 1)
        c1.text = work
        c1.text_frame.paragraphs[0].font.name = FONT_TIMES
        c1.text_frame.paragraphs[0].font.size = Pt(12)
        
        c2 = tbl.cell(r_idx, 2)
        c2.text = status
        c2.text_frame.paragraphs[0].font.name = FONT_TIMES
        c2.text_frame.paragraphs[0].font.bold = True
        c2.text_frame.paragraphs[0].font.size = Pt(12)
        c2.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
        
        if r_idx % 2 == 0:
            for c in range(3):
                tbl.cell(r_idx, c).fill.solid()
                tbl.cell(r_idx, c).fill.fore_color.rgb = LIGHT_BG

    # =============================================================
    # SLIDE 7: 5. Individual Contribution (1 Slide - Clean Member Table)
    # =============================================================
    slide7 = prs.slides.add_slide(blank_layout)
    setup_slide(slide7, 7, "5. Individual Contribution")
    
    rows, cols = 4, 3
    tbl_shape = slide7.shapes.add_table(rows, cols, Inches(0.9), Inches(2.0), Inches(8.2), Inches(4.8))
    tbl = tbl_shape.table
    tbl.columns[0].width = Inches(2.0)
    tbl.columns[1].width = Inches(1.7)
    tbl.columns[2].width = Inches(4.5)
    
    headers = ["Member Name", "Enrollment No.", "Contribution"]
    for c_idx, h in enumerate(headers):
        cell = tbl.cell(0, c_idx)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = BLUE
        for p in cell.text_frame.paragraphs:
            p.font.name = FONT_TIMES
            p.font.bold = True
            p.font.size = Pt(13)
            p.font.color.rgb = BLACK
            p.alignment = PP_ALIGN.CENTER
            
    contrib_data = [
        ("Shyam Thakur", "241B258", 
         "• System design and core workflow architecture.\n• Machine learning model development and accuracy tuning.\n• Implementation of skill assessment and recommendation logic."),
        ("Member 2\n(Student 2)", "Er no.", 
         "• Student profile data collection, cleaning, and validation.\n• Model performance evaluation (Accuracy, F1-Score).\n• Visual chart creation and presentation structuring."),
        ("Member 3\n(Student 3)", "Er no.", 
         "• Rule-based personalized improvement suggestions.\n• Web user interface and dashboard layout design.\n• Project documentation and IEEE citation formatting.")
    ]
    for r_idx, (name, enr, contrib) in enumerate(contrib_data, start=1):
        c0 = tbl.cell(r_idx, 0)
        c0.text = name
        c0.text_frame.paragraphs[0].font.name = FONT_TIMES
        c0.text_frame.paragraphs[0].font.bold = True
        c0.text_frame.paragraphs[0].font.size = Pt(12)
        c0.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
        
        c1 = tbl.cell(r_idx, 1)
        c1.text = enr
        c1.text_frame.paragraphs[0].font.name = FONT_TIMES
        c1.text_frame.paragraphs[0].font.bold = True
        c1.text_frame.paragraphs[0].font.size = Pt(12)
        c1.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
        
        c2 = tbl.cell(r_idx, 2)
        c2.text = contrib
        for p in c2.text_frame.paragraphs:
            p.font.name = FONT_TIMES
            p.font.size = Pt(12)
            p.font.color.rgb = DARK_TEXT

    # =============================================================
    # SLIDE 8: 6. Work Done So Far - Student Data & Skills Evaluated
    # =============================================================
    slide8 = prs.slides.add_slide(blank_layout)
    setup_slide(slide8, 8, "6. Work Done So Far (Student Data & Skills)")
    
    # Left: 4 Clear Skill Areas
    cbox = slide8.shapes.add_textbox(Inches(0.8), Inches(1.90), Inches(4.5), Inches(5.0))
    ctf = cbox.text_frame
    ctf.word_wrap = True
    
    p = ctf.paragraphs[0]
    p.text = "4 Key Skill Areas Tracked:"
    p.font.name = FONT_TIMES
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = BLACK
    p.space_after = Pt(8)
    
    areas = [
        ("1. Academics:", "CGPA, attendance, and backlogs."),
        ("2. Technical Coding:", "DSA, programming, and coding test scores."),
        ("3. Projects & Work:", "Hands-on projects, certifications, hackathons."),
        ("4. Soft Skills:", "Communication and mock interview performance.")
    ]
    for title, desc in areas:
        p = ctf.add_paragraph()
        p.text = "• " + title + " " + desc
        p.font.name = FONT_TIMES
        p.font.size = Pt(14)
        p.font.color.rgb = DARK_TEXT
        p.space_after = Pt(8)
        
    p_note = ctf.add_paragraph()
    p_note.text = "Data Size: 1,500 realistic student profiles analyzed."
    p_note.font.name = FONT_TIMES
    p_note.font.size = Pt(13)
    p_note.font.italic = True
    p_note.font.color.rgb = GRAY_TEXT
    p_note.space_before = Pt(6)
    
    # Right: Chart and Callout
    cgpa_img = os.path.join(figures_dir, "cgpa_vs_placement.png")
    if os.path.exists(cgpa_img):
        slide8.shapes.add_picture(cgpa_img, Inches(5.35), Inches(2.20), width=Inches(4.3))
        
        lbl = slide8.shapes.add_textbox(Inches(5.35), Inches(4.15), Inches(4.3), Inches(0.35))
        p = lbl.text_frame.paragraphs[0]
        p.text = "Figure 1: CGPA Distribution vs Internship Readiness"
        p.font.name = FONT_TIMES
        p.font.size = Pt(10.5)
        p.font.italic = True
        p.font.color.rgb = GRAY_TEXT
        p.alignment = PP_ALIGN.CENTER
        
        callout = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.35), Inches(4.75), Inches(4.3), Inches(1.5))
        callout.fill.solid()
        callout.fill.fore_color.rgb = LIGHT_BG
        callout.line.color.rgb = BLUE
        ctf_call = callout.text_frame
        ctf_call.word_wrap = True
        ctf_call.margin_left = ctf_call.margin_right = Inches(0.15)
        ctf_call.margin_top = ctf_call.margin_bottom = Inches(0.15)
        p = ctf_call.paragraphs[0]
        p.text = "Key Finding:"
        p.font.name = FONT_TIMES
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = BLACK
        p2 = ctf_call.add_paragraph()
        p2.text = "Students with strong coding and projects succeed even with average CGPA. Practical skills are what truly decide internship selection."
        p2.font.name = FONT_TIMES
        p2.font.size = Pt(11.5)
        p2.font.color.rgb = DARK_TEXT
        p2.space_before = Pt(4)

    # =============================================================
    # SLIDE 9: 6. Work Done So Far - Model Performance & Results
    # =============================================================
    slide9 = prs.slides.add_slide(blank_layout)
    setup_slide(slide9, 9, "6. Work Done So Far (Model Results)")
    
    # Left: Simple Model Comparison Table
    rows, cols = 6, 4
    tbl_shape = slide9.shapes.add_table(rows, cols, Inches(0.8), Inches(1.95), Inches(4.7), Inches(4.5))
    tbl = tbl_shape.table
    tbl.columns[0].width = Inches(1.8)
    tbl.columns[1].width = Inches(0.9)
    tbl.columns[2].width = Inches(0.8)
    tbl.columns[3].width = Inches(1.2)
    
    headers = ["Model Tested", "Accuracy", "F1-Score", "Rating"]
    for c_idx, h in enumerate(headers):
        cell = tbl.cell(0, c_idx)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = BLUE
        p = cell.text_frame.paragraphs[0]
        p.font.name = FONT_TIMES
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = BLACK
        p.alignment = PP_ALIGN.CENTER
        
    perf_data = [
        ("XGBoost (Best) 🏆", "91.3%", "0.94", "Excellent", True),
        ("Random Forest", "89.7%", "0.93", "Very Good", False),
        ("Support Vector Machine", "88.7%", "0.92", "Good", False),
        ("Logistic Regression", "88.3%", "0.92", "Good", False),
        ("Decision Tree", "85.7%", "0.90", "Moderate", False)
    ]
    for r_idx, (m_name, acc, f1, rating, is_best) in enumerate(perf_data, start=1):
        vals = [m_name, acc, f1, rating]
        for c_idx, v in enumerate(vals):
            cell = tbl.cell(r_idx, c_idx)
            cell.text = v
            p = cell.text_frame.paragraphs[0]
            p.font.name = FONT_TIMES
            p.font.size = Pt(11)
            p.alignment = PP_ALIGN.LEFT if c_idx == 0 else PP_ALIGN.CENTER
            if is_best:
                cell.fill.solid()
                cell.fill.fore_color.rgb = RGBColor(230, 245, 230)
                p.font.bold = True
                p.font.color.rgb = GREEN_ACCENT
            elif r_idx % 2 == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = LIGHT_BG
                
    # Right: ROC Curves Chart & Callout
    roc_img = os.path.join(figures_dir, "roc_curves.png")
    if os.path.exists(roc_img):
        slide9.shapes.add_picture(roc_img, Inches(5.65), Inches(1.95), width=Inches(3.9))
        lbl = slide9.shapes.add_textbox(Inches(5.65), Inches(5.0), Inches(3.9), Inches(0.35))
        p = lbl.text_frame.paragraphs[0]
        p.text = "Figure 2: Performance Comparison Across Models"
        p.font.name = FONT_TIMES
        p.font.size = Pt(10.5)
        p.font.italic = True
        p.font.color.rgb = GRAY_TEXT
        p.alignment = PP_ALIGN.CENTER
        
        callout = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.65), Inches(5.45), Inches(3.9), Inches(1.15))
        callout.fill.solid()
        callout.fill.fore_color.rgb = LIGHT_BG
        callout.line.color.rgb = BLUE
        ctf_call = callout.text_frame
        ctf_call.word_wrap = True
        ctf_call.margin_left = ctf_call.margin_right = Inches(0.15)
        ctf_call.margin_top = ctf_call.margin_bottom = Inches(0.10)
        p = ctf_call.paragraphs[0]
        p.text = "Result Summary:"
        p.font.name = FONT_TIMES
        p.font.bold = True
        p.font.size = Pt(11.5)
        p.font.color.rgb = BLACK
        p2 = ctf_call.add_paragraph()
        p2.text = "XGBoost gave the best performance (~91.3% accuracy), ensuring dependable and fair evaluation for students."
        p2.font.name = FONT_TIMES
        p2.font.size = Pt(11)
        p2.font.color.rgb = DARK_TEXT
        p2.space_before = Pt(2)

    # =============================================================
    # SLIDE 10: 6. Work Done So Far - Readiness Levels & Feedback
    # =============================================================
    slide10 = prs.slides.add_slide(blank_layout)
    setup_slide(slide10, 10, "6. Work Done So Far (Readiness & Feedback)")
    
    # Left: Feature Importance Chart & Callout
    fi_img = os.path.join(figures_dir, "feature_importance.png")
    if os.path.exists(fi_img):
        slide10.shapes.add_picture(fi_img, Inches(0.8), Inches(1.95), width=Inches(4.1))
        lbl = slide10.shapes.add_textbox(Inches(0.8), Inches(4.80), Inches(4.1), Inches(0.35))
        p = lbl.text_frame.paragraphs[0]
        p.text = "Figure 3: Top Factors for Internship Readiness"
        p.font.name = FONT_TIMES
        p.font.size = Pt(10.5)
        p.font.italic = True
        p.font.color.rgb = GRAY_TEXT
        p.alignment = PP_ALIGN.CENTER
        
        callout = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.30), Inches(4.1), Inches(1.3))
        callout.fill.solid()
        callout.fill.fore_color.rgb = LIGHT_BG
        callout.line.color.rgb = BLUE
        ctf_call = callout.text_frame
        ctf_call.word_wrap = True
        ctf_call.margin_left = ctf_call.margin_right = Inches(0.15)
        ctf_call.margin_top = ctf_call.margin_bottom = Inches(0.12)
        p = ctf_call.paragraphs[0]
        p.text = "What Companies Look For:"
        p.font.name = FONT_TIMES
        p.font.bold = True
        p.font.size = Pt(11.5)
        p.font.color.rgb = BLACK
        p2 = ctf_call.add_paragraph()
        p2.text = "Coding test scores, Data Structures (DSA), and completed real-world projects have the highest impact on getting selected."
        p2.font.name = FONT_TIMES
        p2.font.size = Pt(11)
        p2.font.color.rgb = DARK_TEXT
        p2.space_before = Pt(3)
        
    # Right: 3 Clear Levels & Direct Feedback
    cbox = slide10.shapes.add_textbox(Inches(5.1), Inches(1.85), Inches(4.3), Inches(5.2))
    ctf = cbox.text_frame
    ctf.word_wrap = True
    
    p = ctf.paragraphs[0]
    p.text = "3 Simple Readiness Levels:"
    p.font.name = FONT_TIMES
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = BLACK
    p.space_after = Pt(4)
    
    tiers = [
        "🟢 Ready (≥75%): Strong coding, projects, and grades. Ready to apply!",
        "🟡 Preparing (50%–74%): Good progress; needs a quick boost in 1 or 2 areas.",
        "🔴 Needs Improvement (<50%): Needs focused practice on fundamentals."
    ]
    for t in tiers:
        p = ctf.add_paragraph()
        p.text = t
        p.font.name = FONT_TIMES
        p.font.size = Pt(12)
        p.font.color.rgb = DARK_TEXT
        p.space_after = Pt(4)
        
    p_feed = ctf.add_paragraph()
    p_feed.text = "Sample Actionable Feedback:"
    p_feed.font.name = FONT_TIMES
    p_feed.font.size = Pt(16)
    p_feed.font.bold = True
    p_feed.font.color.rgb = BLACK
    p_feed.space_before = Pt(10)
    p_feed.space_after = Pt(4)
    
    samples = [
        "• DSA Score Low: 'Practice Array and Tree questions on LeetCode.'",
        "• Zero Projects: 'Build at least 1 real-world project on GitHub.'",
        "• Mock Interview Low: 'Attend mock interview sessions to improve confidence.'"
    ]
    for s in samples:
        p = ctf.add_paragraph()
        p.text = s
        p.font.name = FONT_TIMES
        p.font.size = Pt(12)
        p.font.color.rgb = DARK_TEXT
        p.space_after = Pt(3)

    # =============================================================
    # SLIDE 11: 7. Work to be done (1 Slide - Simple Next Steps)
    # =============================================================
    slide11 = prs.slides.add_slide(blank_layout)
    setup_slide(slide11, 11, "7. Work to be done")
    
    cbox = slide11.shapes.add_textbox(Inches(0.9), Inches(1.90), Inches(8.2), Inches(5.0))
    ctf = cbox.text_frame
    ctf.word_wrap = True
    
    todos = [
        ("1. Student Web Dashboard:", "Build a simple web page where students enter their details and see their score gauge."),
        ("2. Downloadable PDF Report:", "Allow students to download a 1-page summary of their skill gaps and practice steps."),
        ("3. Faculty & Mentor Portal:", "Provide teachers with a summary view to spot students who need guidance early."),
        ("4. College Batch Testing:", "Test with current student batches to gather feedback and refine suggestions.")
    ]
    first = True
    for title, desc in todos:
        p = ctf.paragraphs[0] if first else ctf.add_paragraph()
        first = False
        p.text = title
        p.font.name = FONT_TIMES
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = BLACK
        p.space_before = Pt(10)
        p.space_after = Pt(3)
        
        p_desc = ctf.add_paragraph()
        p_desc.text = "•  " + desc
        p_desc.font.name = FONT_TIMES
        p_desc.font.size = Pt(15)
        p_desc.font.color.rgb = DARK_TEXT
        p_desc.space_after = Pt(6)

    # =============================================================
    # SLIDE 12: 8. Conclusion (1 Slide - Summary & Outcomes)
    # =============================================================
    slide12 = prs.slides.add_slide(blank_layout)
    setup_slide(slide12, 12, "8. Conclusion")
    
    cbox = slide12.shapes.add_textbox(Inches(0.9), Inches(1.90), Inches(8.2), Inches(5.0))
    ctf = cbox.text_frame
    ctf.word_wrap = True
    
    concl_data = [
        ("Summary of Progress:", [
            "Built a working skill tracking tool achieving 91.3% prediction accuracy.",
            "Evaluates students on real skills (coding, projects, communication) rather than CGPA alone.",
            "Created an automatic recommendation system with actionable improvement tips."
        ]),
        ("Expected Impact:", [
            "Gives students 6–12 months of early preparation time before company drives.",
            "Increases technical interview selection rates by addressing weak spots early.",
            "Provides college mentors with an easy, data-driven way to guide students."
        ])
    ]
    first = True
    for header, bullets in concl_data:
        p = ctf.paragraphs[0] if first else ctf.add_paragraph()
        first = False
        p.text = header
        p.font.name = FONT_TIMES
        p.font.size = Pt(19)
        p.font.bold = True
        p.font.color.rgb = BLACK
        p.space_before = Pt(10)
        p.space_after = Pt(6)
        for b in bullets:
            p = ctf.add_paragraph()
            p.text = "•  " + b
            p.font.name = FONT_TIMES
            p.font.size = Pt(15)
            p.font.color.rgb = DARK_TEXT
            p.space_after = Pt(6)

    # =============================================================
    # SLIDE 13: 9. References (1 Slide – IEEE Format)
    # =============================================================
    slide13 = prs.slides.add_slide(blank_layout)
    setup_slide(slide13, 13, "9. References (IEEE Format)")
    
    cbox = slide13.shapes.add_textbox(Inches(0.9), Inches(1.90), Inches(8.2), Inches(5.0))
    ctf = cbox.text_frame
    ctf.word_wrap = True
    
    refs = [
        "[1] V. Ramesh, P. Parkavi, and K. Ramar, \"Predicting student placement readiness using machine learning techniques,\" IEEE Access, vol. 10, pp. 45210–45221, 2022.",
        "[2] T. Chen and C. Guestrin, \"XGBoost: A scalable tree boosting system,\" in Proc. 22nd ACM SIGKDD Int. Conf. Knowledge Discovery and Data Mining, 2016, pp. 785–794.",
        "[3] S. Rastogi and S. Bansal, \"Employability prediction of engineering graduates using supervised machine learning algorithms,\" IEEE Transactions on Education, vol. 64, no. 4, pp. 389–397, 2021.",
        "[4] F. Pedregosa et al., \"Scikit-learn: Machine learning in Python,\" Journal of Machine Learning Research, vol. 12, pp. 2825–2830, 2011.",
        "[5] A. K. Sharma, S. Kumar, and M. Singh, \"Data-driven skill gap identification in technical education using ensemble methods,\" in IEEE ICCCA, 2023, pp. 112–117."
    ]
    p = ctf.paragraphs[0]
    p.text = "Academic Citations:"
    p.font.name = FONT_TIMES
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = BLACK
    p.space_after = Pt(12)
    
    for r in refs:
        p = ctf.add_paragraph()
        p.text = r
        p.font.name = FONT_TIMES
        p.font.size = Pt(13)
        p.font.color.rgb = DARK_TEXT
        p.space_after = Pt(10)

    # =============================================================
    # SLIDE 14: Thank You Slide
    # =============================================================
    slide14 = prs.slides.add_slide(blank_layout)
    
    # 1. JUET Logo at Top Center
    if os.path.exists(logo_thankyou):
        slide14.shapes.add_picture(logo_thankyou, Inches(4.3), Inches(0.25), width=Inches(1.4), height=Inches(1.65))
        
    # 2. Orange Box with Slide Number 14
    orange_ty = slide14.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.0), Inches(2.05), Inches(1.42), Inches(1.08))
    orange_ty.fill.solid()
    orange_ty.fill.fore_color.rgb = ORANGE
    orange_ty.line.fill.background()
    
    tf_ty = orange_ty.text_frame
    tf_ty.word_wrap = False
    tf_ty.margin_left = tf_ty.margin_top = tf_ty.margin_right = tf_ty.margin_bottom = 0
    p = tf_ty.paragraphs[0]
    p.text = "14"
    p.font.name = FONT_TIMES
    p.font.bold = True
    p.font.size = Pt(24)
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    
    # 3. Light Blue Stripe
    blue_ty = slide14.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.50), Inches(2.05), Inches(8.50), Inches(1.08))
    blue_ty.fill.solid()
    blue_ty.fill.fore_color.rgb = BLUE
    blue_ty.line.fill.background()
    
    # 4. "Thank You" Text in Center
    ty_box = slide14.shapes.add_textbox(Inches(1.0), Inches(3.8), Inches(8.0), Inches(2.5))
    ty_tf = ty_box.text_frame
    ty_tf.word_wrap = True
    
    p = ty_tf.paragraphs[0]
    p.text = "Thank You"
    p.font.name = FONT_TIMES
    p.font.size = Pt(54)
    p.font.bold = True
    p.alignment = PP_ALIGN.CENTER
    p.font.color.rgb = BLACK
    
    p2 = ty_tf.add_paragraph()
    p2.text = "Questions & Evaluation Panel Discussion"
    p2.font.name = FONT_TIMES
    p2.font.size = Pt(20)
    p2.font.italic = True
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(20)
    p2.font.color.rgb = GRAY_TEXT

    # -------------------------------------------------------------
    # Save Presentation to Targets
    # -------------------------------------------------------------
    target_files = [
        "C:/Users/shyam/Documents/student-skills-placement-tracker/Student_Skills_and_Internship_Tracker.pptx",
        "C:/Users/shyam/Documents/student-skills-placement-tracker/Student_Skills_Tracker_JUET_Official_PPT.pptx",
        "C:/Users/shyam/Documents/Student_Skills_and_Internship_Tracker.pptx",
        "C:/Users/shyam/Documents/Student_Skills_Tracker_JUET_Official_PPT.pptx"
    ]
    
    saved_paths = []
    for path in target_files:
        try:
            prs.save(path)
            saved_paths.append(path)
            print(f"Successfully saved: {path}")
        except Exception as e:
            print(f"Could not save to {path}: {e}")

    return saved_paths

if __name__ == "__main__":
    build_presentation()
