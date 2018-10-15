from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)

try:
    username = os.environ['POSTGRES_USER']
    password = os.environ['POSTGRES_PW']
    url = os.environ['POSTGRES_URL']
    db = os.environ['POSTGRES_DB']
except KeyError:
    raise Exception('variavel .env para postgres não encontrada')

POSTGRES_URI = f'postgresql+psycopg2://{username}:{password}@{url}/{db}'
# SQLITE_URL = 'sqlite:///test.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES_URI

db = SQLAlchemy(app)

from my_app.my_module.views import home
app.register_blueprint(home)

db.create_all()