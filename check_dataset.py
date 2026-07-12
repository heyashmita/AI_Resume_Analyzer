import pandas as pd


# Load original Kaggle dataset

data = pd.read_csv(
    "data/Resume.csv"
)


# Display first 5 rows

print("\nFirst 5 rows:")
print(data.head())


# display column names
print("\nColumns:")
print(data.columns)


# display dataset size
print("\nDataset Size:")
print(data.shape)


# display all categories
print("\nCategories:")
print(data.iloc[:, -1].value_counts())