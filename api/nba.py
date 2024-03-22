import pandas as pd
import numpy as np
import sys
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder

from flask_restful import Api, Resource
from flask import Blueprint, jsonify, request
from joblib import dump, load


model = load('./api/nba_model_save.joblib')

NBA_api = Blueprint('NBA_api', __name__, url_prefix='/api/NBA')
api = Api(NBA_api)

class NBAAPI:
    class _Predict(Resource):
        def post(self):
            body = request.get_json()
            if body is not None:
                data = pd.DataFrame([body])
                above10_proba, below10_proba = np.squeeze(model.predict_proba(data))
                return {'above 10 PPG probability': below10_proba, 'below 10 PPG probability':  above10_proba}, 200
            else:
                return {'message': 'No data provided'}, 400
    
    api.add_resource(_Predict, '/predict')
