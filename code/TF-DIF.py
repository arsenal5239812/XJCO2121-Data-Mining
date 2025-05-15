import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import os

csv_path = r"your path\full_10000_cleaned.csv"
arff_path = r"your path\full_10000_vectorized.arff"

df = pd.read_csv(csv_path)
df.columns = df.columns.str.strip()

df['cleaned_review'] = df['cleaned_review'].astype(str).fillna('')
df['sentiment'] = df['sentiment'].astype(str).fillna('unknown')

vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(df['cleaned_review'])
tfidf_df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

tfidf_df['sentiment'] = df['sentiment'].values

with open(arff_path, 'w', encoding='utf-8') as f:
    f.write("@RELATION sentiment_tfidf\n\n")

    for col in tfidf_df.columns[:-1]:
        f.write(f"@ATTRIBUTE {col} NUMERIC\n")

    classes = sorted(tfidf_df['sentiment'].unique())
    f.write(f"@ATTRIBUTE sentiment {{{','.join(classes)}}}\n\n")

    f.write("@DATA\n")
    for i, row in tfidf_df.iterrows():
        values = [f"{v:.6f}" for v in row[:-1]] + [row['sentiment']]
        f.write(",".join(values) + "\n")

print("TF-IDF ARFF file saved to:", arff_path)