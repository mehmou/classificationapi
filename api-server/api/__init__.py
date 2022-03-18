from flask import Flask
from api.config import DevelopmentConfig, ProductionConfig
import os

app = Flask(__name__)

if os.environ['FLASK_ENV'] == 'production':
    print(os.environ['FLASK_ENV'])
    app.config.from_object(ProductionConfig)
elif os.environ['FLASK_ENV'] == 'development':
    print(os.environ['FLASK_ENV'])
    app.config.from_object(DevelopmentConfig)

from api import models, routes, config
