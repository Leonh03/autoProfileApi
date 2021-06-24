import flask
from flask import request
app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    arg = request.args['year']
    if arg == 'bozo':
        return 'Nigga'
    elif arg == 'bart':
        return 'Lief'



