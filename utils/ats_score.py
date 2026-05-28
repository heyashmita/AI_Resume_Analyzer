def calculate_ats_score(skills):

    total_required_skills = 15

    score = (len(skills) / total_required_skills) * 100

    if score > 100:
        score = 100

    return round(score, 2)