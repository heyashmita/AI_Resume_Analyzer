import joblib

from utils.text_cleaner import clean_text

#load trained model
model = joblib.load(
    "models/resume_classifier.pkl"
)

#load TF-IDF vectorizer
vectorizer = joblib.load(
    "models/tfidf_vectorizer.pkl"
)

#sample resume for testing
resume = """

Software Engineer with experience in Python,
Machine Learning and Artificial Intelligence.

Skills:
Python
TensorFlow
PyTorch
Scikit-learn
Pandas
NumPy
NLP
Computer Vision
Deep Learning

Projects:
Built an image classification model using CNN.
Developed NLP based chatbot using transformers.

"""
#clean resume text
cleaned_resume = clean_text(
    resume
)
#convert text into TF-IDF features
resume_vector = vectorizer.transform(
    [cleaned_resume]
)
#Prediction
prediction = model.predict(
    resume_vector
)
scores = model.decision_function(
    resume_vector
)
print("\nCategory Scores:")

for category, score in zip(model.classes_, scores[0]):
    print(
        category,
        round(score,3)
    )