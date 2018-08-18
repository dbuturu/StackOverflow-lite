from flask import Blueprint, jsonify, make_response, abort, request
from .question.model import QuestionModel
from .user.model import UserModel

user = UserModel({})
question = QuestionModel({})

mod = Blueprint('api', __name__)

@mod.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "no item found"}), 404)


@mod.route('/user/<username>')
def get_user(username):
    users = user.read(username)
    if users:
        return jsonify({"user": users})
    abort(404)
