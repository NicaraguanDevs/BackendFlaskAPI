from models import db
from config import config

db.bind(config['PONY'])
db.generate_mapping(create_tables=True)
