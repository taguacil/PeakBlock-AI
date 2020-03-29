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
from sanic import response

from app.app_settings import URL_BASE
from app.app_settings import app_endpoints

_endpoint_route = lambda x: app_endpoints.route(URL_BASE + x, methods=['GET', 'POST'])

@_endpoint_route('/home')
def _home(request):
    return response.html('<p>Hello world!</p>')
