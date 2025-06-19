from flask import Flask 
from flask_smorest import Api 
from resources.analyze import blp as SentimentBlueprint
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

app.config["API_TITLE"] = "Sentiment Analysis API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(SentimentBlueprint)
