from flask import Blueprint, request, jsonify
from models import db, Movie, Actor
import datetime
import utils
import auth
import errors

movie_blueprint = Blueprint('movie', __name__)


@auth.requires_auth('create:movie')
@movie_blueprint.route('/movies', methods=['POST'])
def create_movie():
    data = request.json
    movie = Movie()
    movie.title = data['title']
    movie.release_date = data['release_date']
    db.session.add(movie)
    db.session.flush()
    if 'actors' in data:
        actors = Actor.query.filter(Actor.id.in_(data['actors'])).all()
        for actor in actors:
            movie.actors.append(actor)
    db.session.commit()
    return jsonify(movie.long()), 201


@auth.requires_auth('read:movie')
@movie_blueprint.route('/movies')
def get_movies():
    max_per_page = 50
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    q = Movie.query
    search_term = request.args.get('search_term', None, str)
    if search_term:
        q = q.filter(Movie.title.ilike(search_term))
    return_movies = []
    pagination = q.paginate(page, per_page, max_per_page)
    for movie in pagination.items:
        return_movies.append(movie.short())
    return_data = {
        'items': return_movies,
        'total_items': pagination.total,
        'page': pagination.page,
        'pages': pagination.pages,
    }
    return jsonify(return_data)


@auth.requires_auth('read:movie')
@movie_blueprint.route('/movies/<int:movie_id>')
def get_movie(movie_id):
    movie = Movie.query.filter(Movie.id == movie_id).first()
    if not movie:
        return errors.not_found_error('Movie not found')
    return jsonify(movie.long())


@auth.requires_auth('update:movie')
@movie_blueprint.route('/movies/<int:movie_id>', methods=['PATCH'])
def patch_movie(movie_id):
    movie = Movie.query.filter(Movie.id == movie_id).first()
    if not movie:
        return errors.not_found_error('Movie not found')
    data = request.json
    if 'title' in data:
        movie.title = data['title']
    if 'release_date' in data:
        movie.release_date = data['release_date']
    if 'actors' in data:
        actors = Actor.query.filter(Actor.id.in_(data['actors'])).all()
        movie.actors = []
        for actor in actors:
            movie.actors.append(actor)
    db.session.commit()
    return jsonify(movie.long())


@auth.requires_auth('delete:movie')
@movie_blueprint.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    movie = Movie.query.filter(Movie.id == movie_id).first()
    if not movie:
        return errors.not_found_error('Movie not found')
    movie.delete()
    return '', 204
