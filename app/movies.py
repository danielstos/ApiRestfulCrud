from flask import Blueprint,current_app,request
from .model import Movie
from .serealizer import MovieSchema

bp_movies = Blueprint('movies', __name__)

@bp_movies.route('/mostrar', methods=['GET'])
def mostrar():
    ms = MovieSchema(many=True)
    result = Movie.query.all()
    return ms.jsonify(result),200

@bp_movies.route('/deletar', methods=['GET'])

def deletar():
    ...

@bp_movies.route('/modificar', methods=['POST'])

def modificar():
    ...

@bp_movies.route('/cadastrar', methods=['POST'])

def cadastrar():
    ms = MovieSchema()
    movie,error = ms.load(request.json)
    current_app.db.session.add(movie)
    current_app.db.session.commit()
    return ms.jsonify(movie), 201