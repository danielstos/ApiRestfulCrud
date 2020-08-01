from marshmallow_sqlalchemy import ModelSchema
from flask_marshmallow import Marshmallow
from .model import Movie


ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class MovieSchema(ma.ModelSchema):
    class Meta:
         model = Movie