"""
Execute this script every time you wanna make a migration to the database
"""
from pony.orm import Database, Required, PrimaryKey

db = Database()


# Set the models
class Movie(db.Entity):
    id = PrimaryKey(int, auto=True)
    tittle = Required(str)
    overview = Required(str)
    poster_path = Required(str)
    date = Required(int)
    vote_average = Required(float)
    vote_count = Required(int)