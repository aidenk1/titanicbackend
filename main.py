import threading
from flask import render_template, request
from flask.cli import AppGroup
from __init__ import app, db, cors
from api.covid import covid_api
from api.joke import joke_api
from api.user import user_api
from api.player import player_api
from api.titanic import titanic_api  # Corrected import statement for titanic_api
from model.users import initUsers
from model.players import initPlayers
from projects.projects import app_projects

# Initialize the SQLAlchemy object to work with the Flask app instance
db.init_app(app)

# Register URIs
app.register_blueprint(joke_api)
app.register_blueprint(covid_api)
app.register_blueprint(user_api)
app.register_blueprint(player_api)
app.register_blueprint(titanic_api)  # Register titanic_api routes
app.register_blueprint(app_projects)

# Error handling for URL not found
@app.errorhandler(404)
def page_not_found(e):
    
    return render_template('404.html'), 404

# Default route
@app.route('/')
def index():
    return render_template("index.html")

# Route for table
@app.route('/table/')
def table():
    return render_template("table.html")

# Before request handler
@app.before_request
def before_request():
    
    allowed_origin = request.headers.get('Origin')
    if allowed_origin in ['http://localhost:4100', 'http://127.0.0.1:4100', 'https://nighthawkcoders.github.io']:
        cors._origins = allowed_origin

# Create an AppGroup for custom commands
custom_cli = AppGroup('custom', help='Custom commands')

# Command to generate data
@custom_cli.command('generate_data')
def generate_data():
    initUsers()
    initPlayers()

# Register the custom command group with the Flask application
app.cli.add_command(custom_cli)

# Run the application on the development server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8086")
