from flask import Flask
from flask_smorest import Api, Blueprint
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    CORS(app)

    app.config["API_TITLE"] = "Sentiment Analysis API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(app)

    from app.resources.twitter import blp as TwitterBlueprint
    from app.resources.analyze import blp as SentimentBlueprint
    api.register_blueprint(SentimentBlueprint)
    api.register_blueprint(TwitterBlueprint)

    return app
