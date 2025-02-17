import hashlib
import jwt
import datetime
from flask import Flask, abort
from config import getconnection, SECRET_KEY
# These functions need to be implemented
class Token:

    def generate_token(self, username, password):
        self.username = username
        self.password = password
        user = None
        query = "SELECT username, password, salt, role FROM users WHERE username = %s"
        
        try:
            conn = getconnection()
            with conn.cursor() as cursor:
                cursor.execute(query, username)
                user = cursor.fetchone()

            for row in user:
                dbuser = user[0]
                dbpass = user[1]
                dbsalt = user[2]
                dbrole = user[3]
            
            hash = hashlib.sha512( str( password ).encode("utf-8") + str( dbsalt ).encode("utf-8") ).hexdigest()
            
            if hash == dbpass :
                token = jwt.encode({
                    'username': dbuser,
                    'role': dbrole,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
                }, SECRET_KEY,'HS256')

                conn.close()
                return token
            else :
                return abort(403)
        except :
            return abort(403, description="Incorrect Credentials")

class Restricted:

    def access_data(self, authorization):
        try:
            decodetoken= jwt.decode(authorization,SECRET_KEY, algorithms=["HS256"])
            return "You are under protected data"
        except jwt.DecodeError:
            return "Invalid Token"
        except jwt.ExpiredSignature:
            return "Token Expired"