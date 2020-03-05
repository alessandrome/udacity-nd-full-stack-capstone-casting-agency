from flask import Blueprint, request, jsonify
from models import db, Movie, Actor
import datetime
import utils
import random
import auth
import errors

actor_blueprint = Blueprint('actor', __name__)

