from pony.orm import Database, Required, PrimaryKey, StrArray, LongStr

db = Database()


# Set the models
class Movies(db.Entity):
    adult = Required(bool)
    id = PrimaryKey(int, auto=True)
    genres = Required(StrArray)
    title = Required(str)
    overview = Required(LongStr)
    poster_path = Required(str)
    release_date = Required(str)
    vote_average = Required(float)
    vote_count = Required(int)
    original_language = Required(str)
    original_title = Required(str)
    popularity = Required(float)


class Genres(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
