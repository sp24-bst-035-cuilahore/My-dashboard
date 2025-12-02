import numpy as np
import pandas as pd

try:
    df = pd.read_csv("sample_data.csv")
    print("Loaded dataset from sample_data.csv")
except:
    df = pd.DataFrame({
        "Age": [22, 25, 30, 28, 40, 50, 18],
        "Income": [30000, 45000, 60000, 52000, 80000, 90000, 20000],
        "City": ["Lahore", "Karachi", "Islamabad", "Lahore", "Karachi", "Lahore", "Lahore"]
    })
    print("No CSV found — using dummy dataset!")

print("\nDataset:")
print(df)

ages = df["Age"].to_numpy()
print("\nExtracted Ages (NumPy Array):")
print(ages)

high_income = df[df["Income"] > 50000]
print("\nPeople with Income > 50,000:")
print(high_income)

unique_cities = np.unique(df["City"])
print("\nUnique Cities:")
print(unique_cities)

young_and_low_income = df[(df["Age"] < 30) & (df["Income"] < 50000)]
print("\nAge < 30 AND Income < 50,000:")
print(young_and_low_income)

print("\nStatistical Extraction:")
print("Mean Age:", np.mean(ages))
print("Max Income:", np.max(df["Income"].to_numpy()))
print("Min Income:", np.min(df["Income"].to_numpy()))

extracted_df = pd.DataFrame({
    "Age": ages,
    "Income": df["Income"].to_numpy()
})

print("\nFinal Extracted DataFrame:")
print(extracted_df)
