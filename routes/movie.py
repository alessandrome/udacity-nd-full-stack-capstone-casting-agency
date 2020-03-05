from flask import Blueprint, request, jsonify
from models import db, Movie, Actor
import datetime
import utils
import random
import auth
import errors

movie_blueprint = Blueprint('movie', __name__)
