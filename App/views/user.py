from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
from App.models import db, Word


from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
    get_all_words_json,
    start_game,
    check_word,
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')


@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/api/users')
def client_app():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/lol')
def lol():
    return 'lol'

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')

@user_views.route('/words')
def test():
    words = start_game(1)
    #words = Word.query.all()
    return render_template('test.html', words = words)
