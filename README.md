# Sentiment Analysis API (Flask Backend)

This is the backend API for analyzing the sentiment of text, Reddit comments, Twitter posts (mocked), and YouTube video comments using both classical and transformer-based NLP models (VADER and RoBERTa). Built with Flask and Flask-Smorest, the API is documented using Swagger/OpenAPI and ready for integration with a frontend dashboard or other services.

---

## Features

-  Analyze sentiment of raw text using VADER and RoBERTa
-  Analyze mocked Twitter data (or real with API)
-  Analyze YouTube video comments (by URL or keyword)
-  Analyze Reddit comments from a subreddit
-  Summary statistics of sentiments (positive, neutral, negative)

---
## Model Choice

In the `notebooks/` folder, we compared VADER (lexicon-based) and RoBERTa (transformer-based) for sentiment analysis.

Based on performance, we chose to integrate only **RoBERTa** into the production Flask API.

## Tech Stack

- Python 3.10+
- Flask
- Flask-Smorest (OpenAPI + Marshmallow)
- Hugging Face Transformers (`cardiffnlp/twitter-roberta-base-sentiment`)
- VADER SentimentIntensityAnalyzer
- Google API for YouTube
- PRAW for Reddit API
- dotenv for environment configuration

---
## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/sentiment-backend.git
cd sentiment-backend
```
### 2.Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4.Create .env file

#### .env
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=your_reddit_app_name

YOUTUBE_API_KEY=your_google_youtube_api_key
note : You must enable the YouTube Data API v3 from Google Cloud Console







