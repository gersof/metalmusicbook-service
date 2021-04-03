from flask_marshmallow import Marshmallow
from flask import Flask
from flask_restplus import Api, Namespace
from flask_sqlalchemy import SQLAlchemy


class WebConfiguration:
    DB_USER_NAME = 'postgres'
    DB_NAME = 'mmbdb'
    DB_PASSWORD = 'Abc.123456'


app = Flask(__name__)


name_space = Namespace('main', description='Main APIs')

SQL_SERVER_URL = f"postgresql+psycopg2://{WebConfiguration.DB_USER_NAME}:" \
                                        f"{WebConfiguration.DB_PASSWORD}@localhost/" \
                                        f"{WebConfiguration.DB_NAME}"

app.config["SQLALCHEMY_DATABASE_URI"] = SQL_SERVER_URL

db = SQLAlchemy(app)

api = Api(app = app)


ma = Marshmallow()