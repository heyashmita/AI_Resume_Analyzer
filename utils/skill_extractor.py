import pandas as pd

skills_db = pd.read_csv("data/skills.csv")

skills_list = skills_db.iloc[:,0].tolist()

def extract_skills(text):

    found_skills = []

    for skill in skills_list:

        if skill.lower() in text.lower():
            found_skills.append(skill)

    return list(set(found_skills))