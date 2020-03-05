from flask import Blueprint, request, jsonify
from models import db, Movie, Actor
import datetime
import utils
import auth
import errors


actor_blueprint = Blueprint('actor', __name__)


@auth.requires_auth('create:actor')
@actor_blueprint.route('/actors', methods=['POST'])
def create_actor():
    pass


@auth.requires_auth('read:actor')
@actor_blueprint.route('/actors')
def get_actors():
    pass


@auth.requires_auth('read:actor')
@actor_blueprint.route('/actors/<int:actor_id>')
def get_actor(actor_id):
    pass


@auth.requires_auth('update:actor')
@actor_blueprint.route('/actors/<int:actor_id>', methods=['PATCH'])
def patch_actor(actor_id):
    pass


@auth.requires_auth('delete:actor')
@actor_blueprint.route('/actors/<int:actor_id>', methods=['PATCH'])
def delete_actor(actor_id):
    pass
