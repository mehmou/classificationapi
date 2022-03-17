from api import app
import os
import pickle


@app.route('/api')
@app.route('/')
def api_home():
    return 'Hello from ml api!'

@app.route('/api/ml', methods=['GET'])
def model_prediction():
    model_path = os.path.join(os.getcwd(), 'api', 'models', 'model.pkl')
    with open(model_path, 'rb') as p:
        model = pickle.load(p)
        return str(model.feature_importances_)
