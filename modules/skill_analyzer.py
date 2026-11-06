SKILLS = [
    "python", "java", "c", "c++", "sql",
    "machine learning", "deep learning",
    "data analysis", "data science",
    "numpy", "pandas", "matplotlib",
    "scikit-learn", "tensorflow", "pytorch",
    "html", "css", "javascript",
    "flask", "django", "react",
    "mysql", "mongodb",
    "communication", "problem solving",
    "leadership", "teamwork"
]

def extract_skills(text):
    text = text.lower()
    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return found
