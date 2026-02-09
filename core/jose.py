from jose import JWTError, jwt
from datetime import datetime, timedelta
from config import Config

class JWTHandler:

    @staticmethod
    def create_token(user_id: int):

        payload = {
            "user_id": user_id,
            "type": "access",
            "iat": datetime.now(),
            "exp": datetime.now() + timedelta(minutes=Config.PythonJose.expiration)
        }

        return jwt.encode(payload, Config.PythonJose.secret, algorithm=Config.PythonJose.algorithm)

    @staticmethod
    def decode_token(token: str) -> dict:
        try:
            payload = jwt.decode(
                token,
                Config.PythonJose.secret,
                algorithms=[Config.PythonJose.algorithm]
            )
            return payload

        except JWTError:
            raise Exception("Invalid token")