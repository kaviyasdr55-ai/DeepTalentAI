import os

from flask import Flask, render_template, request

from modules.resume_parser import extract_resume_text
from modules.skill_analyzer import extract_skills
from modules.talent_scorer import calculate_talent_score
from modules.career_recommender import recommend_jobs

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

JOB_SKILLS = {
    "Data Analyst": [
        "python", "sql", "pandas", "numpy", "matplotlib"
    ],

    "Python Developer": [
        "python", "sql", "flask", "django"
    ],

    "Machine Learning Engineer": [
        "python", "machine learning",
        "scikit-learn", "pandas", "numpy"
    ],

    "Frontend Developer": [
        "html", "css", "javascript", "react"
    ]
}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    file = request.files.get("resume")
    selected_role = request.form.get("role")

    if not file or not file.filename:
        return "Please upload a resume."

    if selected_role not in JOB_SKILLS:
        return "Please select a valid job role."

    allowed = (".pdf", ".docx", ".txt")

    if not file.filename.lower().endswith(allowed):
        return "Only PDF, DOCX and TXT files are supported."

    filename = os.path.basename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    file.save(file_path)

    try:
        resume_text = extract_resume_text(file_path)
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

    if not resume_text.strip():
        return "No readable text found in this resume."

    candidate_skills = extract_skills(resume_text)
    required_skills = JOB_SKILLS[selected_role]

    score, matched, missing = calculate_talent_score(
        candidate_skills,
        required_skills
    )

    recommendations = recommend_jobs(candidate_skills)

    return render_template(
        "result.html",
        candidate_skills=candidate_skills,
        score=score,
        matched=matched,
        missing=missing,
        recommendations=recommendations,
        selected_role=selected_role
    )


if __name__ == "__main__":
    app.run(debug=True)
