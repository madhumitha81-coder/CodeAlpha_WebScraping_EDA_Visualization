import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns

# Create dataset
data = {
    "Review": [
        "This book is excellent and very interesting",
        "I really enjoyed this book",
        "Amazing story and great writing",
        "The book was boring and disappointing",
        "I did not like this book",
        "The story was terrible",
        "The book is okay",
        "It was an average book",
        "The story was fine"
    ]
}

df = pd.DataFrame(data)

# Sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to find sentiment
def get_sentiment(text):
    score = sia.polarity_scores(text)["compound"]

    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["Sentiment"] = df["Review"].apply(get_sentiment)

# Display results
print(df)

# Count sentiments
sentiment_counts = df["Sentiment"].value_counts()

print("\nSentiment Counts:")
print(sentiment_counts)

# Save results
df.to_csv("sentiment_results.csv", index=False)

# Create visualization
plt.figure(figsize=(7, 5))

sns.barplot(
    x=sentiment_counts.index,
    y=sentiment_counts.values
)

plt.title("Sentiment Analysis of Book Reviews")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")

plt.savefig("sentiment_distribution.png", bbox_inches="tight")

plt.show()