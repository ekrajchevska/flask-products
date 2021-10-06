from jose import jwt, JWTError
from .exceptions import InvalidAPIUsage
from functools import wraps
from flask import request, jsonify
import os


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if "x-access-tokens" in request.headers:
            token = request.headers["x-access-tokens"]

        if not token:
            return jsonify({"message": "A valid token is missing"})

        try:
            validate_access_token(token)
        except:
            return jsonify({"message": "Token is invalid"})

    return decorator


def validate_access_token(token: str):
    try:
        payload = jwt.decode(
            token, os.getenv("secret"), algorithms=[os.getenv("algorithm")]
        )
        email: str = payload.get("email")
        if email is None:
            raise InvalidAPIUsage("Invalid token!", 401)

    except JWTError:
        raise InvalidAPIUsage("Not authorized!", 401)

    return email
