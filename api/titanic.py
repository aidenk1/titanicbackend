from flask import Blueprint, jsonify, request
from titanic_model import predict_survival  # Import the function for predicting survival from the Titanic model

titanic_api = Blueprint('titanic_api', __name__, url_prefix='/api/titanic')

@titanic_api.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if data is None:
        return jsonify({'error': 'No data provided'}), 400
    
    # Assuming predict_survival function takes the necessary data and returns the prediction
    prediction = predict_survival(data)

    return jsonify({'prediction': prediction}), 200
