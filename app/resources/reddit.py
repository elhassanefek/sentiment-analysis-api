from flask_smorest import Blueprint , abort
from flask.views import MethodView 

from app.schemas.reddit import RedditRequestSchema , RedditResponseSchema
from app.services.reddit_service import analyze_reddit_subreddit

blp  = Blueprint("Reddit" , "reddit",url_prefix = "/api/reddit", description = "Reddit Sentiment Analysis")


@blp.route("/analyze") 
class RedditSentiment(MethodView) :
    @blp.arguments(RedditRequestSchema)
    @blp.response(200,RedditResponseSchema)
    def post(self , request_data) :
        subreddit = request_data.get("subreddit")
        count = request_data.get("count")


        if not subreddit :
            abort(400, message ="Subreddit is required")
        
        try :
             return analyze_reddit_subreddit(subreddit , count)
        except Exception as e :
            abort(500, message = str(e))
