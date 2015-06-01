"""
Gombert - readability analysis api

Get readability stats for any block of text that can be passed in

@category   Utility
@version    $ID: 1.1.1, 2015-05-30 17:00:00 CST $;
@author     KMR
@licence    http://www.wtfpl.net
"""
__version__ = "1.1.1"

#Import some stuff
import os
import yaml
import lyser

from flask import Flask, jsonify

#Work out where we are
DIR = os.path.dirname(os.path.realpath(__file__))

#Get the config
config = yaml.safe_load(open("{}/lyrer.cfg".format(DIR)))

#Get a lyser (analyser yo)
analyser = lyser.lyser(config)

#Make a Flask app
app = Flask(__name__)

#Add some routes, for the moment we have all stats, and individual stats to deal with
@app.route("/all", methods=['POST'])
def index():

    details = analyser.getAllStats(text)

    return jsonify(details)

@app.route("/method/<method>", methods=['POST'])
def index(method):
    details = analyser.getStats(method, text)

    return jsonify(details)


if config['debug']:
    app.debug = True
    app.run()
else:
    app.debug = False
    app.run(host=config['host'])
