from utils.text_cleaner import clean_text


resume_text = """
I am a Python Developer with 3 years experience.
I have completed 5 Machine Learning projects.
"""


result = clean_text(resume_text)


print(result)