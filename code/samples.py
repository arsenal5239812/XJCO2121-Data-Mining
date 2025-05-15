import pandas as pd

# Original CSV file path
file_path = r"your path\Amazon_Unlocked_Mobile.csv"

# Raw data
df = pd.read_csv(file_path)

# Randomly sample 10000 pieces of data
sample_df = df.sample(n=10000, random_state=42)

# Save the sampled data to a new CSV file
output_path = r"your path\Amazon_10k_Sample.csv"
sample_df.to_csv(output_path, index=False)

print("Done! 10000 pieces of data have been saved to:", output_path)