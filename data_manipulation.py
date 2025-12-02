import numpy as np
import pandas as pd

try:
    df = pd.read_csv("sample_data.csv")
    print("Loaded dataset from sample_data.csv")
except:
    df = pd.DataFrame({
        "Name": ["Ali", "Sara", "Zain", "Hina", "Omar", "Ayesha", "Bilal"],
        "Age": [22, 25, 30, 28, 40, 50, 18],
        "Income": [30000, 45000, 60000, 52000, 80000, 90000, 20000],
        "City": ["Lahore", "Karachi", "Islamabad", "Lahore", "Karachi", "Lahore", "Lahore"]
    })
    print("No CSV found — using dummy dataset!")

print("\nOriginal Dataset:")
print(df)

df["Age_plus_5"] = df["Age"] + 5
df["Income_k"] = df["Income"] / 1000

df["City_Upper"] = df["City"].str.upper()
df["Name_Initial"] = df["Name"].str[0]

df_sorted = df.sort_values(by="Income", ascending=False)

df_filtered = df[(df["Age"] > 25) & (df["Income"] > 50000)]

age_mean = np.mean(df["Age"].to_numpy())
income_max = np.max(df["Income"].to_numpy())
income_min = np.min(df["Income"].to_numpy())

print("\nManipulated Dataset:")
print(df)

print("\nSorted by Income (Descending):")
print(df_sorted)

print("\nFiltered Data (Age > 25 AND Income > 50000):")
print(df_filtered)

print("\nStatistics:")
print("Mean Age:", age_mean)
print("Max Income:", income_max)
print("Min Income:", income_min)
