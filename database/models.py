from utils.helper import create_token
from psycopg2.extras import RealDictCursor
import hashlib


class User:

    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    # return token or False by login and password
    def login(self, email, password):
        with self.conn.cursor() as cursor:
            cursor.execute(
                """SELECT * FROM users WHERE email = '{0}' AND password = '{1}' LIMIT 1""".format(
                    email, hashlib.md5(password.encode()).hexdigest()))
            tmp = cursor.fetchone()
            return self.serialize(tmp, public=False)

    def create_account(self, username, email, password) -> bool:
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    """insert into users (username, email, password) values('{0}', '{1}', '{2}')"""
                        .format(username, email, hashlib.md5(password.encode()).hexdigest()))
                self.conn.commit()
                return True
            except Exception:
                return False

    def get(self, user_id=None, email=None, username=None, LIMIT=1, PUBLIC=False):
        with self.conn.cursor() as cursor:
            if user_id is not None:
                pass
            elif email is not None:
                cursor.execute(
                    """SELECT * FROM users WHERE email = '{0}' LIMIT {1}""".format(email, LIMIT))
                tmp = cursor.fetchall()
                return self.serialize(many=tmp, public=PUBLIC)
            elif username is not None:
                pass
            return None

    @staticmethod
    def serialize(one=None, many=None, public=False):
        if one is not None:
            return {"user_id": one[0] if public else -1, "name": one[1], "email": one[2],
                    "password": one[3] if public else ''}
        elif many is not None:
            result = []
            for user in many:
                result.append(User.serialize(one=user, public=public))
            return result
        return None
