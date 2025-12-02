data = np.array([10, 12, np.nan, 15, 300, 18, np.nan, 20, 14, 500])

print("Original Data:")
print(data)

clean_data = data[~np.isnan(data)]
print("\nAfter Removing NaN:")
print(clean_data)

Q1 = np.percentile(clean_data, 25)
Q3 = np.percentile(clean_data, 75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

median_value = np.median(clean_data)
outlier_cleaned = np.where((clean_data < lower_limit) | (clean_data > upper_limit),
                           median_value,
                           clean_data)

print("\nAfter Replacing Outliers:")
print(outlier_cleaned)

min_val = np.min(outlier_cleaned)
max_val = np.max(outlier_cleaned)

normalized_data = (outlier_cleaned - min_val) / (max_val - min_val)

print("\nNormalized Data (0–1 Scale):")
print(normalized_data)

print("\nSummary:")
print("Mean:", np.mean(normalized_data))
print("Std Dev:", np.std(normalized_data))
print("Min:", np.min(normalized_data))
print("Max:", np.max(normalized_data))
