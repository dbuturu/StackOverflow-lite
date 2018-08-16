
from flask import Flask
from app.api import routes


app = Flask(__name__)

app.register_blueprint(routes.mod, url_prefix='/api/v1')
