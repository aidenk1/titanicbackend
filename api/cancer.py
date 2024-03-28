import pandas as pd
import numpy as np

from flask_restful import Api, Resource
from flask import Blueprint, request
from joblib import load

#Load the ML model: replace the file name with whatever yours is
model = load('./api/cancer_model.joblib')

#Initialize Flask API endpoint blueprint
cancer_api = Blueprint('cancer_api', __name__, url_prefix='/api/cancer')
api = Api(cancer_api)

#Use a post request to take data from the frontend as a JSON, then return output value
class cancerAPI:
    class _Predict(Resource):
        def post(self):
            #Get data from frontend
            body = request.get_json()
            
            if body is not None:
                #Convert frontend JSON output to a pandas dataframe
                data = pd.DataFrame([body])
                data = data.rename(columns={"bareNuclei":"Bare Nuclei","epithelialCellSize":"Single Epithelial Cell Size","mitoses":"Mitoses","normalNucleoli":"Normal Nucleoli","clumpThickness":"Clump Thickness","cellSizeUniformity":"Uniformity of Cell Size","cellShapeUniformity":"Uniformity of Cell Shape"})

                #Predict and return the happiness score (model.predict returns a 1-element array so we need to take a slice)
                score = model.predict(data)[0].astype(float)
                return {'score': score}, 200
            else:
                return {'message': 'No data provided'}, 400
    
    #Add endpoint resource for this method
    api.add_resource(_Predict, '/predict')