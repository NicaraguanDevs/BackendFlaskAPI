from pony.orm import Database, Required, PrimaryKey, StrArray, LongStr

db = Database()


# Set the models
class Movie(db.Entity):
    adult = Required(bool)
    id = PrimaryKey(int, auto=True)
    genres = Required(StrArray)
    tittle = Required(str)
    overview = Required(LongStr)
    poster_path = Required(str)
    release_date = Required(int)
    vote_average = Required(float)
    vote_count = Required(int)
    original_language = Required(str)
    original_title = Required(str)
    popularity = Required(int)


class Genre(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
