from flask import Blueprint,current_app,request,jsonify
from .model import Movie
from .serealizer import MovieSchema

bp_movies = Blueprint('movies', __name__)

@bp_movies.route('/mostrar', methods=['GET'])
def mostrar():
    ms = MovieSchema(many=True)
    result = Movie.query.all()
    return ms.jsonify(result),200

@bp_movies.route('/deletar/<identificador>', methods=['DELETE'])
def deletar(identificador):
    Movie.query.filter(Movie.id == identificador).delete()
    current_app.db.session.commit()
    return jsonify('Deletado!!!')

@bp_movies.route('/modificar/<identificador>', methods=['PUT'])
def modificar(identificador):
    query = Movie.query.filter(Movie.id == identificador)
    query.update(request.json)
    current_app.db.session.commit() 
    return ms.jsonify(query.first()) 

@bp_movies.route('/cadastrar', methods=['POST'])
def cadastrar():
    ms = MovieSchema()
    movie = ms.load(request.json)
    current_app.db.session.add(movie)
    current_app.db.session.commit()
    return ms.jsonify(movie), 201 