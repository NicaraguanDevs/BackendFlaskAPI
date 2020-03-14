from pony.orm import Database, Required, PrimaryKey

db = Database()


class Genre(db.Entity):
    id = PrimaryKey()
    name = Required(str)
