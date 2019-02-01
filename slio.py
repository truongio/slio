import requests
from functional import seq
from flask import Flask
from flask import jsonify
from flask_cors import CORS
import yaml

app = Flask(__name__)
CORS(app)

cfg = yaml.safe_load(open('config.yaml', 'r'))
key = cfg["key"]


@app.route("/")
def get_time():
    home = requests.get('http://api.sl.se/api2/realtimedeparturesV4.json?key={}&siteid=1555&timewindow=200&bus=false&train=false&metro=false&ship=false'.format(key)).json()
    work = requests.get('http://api.sl.se/api2/realtimedeparturesV4.json?key={}&siteid=9325&timewindow=200&bus=false&train=false&metro=false&ship=false'.format(key)).json()

    tramshome = home['ResponseData']['Trams']
    tramswork = work['ResponseData']['Trams']
    resulthome = seq(tramshome)\
                .filter(lambda x: x['Destination'] == 'Solna station')\
                .map(lambda x: x['DisplayTime'])\
                .take(2)\
                .to_list()

    resultwork = seq(tramswork)\
                .filter(lambda x: x['Destination'] == 'Sickla')\
                .map(lambda x: x['DisplayTime'])\
                .take(2)\
                .to_list()

    return jsonify(resulthome, resultwork)
