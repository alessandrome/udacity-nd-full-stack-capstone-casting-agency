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
    pass


@auth.requires_auth('read:movie')
@movie_blueprint.route('/movies')
def get_movies():
    pass


@auth.requires_auth('read:movie')
@movie_blueprint.route('/movies/<int:movie_id>')
def get_movie(movie_id):
    pass


@auth.requires_auth('update:movie')
@movie_blueprint.route('/movies/<int:movie_id>', methods=['PATCH'])
def patch_movie(movie_id):
    pass


@auth.requires_auth('delete:movie')
@movie_blueprint.route('/movies/<int:movie_id>', methods=['PATCH'])
def delete_movie(movie_id):
    pass
