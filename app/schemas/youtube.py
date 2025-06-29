from marshmallow import Schema , fields 


class YoutubeByUrlRequestSchema(Schema) :
    video_url  = fields.Str(required = True)


class YouTubeMultiKeywordRequestSchema(Schema):
    keyword = fields.Str(required=True, example="ai")
    max_videos = fields.Int(missing=3)
    comments_per_video = fields.Int(missing=10)


class YouTubeByKeywordRequestSchema(Schema):
    keyword = fields.Str(required=True)
    count = fields.Int(required=False, missing=10)




class YouTubeSentimentSchema(Schema):
    text = fields.Str()
    sentiment = fields.Str()


class YouTubeSingleVideoResponseSchema(Schema):
    video_id = fields.Str()
    video_url = fields.Str()
    title = fields.Str()
    summary = fields.Dict(keys=fields.Str(), values=fields.Int())
    comments = fields.List(fields.Nested(YouTubeSentimentSchema))

