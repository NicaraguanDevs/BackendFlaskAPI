from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from pony.flask import Pony
from controllers import HelloWorld

from config import config

# Create the application
app = Flask(__name__)

# Import the config to connect the database
app.config.update(config)

# Allow Cross Origin Policy
CORS(app)

# Make pony the default ORM
Pony(app)

# Create the API
api = Api(app)

api.add_resource(HelloWorld,
                 '/',
                 '/hello')
