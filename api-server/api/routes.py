from api import app
import os
import pickle
import numpy as np
import json
from flask import request
from flask import jsonify


@app.route('/api')
@app.route('/')
def api_home():
    return 'Hello from ml api!'

@app.route('/api/ml', methods=['POST'])
def model_prediction():
    record = json.loads(request.data)['data']

    with open(app.config['MODEL_PATH'], 'rb') as p:
        model = pickle.load(p)

    data = np.array(record)
    predictions = model.predict(data)
    
    return jsonify(str(predictions))
