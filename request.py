import requests
import json

parameters = {
    "api_key": "16c54b5cc29a4cc43c2fe52d3be06784",
    "language": "es-es",
    "page": 1,
}

response = requests.get(
    "https://api.themoviedb.org/3/movie/popular", params=parameters)
movies = json.loads(response.text)
print(movies)
