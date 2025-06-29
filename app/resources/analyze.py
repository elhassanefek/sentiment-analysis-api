
from flask_smorest import Blueprint , abort
from flask.views import MethodView
from app.schemas.sentiment import SentimentRequestSchema , SentimentResponseSchema
from app.services.analyze_text import polarity_scores_reborta

blp = Blueprint("Sentiment","sentiment",description = "Sentiment analysis routes")

@blp.route("/analyze")

class Sentiment(MethodView) :
    @blp.arguments(SentimentRequestSchema)
    @blp.response(200, SentimentResponseSchema)

    def post(self,request_data) :

        text = request_data.get("text", "")

        if not text.strip() :
            abort(400, message = "Text input is empty")
        
        result = polarity_scores_reborta(text)

        return {
            "text": text,
            "predictions" : {
            "negative": result["roberta_neg"],
            "neutral": result["roberta_neu"],
            "positive": result["roberta_pos"]
             },
            "top_label": max(result, key=result.get).replace("roberta_", "")
        }