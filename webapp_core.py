"""
=============================================================================
Title    : Main webapp_core script
Project  : PeakBlock
File     : webapp_core.py
-----------------------------------------------------------------------------

    Description:

    This file contains the main webapp blueprints


-----------------------------------------------------------------------------
Major Revisions:
    Date            Version     Name        Description
    28-Mar-2020     1.0         Taimir        First iteration of the script
"""

from typing import Union
from sanic import Sanic

# User-defined library import
import webapp_settings
from app.app_core import app_endpoints
from Utilities.logger import create_logger

logger = create_logger(__name__)

app = Sanic(__name__)
app.blueprint(app_endpoints)
app.static('/', file_or_directory=webapp_settings.STATIC_FOLDER)
app.static('/', file_or_directory=webapp_settings.HTML_INDEX_STATIC_FILE)

app.config.update(webapp_settings.WEBAPP_CONFIG)

logger.info(f"List of active endpoints { app.router.routes_all.keys() }")


def run(port: Union[None, int] = None):
    if port is not None:
        webapp_settings.CONFIG_SERVER['port'] = int(port)
    logger.info("Using port: %d", webapp_settings.CONFIG_SERVER['port'])
    app.config.LOGO = None
    app.run(**webapp_settings.CONFIG_SERVER)
