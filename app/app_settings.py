"""
=============================================================================
Title    : Webservice settings
Project  : PeakBlock
File     : app_settings.py
-----------------------------------------------------------------------------

    Description:

    This file contains webservice settings


-----------------------------------------------------------------------------
Major Revisions:
    Date            Version     Name        Description
    28-Mar-2020     1.0         Taimir        First iteration of the script
"""

from sanic import Blueprint

API_VERSION = '0.1'
URL_BASE = '/api/ai'

app_endpoints = Blueprint('app_endpoints')