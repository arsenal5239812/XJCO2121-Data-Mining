import pandas as pd

# 1. Load the CSV file
csv_file = r"your path\full_10000_cleaned.csv"
df = pd.read_csv(csv_file)

# 2. Clean and prepare
df.columns = df.columns.str.strip()
df['cleaned_review'] = df['cleaned_review'].astype(str).str.replace("'", "\\'", regex=False)
df['sentiment'] = df['sentiment'].astype(str)

# 3. Save as ARFF
arff_file = r"ypur path\full_10000_cleaned.arff"

with open(arff_file, 'w', encoding='utf-8') as f:
    f.write("@RELATION sentiment_analysis\n\n")
    f.write("@ATTRIBUTE cleaned_review STRING\n")
    classes = sorted(df['sentiment'].unique())
    f.write(f"@ATTRIBUTE sentiment {{{','.join(classes)}}}\n\n")
    f.write("@DATA\n")
    for _, row in df.iterrows():
        f.write(f"'{row['cleaned_review']}',{row['sentiment']}\n")

print("✅ ARFF file saved to:", arff_file)