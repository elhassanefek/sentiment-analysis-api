from marshmallow import Schema , fields 

class SentimentRequestSchema(Schema) :

    text = fields.Str(required = True) 
class SentimentResponseSchema(Schema) :

    label = fields.Str()
    confidence = fields.Float()