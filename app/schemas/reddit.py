

from marshmallow import Schema , fields




class RedditRequestSchema(Schema) :
    subreddit = fields.Str(required= True)
    count = fields.Int(missing= 5, metadata = {"description" :"The number of tweets to fetch ...default 2"})

class RedditSentimentSchema(Schema) :
    text = fields.Str()
    sentiment = fields.Str()

class RedditResponseSchema(Schema) :
    subreddit = fields.Str() 
    summary = fields.Dict(
        keys = fields.Str(),
        values = fields.Int(),
        metadata = {"description" : "Counts the number of pos ,neu, neg tweets"}

    )
    comments = fields.List(fields.Nested(RedditSentimentSchema))