def recommend_role(skills):

    skills = [skill.lower() for skill in skills]

    if "machine learning" in skills or "tensorflow" in skills:
        return "Machine Learning Engineer"

    elif "react" in skills or "javascript" in skills:
        return "Frontend Developer"

    elif "sql" in skills and "python" in skills:
        return "Data Analyst"

    else:
        return "Software Developer"