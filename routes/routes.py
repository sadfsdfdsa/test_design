from app import *
from flask import request

from utils.http_errors import Errors
from utils.helper import validate_params, rest

from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity, jwt_optional, create_refresh_token, jwt_refresh_token_required
)


# login by LOGIN and PASSWORD
# return token or error
# validation: login, password
@app.route('/api/v1/login/', methods=["POST"])
@jwt_optional
def login():
    current_user = get_jwt_identity()

    if current_user is None:
        data = request.json
        if not validate_params(data, 'login', 'password'):
            return rest('error', Errors.request_params_error)

        user = db.User.login(data['login'], data['password'])

        if user is None:
            return rest('error', Errors.auth_error)

        return rest('success', {"access_token": create_access_token(identity=user['email']),
                                'refresh_token': create_refresh_token(identity=user['email']),
                                'user': user
                                })
    else:
        user = db.User.get(email=current_user, PUBLIC=False)[0]
        return rest('success', {'user': user,
                                "access_token": create_access_token(identity=user['email']),
                                'refresh_token': create_refresh_token(identity=user['email'])
                                })


# refresh token
@app.route('/refresh/', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    return rest('success', {"access_token": create_access_token(identity=current_user)})


@app.route('/api/v1/signup/', methods=["POST"])
def signup():
    data = request.json

    if not validate_params(data, 'email', 'password', 'username'):
        return rest('error', Errors.request_params_error)

    success = db.User.create_account(data['username'], data['email'], data['password'])

    if success:
        return rest('success', {"access_token": create_access_token(identity=data['email']),
                                'refresh_token': create_refresh_token(identity=data['email']),
                                'user': db.User.get(email=data['email'], PUBLIC=True)[0]
                                })

    return rest('error', Errors.auth_error)


@app.route('/api/v1/user/', methods=["GET"])
@jwt_required
def get_user():
    current_user = get_jwt_identity()
    user = db.User.get(email=current_user, PUBLIC=False)
    return rest('success', user)
