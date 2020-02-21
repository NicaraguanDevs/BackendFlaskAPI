from src import app
from models import db

if __name__ == '__main__':
    db.bind(**app.config['PONY'])
    db.generate_mapping(create_tables=True)
    app.run(debug=True)
