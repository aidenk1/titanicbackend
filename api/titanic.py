import pandas as pd
import numpy as np

from flask_restful import Api, Resource
from flask import Blueprint, request
from joblib import load


model = load('./api/model_save.joblib')
# passenger = pd.DataFrame({
#     'pclass': [1],
#     'sex': [0],
#     'age': [5],
#     'sibsp': [0],
#     'parch': [0],
#     'fare': [512.00],
#     'alone': [0]
# })

titanic_api = Blueprint('titanic_api', __name__, url_prefix='/api/titanic')
api = Api(titanic_api)

class titanicAPI:
    class _Predict(Resource):
        def post(self):
            body = request.get_json()
            if body is not None:
                data = pd.DataFrame([body])
                dead_proba, alive_proba = np.squeeze(model.predict_proba(data))
                return {'alive_chance': alive_proba, 'dead_chance': dead_proba}, 200
            else:
                return {'message': 'No data provided'}, 400
    
    api.add_resource(_Predict, '/predict')