from flask_smorest import Blueprint , abort
from flask.views import MethodView
from schemas.sentiment import SentimentRequestSchema , SentimentResponseSchema
from services import analyze_text

blp = Blueprint("Sentimet","sentiment",description = "Sentiment analysis routes")

@blp.route("/analyze")

class Sentiment(Methodview) :
    @blp.arguments(SentimentRequestSchema)
    @blp.respsonse(200, SentimentResponseSchema)

    def post(self,request_data) :

        result = analyse_text(request_data["text"])

        return result 