from jose import jwt, JWTError
from . import auth_env
from .exceptions import InvalidAPIUsage

SECRET_KEY = auth_env.secret
ALGORITHM = auth_env.algorithm


def validate_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        if email is None:
            raise InvalidAPIUsage("Invalid token!", 401)

    except JWTError:
        raise InvalidAPIUsage("Not authorized!", 401)

    return email
