
from flask_smorest import Blueprint , abort 

from flask.views import MethodView 


from app.services.youtube_service import (
    extract_video_id,
    search_video_by_keyword,
    analyze_comments,
    analyze_comments_for_multiple_videos 

)
from app.schemas.youtube import (
    YoutubeByUrlRequestSchema,
    YouTubeByKeywordRequestSchema,
    YouTubeMultiKeywordRequestSchema,  
    YouTubeSingleVideoResponseSchema,
   
)

blp = Blueprint("Youtube" , "youtube" ,url_prefix = "/api/youtube", description = "Youtube Sentiment Analysis")


@blp.route("/by-url/analyze")
class YoutubeByUrl(MethodView) :
    @blp.arguments(YoutubeByUrlRequestSchema)
    @blp.response(200, YouTubeSingleVideoResponseSchema)
    def post(self , request_data) :
        raw_url = request_data["video_url"]
        video_url = extract_video_id(raw_url)
        if not video_url :
            abort(400, message = "Invalid Youtube video Id or link")
        return analyze_comments(video_url , count = 10)
    


@blp.route("/by-keyword/analyze")
class YouTubeByKeyword(MethodView):
    @blp.arguments(YouTubeByKeywordRequestSchema)
    @blp.response(200, YouTubeSingleVideoResponseSchema)
    def post(self, data):
        keyword = data["keyword"]
        count = data.get("count", 10)
        try:
            video_id = search_video_by_keyword(keyword)
            return analyze_comments(video_id, count)
        except Exception as e:
            abort(500, message=f"Search failed: {str(e)}")

@blp.route("/by-keyword/multi/analyze")
class YouTubeByKeywordMulti(MethodView):
    @blp.arguments(YouTubeMultiKeywordRequestSchema)
    @blp.response(200, YouTubeSingleVideoResponseSchema(many=True))
    def post(self, data):
        keyword = data["keyword"]
        max_videos = data.get("max_videos", 3)
        comments_per_video = data.get("comments_per_video", 10)

        results = analyze_comments_for_multiple_videos(keyword, max_videos, comments_per_video)
        return results