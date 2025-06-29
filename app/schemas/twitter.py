from importlib import metadata
import keyword
from attr import field
from marshmallow import Schema , fields

class TwitterRequestSchema(Schema):
    keyword  = fields.Str( required=True , example = "Meta")
    count = fields.Int(missing= 5, metadata = {"description" :"The number of tweets to fetch ...default 2"})

class TweetSentimentSchema(Schema) :
    text = fields.Str()
    sentiment = fields.Str()


class TwitterResponseSchema(Schema) :
    keyword = fields.Str()
    summary = fields.Dict(
        keys = fields.Str(),
        values = fields.Int(),
        metadata = {"description" : "Counts the number of pos ,neu, neg tweets"}

    )
    tweets = fields.List(fields.Nested(TweetSentimentSchema))