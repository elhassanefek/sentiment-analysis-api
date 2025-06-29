import keyword
from flask_smorest import Blueprint , abort 
from flask.views import MethodView
from app.schemas.twitter import TwitterRequestSchema , TwitterResponseSchema

from app.services.twitter_service import analyze_twitter_keyword

blp = Blueprint("Twitter(X)", "twitter", url_prefix = "/api/x" , description = "Twiiter (X) sentiment analysis")

@blp.route("/analyze")
class TwitterAnalyze(MethodView) :
    @blp.arguments(TwitterRequestSchema)
    @blp.response(200, TwitterResponseSchema)

    def post(self , request_data) :
        keyword = request_data.get("keyword")
        count = request_data.get("count")

        result = analyze_twitter_keyword(keyword , count) 
        return result 