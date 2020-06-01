from flask import Flask, render_template
from flask_jwt_extended import JWTManager

from flask_compress import Compress

from database.database import Database
from config.config import Config

# custom app settings for REST API and frontend on vue
app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='static')

app.config.from_object(Config)
app.config['JWT_SECRET_KEY'] = 'k45fll23l4tkvka'

jwt = JWTManager(app)

Compress(app)

# Database init
db = Database()


# frontend index page
@app.route('/')
def index():
    return render_template('index.html')


# DO NOT DELETE OR MOVE ON TOP
# import routes
from routes.routes import *


# give all to vue router
@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
