import threading
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

from __init__ import app, db, cors

from api.titanic import titanic_api
from api.nba import NBA_api

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Register URIs
app.register_blueprint(titanic_api)
app.register_blueprint(NBA_api)

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
    app.run(host='0.0.0.0', port="8086")
