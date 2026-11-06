def identify_skill_gaps(candidate_skills, required_skills):

    return [
        skill for skill in required_skills
        if skill not in candidate_skills
    ]
