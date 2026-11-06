def calculate_talent_score(candidate_skills, required_skills):

    if not required_skills:
        return 0, [], []

    matched = [
        skill for skill in required_skills
        if skill in candidate_skills
    ]

    missing = [
        skill for skill in required_skills
        if skill not in candidate_skills
    ]

    score = round(
        len(matched) / len(required_skills) * 100, 2
    )

    return score, matched, missing
