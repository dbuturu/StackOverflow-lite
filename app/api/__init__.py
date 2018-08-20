from flask import Blueprint, jsonify, make_response, abort, request
from .question.model import QuestionModel
from .user.model import UserModel
from .answer.model import AnswerModel

user = UserModel({})
question = QuestionModel({})
answer = AnswerModel({})

mod = Blueprint('api', __name__)


@mod.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "no item found"}), 404)


@mod.route('/user/<string:username>')
def get_user(username):
    users = user.read(username)
    if users:
        return jsonify({"user": users})
    abort(404)


@mod.route('/user', methods=["POST"])
def sign_up():
    if not request.json or not request.json['username']:
        abort(400)
    new_user = {
        'username': request.json['username'],
        'name': request.json['name'],
        'password': request.json['password']
    }
    return user.sign_up(new_user)


@mod.route('/user/<string:username>', methods=["POST"])
def sign_in(username):
    validate = (
        not request.json or
        not (request.json['username'] and request.json['password']) or
        not (username == request.json['username']))
    if validate:
        abort(400)
    user.sign_in(username, request.json['password'])


@mod.route("/questions", methods=["GET"])
def get_all_question():
    if question:
        for questions in question.read_all():
            questions["answer"] = len(answer.read(questions["id"]))
        return jsonify({"questions": question.read_all()})
    abort(404)
