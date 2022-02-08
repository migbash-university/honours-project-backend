# -*- coding: utf-8 -*-
# !flask/bin/Python

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~ OTHER LIBRARIES FOR PYTHON ~~~~~~~

import json
import requests
import random
import datetime
import logging
import time
# import base64
# import dns

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~ OTHER LIBRARIES FOR FLASK  ~~~~~~~

from flask import Flask
from flask import jsonify
from flask import send_file
from flask import safe_join
from flask import abort
from flask import request
from flask_restful import Api
from flask_cors import CORS

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~ OTHER LIBRARIES FOR BERT  ~~~~~~~~

from bert_env import main

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~ Init APP START ~~~~~~~~~~

app = Flask(__name__)
api = Api(app)
CORS(app)
# crontab = Crontab(app)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~ FLASK LOGGER ~~~~~~~~~~~~

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
# app.logger.setLevel(logging.INFO)
app.logger.setLevel(logging.DEBUG)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~ Declaring APP Constant Values ~~

app.config["COMPANY_LOGOS"] = './assets/company-logo'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SpaceRealm Official Custom API Endpoints
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# - /post-question;
# https://stackabuse.com/how-to-get-and-parse-http-post-body-in-flask-json-and-form-data/
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.route('/post_question', methods=['POST'])
def post_question():
    """
    Returns: JSON - response from the conversational agent;
	"""
    try:
        # ... EXTRACT DATA;
        payload_data = request.json # ... OR request.data - request.get_json()
        # ... INTERCEPT DATA;
        # context = payload_data["user_input"]
        user_response = payload_data["user_input"]
        # ... COMPUTE MODEL, and GIVE ANSWER;
        agent_response = main.trainModel_without_CUDA(user_response)
        # ... DEBUGGING;
        if app.debug:
            app.logger.info(f'{payload_data} {user_response} {agent_response}')
        # ...
        return json.dumps({'data': agent_response}, indent=4), 200

    except Exception as e:
        # ...
        return jsonify({'error': f'An Error Occured: {e}'}), 404

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#       INITIALIZE APPLICATION
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
    # ... start the application
    app.run(debug=True, threaded=True, host='0.0.0.0', port=9000)
