import pandas as pd

data = pd.read_csv(
    "data/final_resume_dataset.csv"
)

print(data["Category"].value_counts())
