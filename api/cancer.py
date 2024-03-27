from __init__ import app
from api.happy import cancer_api
from flask import Flask
from flask_cors import CORS

#Enable CORS for everything
app = Flask(__name__)
CORS(app)

app.register_blueprint(cancer_api)

#Allow all CORS headers before requests
@app.before_request
def before_request():
    allowed_origin = request.headers.get('Origin')
    if allowed_origin:
        cors._origins = "*"