import pandas as pd

#load original dataset
data = pd.read_csv(
    "data/resume.csv"
)

#select required columns
data = data[
    [
        "Resume_str",
        "Category"
    ]
]

#rename Resume_str
data.rename(
    columns={
        "Resume_str": "Resume_Text"
    },
    inplace=True
)
#remove empty rows
data.dropna(
    inplace=True
)
#save cleaned dataset
data.to_csv(
    "data/resume_dataset.csv",
    index=False
)
print("Dataset prepared successfully!")

print(data.head())

print("\nDataset size:")
print(data.shape)

print("\nCategories:")
print(data["Category"].value_counts())