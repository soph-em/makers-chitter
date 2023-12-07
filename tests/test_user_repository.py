from lib.user_repository import *
from lib.user import *


def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/chitter.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new BookRepository

    users = repository.all() # Get all books

    # Assert on the results
    assert users == [
        User(1, "username", "display name", "email", "Password"),
    ]

def test_create_user(db_connection):
    db_connection.seed("seeds/test_chitter.sql")
    repository = UserRepository(db_connection)

    created_peep = repository.create(User(None, "Test username", "Test display" , "Test email", "Test Password"))
    # assert created_peep == Peep(2, "Test Content", "07-12-2023" ,1)

    result = repository.all()
    assert result == [
        User(1, "Test", "Test Display", "Test email", "Password"),
        User(2, "Test username", "Test display" , "Test email", "Test Password")
    ]
    #struggle to get this test passing because of hashed password