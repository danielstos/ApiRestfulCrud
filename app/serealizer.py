from flask_marshmallow import Marshmallow
from .model import Movie

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class MovieSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
         model = Movie