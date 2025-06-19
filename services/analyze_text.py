from transformers import pipeline

# Load sentiment analysis pipeline once
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_text(text):
    """
    Analyzes the sentiment of a given text using Hugging Face transformers.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary with the sentiment label and confidence score.
    """
    result = sentiment_pipeline(text)[0]
    return {
        "label": result["label"],
        "confidence": round(result["score"], 4)
    }
