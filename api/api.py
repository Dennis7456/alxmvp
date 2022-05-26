import time
from flask import Flask
"""
Entry point for the application
"""
app = Flask(__name__)


@app.route('/')
def index():
    return {'time': time.time()}

@app.route('/time')
def get_current_time():
    return {'time': time.time()}
