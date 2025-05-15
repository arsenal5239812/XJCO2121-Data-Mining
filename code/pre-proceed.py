import pandas as pd
import string
import nltk
from nltk.corpus import stopwords

# Download English stopwords
nltk.download('stopwords')

# Load the original dataset (adjust the path if needed)
file_path = r"your path\Amazon_10k_Sample.csv"
try:
    df = pd.read_csv(file_path)
    print("File loaded successfully.")
except Exception as e:
    print("Failed to load file:", e)
    exit()

# Strip extra whitespace from column names (prevent hidden errors)
df.columns = df.columns.str.strip()

# Text cleaning function
def clean_text(text):
    if pd.isnull(text):
        return ""
    text = str(text).lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]  # Remove stopwords
    return ' '.join(words)

# Apply text cleaning with progress message
try:
    print("Cleaning review text...")
    df['cleaned_review'] = df['Reviews'].apply(clean_text)
    print("Text cleaning complete.")
except Exception as e:
    print("Error during text cleaning:", e)
    exit()

# Automatically label sentiment based on rating
def label_sentiment(rating):
    if rating >= 4:
        return 'positive'
    elif rating <= 2:
        return 'negative'
    else:
        return None  # Skip 3-star reviews

try:
    df['sentiment'] = df['Rating'].apply(label_sentiment)
    df = df.dropna(subset=['sentiment'])
    print(f"Sentiment labeled. Remaining rows after filtering: {len(df)}")
except Exception as e:
    print("Error during sentiment labeling:", e)
    exit()

# Save cleaned and labeled dataset
output_path = r"your path\full_10000_cleaned.csv"
try:
    df[['cleaned_review', 'sentiment']].to_csv(output_path, index=False)
    print("Cleaning complete. File saved to:", output_path)
except Exception as e:
    print("Failed to save output:", e)