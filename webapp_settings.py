"""
=============================================================================
Title    : Main webapp_core script
Project  : PeakBlock
File     : web_app settings.py
-----------------------------------------------------------------------------

    Description:

    This file contains the main webapp settigns


-----------------------------------------------------------------------------
Major Revisions:
    Date            Version     Name        Description
    28-Mar-2020     1.0         Taimir        First iteration of the script
"""

import os
import sys
from Utilities.logger import create_logger, get_log_config

logger = create_logger(__name__)
log_conf = get_log_config()


def envint(varname: str, default: int) -> int:
    return int(os.getenv(varname, default))


# SERVER configuration
CONFIG_SERVER = dict(
    host=os.getenv("PEAKBLOCK_WEBSERVICE_HOST", "0.0.0.0"),
    port=envint("PEAKBLOCK_WEBSERVICE_PORT", 5050), debug=True, workers=1, log_config=log_conf,
)

# WEBAPP configuration
WEBAPP_CONFIG = dict(
    REQUEST_MAX_SIZE=envint("PEAKBLOCK_WEBSERVICE_REQUEST_MAX_SIZE", int(100 * 1e6)),  # 100 megabytes
    REQUEST_TIMEOUT=envint("PEAKBLOCK_WEBSERVICE_REQUEST_TIMEOUT", 600),  # 10 min
    KEEP_ALIVE=True,
    GRACEFUL_SHUTDOWN_TIMEOUT=envint("PEAKBLOCK_WEBSERVICE_GRACEFUL_SHUTDOWN_TIMEOUT", 3),  # 3 sec
    WEBSOCKET_MAX_SIZE=envint("PEAKBLOCK_WEBSERVICE_WEBSOCKET_MAX_SIZE", int(1e6)),  # 1 megabyte
    WEBSOCKET_MAX_QUEUE=envint("PEAKBLOCK_WEBSERVICE_WEBSOCKET_MAX_QUEUE", 32)
)
MAX_NUMBER_OF_ANSWERS = envint("PEAKBLOCK_WEBSERVICE_MAX_NUM_ANSWERS", 50)
HOSTNAME = os.getenv('PEAKBLOCK_HOSTNAME', "DEV_SERVER")

# FILE configuration
THIS_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__)))
STATIC_FOLDER = os.path.join(THIS_FOLDER, 'static')
HTML_INDEX_STATIC_FILE = os.path.join(STATIC_FOLDER, 'index.html')

MAX_SIZE_INLINE_TEXT = envint("PEAKBLOCK_WEBSERVICE_MAX_SIZE_INLINE_TEXT", int(1.5e5))  # in number of characters


