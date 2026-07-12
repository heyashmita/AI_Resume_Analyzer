import pandas as pd

# load prepared dataset
data = pd.read_csv(
    "data/resume_dataset.csv"
)

# category mapping
category_mapping = {

    "INFORMATION-TECHNOLOGY": "Software Developer",

    "ENGINEERING": "Software Developer",

    "BUSINESS-DEVELOPMENT": "Business Analyst",

    "DESIGNER": "UI/UX Designer",

    "DIGITAL-MEDIA": "UI/UX Designer",

    "ACCOUNTANT": "Data Analyst",

    "FINANCE": "Data Analyst",

    "BANKING": "Data Analyst",

    "CONSULTANT": "Business Analyst",

    "AUTOMOBILE": "Engineering",

    "HR": "Human Resources"
}

#replace categories
data["Category"] = data["Category"].map(
    category_mapping
)

#remove unwanted categories
data.dropna(
    inplace=True
)

#save final dataset
data.to_csv(
    "data/final_resume_dataset.csv",
    index=False
)

print("Final Dataset Created")

print("\nDataset Size:")
print(data.shape)

print("\nCategories:")
print(data["Category"].value_counts())