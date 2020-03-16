import json
import requests

from flask_restful import Resource
from flask import request
from pony.orm import *

from models import Movies, Genres

parameters = {
    "api_key": "16c54b5cc29a4cc43c2fe52d3be06784",
    "language": "es-ES",
    "page": 1,
}


class GetMovie(Resource):
    @db_session
    def get(self, Id):
        try:
            movie = Movies[Id]
        except:
            return {'status': 'Película no encontrada', 'movie': {}}, 404
        else:
            return {'status': 'Success', 'movie': movie.to_dict(with_lazy=True)}, 200


class GetPopular(Resource):
    @db_session
    def get(self):
        popular_movies = []
        try:
            page = int(request.args.get('page'))

            if page == 1:
                query = Movies.select().order_by(desc(Movies.popularity))[:20]  # 20 most popular Movies
            else:
                query = Movies.select().order_by(desc(Movies.popularity))[
                        (page - 1) * 20:page * 20]  # 20 most popular Movies

            for movie in query:
                popular_movies.append(movie.to_dict(with_lazy=True))
        except:
            return {'status': 'Pagina no encontrada'}, 404
        else:
            return {'status': 'Success', 'page': page, 'results': popular_movies}, 200


class GetMovies(Resource):
    @db_session
    def get(self):
        for i in range(500):
            parameters['page'] = i + 1
            response = requests.get(
                "https://api.themoviedb.org/3/movie/popular", params=parameters)
            movies = json.loads(response.text)
            for single_movie in movies['results']:
                try:
                    Movies(adult=single_movie['adult'],
                           id=single_movie['id'],
                           genres=single_movie['genre_ids'],
                           title=single_movie['title'],
                           overview=single_movie['overview'],
                           poster_path=single_movie['backdrop_path'],
                           release_date=single_movie['release_date'],
                           vote_average=0,
                           vote_count=0,
                           original_language=single_movie['original_language'],
                           original_title=single_movie['original_title'],
                           popularity=single_movie['popularity'])
                    print('OK')
                except:
                    print("Película saltada")

        return {'status': 'success', 'data': movies['results']}, 200


class GetGenres(Resource):
    @db_session
    def get(self):
        response = requests.get(
            'https://api.themoviedb.org/3/genre/movie/list?api_key=16c54b5cc29a4cc43c2fe52d3be06784&language=es-ES')
        genres = json.loads(response.text)
        for genre in genres['genres']:
            try:
                Genres(id=genre['id'],
                       name=genre['name'])
                print('OK' + genre['name'])
            except:
                print('Fail')
