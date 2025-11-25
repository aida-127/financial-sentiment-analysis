# test_sentiment.py
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import yfinance as yf

print("🎉 FINANCIAL SENTIMENT ANALYSIS ENVIRONMENT READY!")
print("Packages working: pandas, matplotlib, textblob, vader, yfinance")

# Test sentiment analysis
headlines = [
    "Apple stock surges on strong earnings",
    "Market declines amid economic concerns"
]

analyzer = SentimentIntensityAnalyzer()
for headline in headlines:
    blob = TextBlob(headline)
    print(f"\n{headline}")
    print(f"TextBlob: {blob.sentiment}")
    print(f"VADER: {analyzer.polarity_scores(headline)}")

print("\n✅ Ready to start Task 1 EDA!")