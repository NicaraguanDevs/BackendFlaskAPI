from flask_restful import Resource
from pony.orm import *
from models import Movie, Genre


class GetMovie(Resource):
    @db_session
    def get(self, Id):
        movie = Movie[Id]
        dictionary = movie.to_dict()
        return dictionary


class GetPopular(Resource):
    @staticmethod
    def get():
        return "Popular movies Here!"
