from app import app
from flask import request
from .models import User, Nutrition, Diary
from werkzeug.security import check_password_hash

@app.route('/signup', methods=["POST"])
def signUpAPI():

    data = request.json

    first_name = data['first_name']
    last_name = data['last_name']
    username = data['username']
    email = data['email']
    password = data['password']

    u1 = User.query.filter_by(username=username).first()
    u2 = User.query.filter_by(email=email).first()

    if u1 and u2:
        return{
            'status': 'not ok',
            'message': 'Username AND email already exist'
        }
    elif u1:
        return{
            'status': 'not ok',
            'message': 'Username already exists'
        }
    elif u2:
        return{
            'status': 'not ok',
            'message': 'Email already exists'
        }
    else:
        user = User(first_name, last_name, username, email, password)
        user.saveToDB()

        return{
            'status': 'ok',
            'message': 'Succesfully created account!'
        }

@app.route('/login', methods=["POST"])
def logMeInAPI():
    data = request.json
    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    if user:
        if check_password_hash(user.password, password):
            return {
            'status': 'ok',
            'message': f'Successfully logged in. Welcome back, {user.username}!',
            'user': user.to_dict()
        }
        else:
            return {
            'status': 'not ok',
            'message': 'Incorrect password...'
        }
    else:
        return {
            'status': 'not ok',
            'message': 'User does not exist...'
        }

@app.route('/diary', methods=["GET"])
def getDiary():
    pass