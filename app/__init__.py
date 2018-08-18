
from flask import Flask
from .api import mod


app = Flask(__name__)

app.register_blueprint(mod, url_prefix='/api/v1')
