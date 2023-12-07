from lib.peep_repository import *
from lib.peep import *

# def test_all_returns_list(db_connection):
#     db_connection.seed('seeds/chitter.sql')
#     repository = PeepRepository(db_connection)
#     peeps = repository.all()
#     assert peeps == [Peep(1, "Test peep", '2023-12-06 16:52:01.774215+00', 1)]
# because timestamp includes minutes and seconds this test won't consistently pass 

def test_create_record(db_connection):
    db_connection.seed("seeds/test_chitter.sql")
    repository = PeepRepository(db_connection)

    created_peep = repository.create(Peep(None, "Test Content", "07-12-2023" ,1))
    # assert created_peep == Peep(2, "Test Content", "07-12-2023" ,1)

    result = repository.all()
    assert result == [
        Peep(1, "Test peep", "2023-12-07 16:50:10.971912+00:00", 1),
        Peep(2, "Test Content", "2023-07-12 00:00:00+01:00" ,1)
    ]