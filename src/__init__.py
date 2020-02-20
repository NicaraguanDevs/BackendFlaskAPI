from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from pony.orm import *
from models import db, Movie

# Create the application
app = Flask(__name__)
CORS(app)

# Create the API
api = Api(app)


@app.route("/")
def hello():
    with db_session:
        movie = Movie(tittle='Spider man', overview='This is the description',
                      poster_path='Some Stuff', date=1998, vote_average=0, vote_count=5)
    # db_insert(movie)
    return "Hello, World!"
