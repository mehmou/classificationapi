from crypt import methods
from api import app
import os


@app.route('/api')
@app.route('/')
def api_home():
    return 'Hello from ml api!'

@app.route('/api/ml', methods=['GET'])
def model_prediction():
    model_path = os.path.split(os.getcwd())[1]
    model_path = os.path.join('.', '..', model_path)
    print(os.listdir(model_path))
    return model_path
