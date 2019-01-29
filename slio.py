import requests
from functional import seq
from flask import Flask
from flask import jsonify
import yaml

app = Flask(__name__)
cfg = yaml.safe_load(open('config.yaml', 'r'))
key = cfg["key"]


@app.route("/")
def get_time():
    content = requests.get('http://api.sl.se/api2/realtimedeparturesV4.json?key={}&siteid=1555&timewindow=20&bus=false&train=false&metro=false&ship=false'.format(key)).json()
    trams = content['ResponseData']['Trams']
    result = seq(trams)\
              .filter(lambda x: x['Destination'] == 'Solna station')\
              .map(lambda x: x['DisplayTime'])\
              .take(2)\
              .to_list()

    return jsonify(result)
