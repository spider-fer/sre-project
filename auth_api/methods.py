import hashlib
import jwt
import datetime
import time
from database import getconnection
# These functions need to be implemented
class Token:

    def generate_token(self, username, password):
        self.username = username
        self.password = password
        SECRET_KEY = 'my2w7wjd7yXF64FIADfJxNs1oupTGAuW'
        user = None
        query = "SELECT username, password, salt, role FROM users WHERE username = %s"

        conn = getconnection()
        with conn.cursor() as cursor:
            cursor.execute(query, username)
            user = cursor.fetchone()

        for row in user:
            dbuser = user[0]
            dbpass = user[1]
            dbsalt = user[2]
            dbrole = user[3]

        newpass = password +  dbsalt
        hash = hashlib.sha512( str( password ).encode("utf-8") + str( dbsalt ).encode("utf-8") ).hexdigest()
        # print(hash)
        token = jwt.encode({
                'username': dbuser,
                'role': dbrole,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
        }, SECRET_KEY,  algorithm='HS256')

        # decodetoken= jwt.decode(
        #         token,SECRET_KEY, algorithms=["HS256"])
        # print(token)
        # print("Decode",decodetoken)

        conn.close()
        return token


class Restricted:

    def access_data(self, authorization):
        return 'test'
