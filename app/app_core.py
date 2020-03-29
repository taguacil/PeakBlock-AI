"""
=============================================================================
Title    : Main webservice script
Project  : PeakBlock
File     : app_core.py
-----------------------------------------------------------------------------

    Description:

    This file contains the flask webservice


-----------------------------------------------------------------------------
Major Revisions:
    Date            Version     Name        Description
    28-Mar-2020     1.0         Taimir        First iteration of the script
"""
# Python library import
from sanic import response

from app.app_settings import URL_BASE
from app.app_settings import app_endpoints

# User-defined library import
from diagnosis.diagnosis_algorithms.naive_bayes import PredictorClass

_endpoint_route = lambda x: app_endpoints.route(URL_BASE + x, methods=['GET', 'POST'])

@_endpoint_route('/home')
def _home(request):
    return response.html('<p>Hello world!</p>')

@_endpoint_route('/diagnosis')
def _diagnosis(request):
    config = {
        'model_type': 'naive_bayes',
        'model_hyperparams': {},
    }
    diagnoser = PredictorClass({})
    features = diagnoser.process_api_data(request.json)
    prob = diagnoser.predict(features)
    output = {"COVID Probability": prob}
    print(type(request.json))
    return response.json(output)
