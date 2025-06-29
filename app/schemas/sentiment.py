
from importlib import metadata
from marshmallow import Schema, fields
from sympy import Float

class SentimentRequestSchema(Schema):
    text = fields.Str(required=True, 
                      example="I love Flask",
                       metadata={"description":"Text to analyze"}
                       )

class SentimentResponseSchema(Schema):
    text = fields.String(metadata={"description" :"The original input text"})
    predictions = fields.Dict(

        keys = fields.Str(),
        values= fields.Float(),
        metadata = {"description" :"Sentiment scores (pos ,neu , neg)"}

    )
    top_label = fields.Str(required= False , metadata={"description":"Label with the highest score"})