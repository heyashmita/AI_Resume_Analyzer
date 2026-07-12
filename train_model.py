import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, classification_report

import joblib


from utils.text_cleaner import clean_text
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns



# Load dataset

data = pd.read_csv(
    "data/final_resume_dataset.csv"
)


print("Dataset Loaded")
print(data.head())



# Remove empty values

data.dropna(
    inplace=True
)



# Clean resume text

data["Cleaned_Text"] = data["Resume_Text"].apply(
    clean_text
)



# Input

X = data["Cleaned_Text"]


# Output

y = data["Category"]



# Split dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)



# Convert text into numerical features

vectorizer = TfidfVectorizer(
    max_features=5000
)



X_train_vector = vectorizer.fit_transform(
    X_train
)


X_test_vector = vectorizer.transform(
    X_test
)



# Models

models = {

    "Logistic Regression":
    LogisticRegression(
        max_iter=1000
    ),


    "Support Vector Machine":
    LinearSVC(),


    "Random Forest":
    RandomForestClassifier(
        n_estimators=100
    )

}



best_model = None
best_accuracy = 0



for name, model in models.items():

    print("\nTraining:", name)


    model.fit(
        X_train_vector,
        y_train
    )


    prediction = model.predict(
        X_test_vector
    )


    accuracy = accuracy_score(
        y_test,
        prediction
    )


    print(
        "Accuracy:",
        accuracy
    )

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            prediction
        )
    )  

    cm = confusion_matrix(
        y_test,
        prediction
    )

    plt.figure(figsize=(10,7))

    sns.heatmap(   
        cm,
        annot=True,
        fmt="d"
    )

    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    plt.show()           



    if accuracy > best_accuracy:

        best_accuracy = accuracy

        best_model = model



print("\nBest Accuracy:")
print(best_accuracy)
print(type(best_model))



# Save model and vectorizer

joblib.dump(
    best_model,
    "models/resume_classifier.pkl"
)


joblib.dump(
    vectorizer,
    "models/tfidf_vectorizer.pkl"
)


print("\nModel Saved Successfully")