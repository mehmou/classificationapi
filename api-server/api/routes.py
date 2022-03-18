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

    data = np.array(record)
    predictions = app.config['MODEL'].predict(data)
    
    return jsonify(str(predictions))
