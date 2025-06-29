from app.services.analyze_text import polarity_scores_reborta
import os 
from dotenv import load_dotenv
import tweepy 
load_dotenv()
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
client = tweepy.Client(bearer_token= BEARER_TOKEN)


def fetch_tweets_real(keyword, count=5):
    return [
        "I love AI and OpenAI!",
        "This project looks promising.",
        "I'm not convinced by AI yet.",
        "AI is the future of everything.",
        "I hate how slow it is."
    ]

def analyze_twitter_keyword(keyword, count=5):
    tweets = fetch_tweets_real(keyword, count)  # ← now uses mock
    results = []

    sentiment_counts = {"pos": 0, "neu": 0, "neg": 0}

    for tweet in tweets:
        scores = polarity_scores_reborta(tweet)
        label = max(scores, key=scores.get)
        sentiment = label.split('_')[-1]  # 'positive', 'neutral', 'negative'

        sentiment_counts[sentiment] += 1

        results.append({
            "text": tweet,
            "sentiment": sentiment
        })

    return {
        "keyword": keyword,
        "summary": sentiment_counts,
        "tweets": results
    }