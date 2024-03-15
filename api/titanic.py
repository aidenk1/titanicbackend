from flask import Blueprint

titanic_api = Blueprint('titanic_api', __name__, url_prefix='/api/titanic')

# Define your API routes and resources here

# Example route
@titanic_api.route('/example')
def example_route():
    return {'message': 'Example route'}, 200
