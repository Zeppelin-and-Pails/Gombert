"""
Gombert - readability analysis api

Get readability stats for any block of text that can be passed in

@category   Utility
@version    $Id: 0.1.0, 2015-06-03 13:32:04 ACST $;
@author     KMR, Jason
@licence    GNU GPL v3
"""
__version__ = "1.1.1"

#Import some stuff
import os
import yaml
import lyser

from flask import Flask, request, jsonify, abort as flask_abort

#Work out where we are
DIR = os.path.dirname(os.path.realpath(__file__))

#Get the config
config = yaml.safe_load(open("{}/gombert.cfg".format(DIR)))

#Get a lyser (analyser yo)
analyser = lyser.lyser(config)

#Make a Flask app
app = Flask(__name__)

#Add some routes, for the moment we have all stats, and individual stats to deal with
@app.route("/all", methods=['POST'])
def all():
    if request.form:
        #Get the text from the body, so we can deal with it
        text = request.form['text']
        #Deal with the text
        details = analyser.getAllStats(text)
        #Return the dict
        return jsonify(details)
    else:
        flask_abort(400)

@app.route("/method/<method>", methods=['POST'])
def method(method):
    if request.form:
        #Get the text from the body, so we can deal with it
        text = request.form['text']
        #Deal with the text
        details = analyser.getStats(method, text)
        #return the resultant dict
        return jsonify(details)
    else:
        flask_abort(400)

if config['debug']:
    app.debug = True
    app.run()
else:
    app.debug = False
    app.run(host=config['host'], port=config['port'])
