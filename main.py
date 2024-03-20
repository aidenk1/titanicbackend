import threading
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

from api.titanic import titanic_api
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Define your API routes here

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8086)

# Initialize the SQLAlchemy object to work with the Flask app instance
# db.init_app(app)

# Register URIs
app.register_blueprint(titanic_api)

# Error handling for URL not found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Before request handler
@app.before_request
def before_request():
    allowed_origin = request.headers.get('Origin')
    if allowed_origin:
        cors._origins = "*"

# Run the application on the development server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8086")
