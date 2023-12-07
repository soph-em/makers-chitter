from lib.peep import *
from datetime import datetime, timezone

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
    
    
    def list_timeline_peeps(self):
        rows = self._connection.execute('SELECT peeps.id, peeps.content, peeps.post_time, users.display_name as author_name from peeps JOIN users on users.id = peeps.user_id')
        peeps = []
        for row in rows:
            formatted_post_time = datetime.fromisoformat(str(row['post_time']))
            user_friendly_format = formatted_post_time.strftime("%H:%M %d-%m-%Y")
            item = Peep(row['id'], row['content'], user_friendly_format, row['author_name'])
            peeps.append(item)

        res = peeps[::-1]
        return res
