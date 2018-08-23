
from flask import Flask, redirect
from .api import mod


app = Flask(__name__)

app.register_blueprint(mod, url_prefix='/api/v1')

@app.route('/')
def index():
    return redirect('/api/v1/questions')
