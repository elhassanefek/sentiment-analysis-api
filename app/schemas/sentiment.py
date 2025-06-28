
from marshmallow import Schema, fields

class SentimentRequestSchema(Schema):
    text = fields.Str(required=True, example="I love Flask")

class SentimentResponseSchema(Schema):
    text = fields.String()
    negative = fields.Float()
    neutral= fields.Float()
    positive = fields.Float()