from lib.user import *
import hashlib

class UserRepository():
    def __init__(self, connection):
        self._connection = connection

    def create(self, user):
        print('create method on user repository')
        binary_password = user.password.encode("utf-8")
        self.hashed_password = hashlib.sha256(binary_password).hexdigest()
        rows = self._connection.execute('INSERT INTO users (username, display_name, email, password) VALUES (%s, %s, %s, %s) RETURNING id', [user.username, user.display_name, user.email, self.hashed_password])
        row = rows[0]
        user.id = row["id"]
        return user
    
    def check_password(self, email, password_attempt):
        # Hash the password attempt
        binary_password_attempt = password_attempt.encode("utf-8")
        hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()

        # Check whether there is a user in the database with the given email
        # and a matching password hash, using a SELECT statement.
        rows = self._connection.execute(
            'SELECT * FROM users WHERE email = %s AND password = %s',
            [email, hashed_password_attempt])

        # If that SELECT finds any rows, the password is correct.
        return len(rows) > 0
    
    def find_by_email(self, email):
        rows = self._connection.execute('SELECT * from users WHERE email = %s', [email])
        for row in rows:
            user = User(row['id'], row['username'], row['display_name'], row['email'], row['password'])
        return user