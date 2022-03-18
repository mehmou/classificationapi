import os
import pickle

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    SECRET_KEY = 'secret_key'
    DEBUG = False
    TESTING = False 
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    MODEL_PATH = os.path.join(BASE_DIR, 'models', 'model.pkl')
    with open(MODEL_PATH, 'rb') as p:
        MODEL = pickle.load(p)


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    SECRET_KEY = 'another_secret_key'
    DEBUG = False
    TESTING = False 
