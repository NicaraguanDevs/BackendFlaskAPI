from flask import Flask
from pony.flask import Pony
from flask_restful import Resource
from pony.orm import *
from models import db, Movie


class HelloWorld(Resource):
    def get(self):
        with db_session:
            movie = Movie(tittle='Spider man', overview='This is the description',
                          poster_path='Some Stuff', date=1998, vote_average=0, vote_count=5)
        return "Hello, World!"
