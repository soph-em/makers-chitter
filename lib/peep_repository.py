from lib.peep import *

class PeepRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from peeps')
        peeps = []
        for row in rows:
            item = Peep(row['id'], row['content'], row['post_time'], row['user_id'])
            peeps.append(item)
        return peeps
    
    def create(self, peep):
        rows = self._connection.execute('INSERT INTO peeps (content, post_time, user_id) VALUES (%s, %s, %s) RETURNING id', [peep.content, peep.post_time, peep.user_id])
        row = rows[0]
        peep.id = row["id"]
        return peep