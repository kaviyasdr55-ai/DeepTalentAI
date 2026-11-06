JOB_ROLES = {
    "Python Developer": [
        "python", "sql", "flask", "django"
    ],

    "Data Analyst": [
        "python", "sql", "pandas",
        "numpy", "matplotlib"
    ],

    "Machine Learning Engineer": [
        "python", "machine learning",
        "scikit-learn", "pandas", "numpy"
    ],

    "Frontend Developer": [
        "html", "css", "javascript", "react"
    ],

    "Data Scientist": [
        "python", "machine learning",
        "deep learning", "pandas",
        "numpy", "sql"
    ]
}

def recommend_jobs(candidate_skills):

    recommendations = []

    for role, skills in JOB_ROLES.items():

        matched = [
            skill for skill in skills
            if skill in candidate_skills
        ]

        score = round(
            len(matched) / len(skills) * 100, 2
        )

        recommendations.append({
            "role": role,
            "score": score,
            "matched_skills": matched
        })

    return sorted(
        recommendations,
        key=lambda x: x["score"],
        reverse=True
    )
