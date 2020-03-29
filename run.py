"""
=============================================================================
Title    : Main peakblock script
Project  : PeakBlock
File     : run.py
-----------------------------------------------------------------------------

    Description:

    This file contains the main routines for running the models and connect to backend


-----------------------------------------------------------------------------
Major Revisions:
    Date            Version     Name        Description
    28-Mar-2020     1.0         Taimir        First iteration of the script
"""

# Python library imports
import os
import datetime
import collections
import platform
import pandas as pd
import json
import sys
import importlib
import traceback

# User-defined library import
import webapp_core

# Logger
from Utilities.logger import create_logger

logger = create_logger(__name__)

if platform.system() == "Windows":
    ident = "\\"
else:
    ident = "/"

working_dir = os.getcwd()


class PeakBlock:
    """
    Main PeakBlock object
    """

    # Constructor
    def __init__(self, input_file):
        self.port = input_file['port']

    def run(self):
        if self.port is not None and self.port <= 0:
            logger.info("Pre-initialized and pre-compiled all dependencies")
            sys.exit(0)

        logger.debug(f"Initializing on port {self.port}")
        webapp_core.run(port=self.port)


def update(dictionary, updateDict):
    """
    Generic function for updating dictionaries
    :param dictionary: old dict object
    :param updateDict: new dict object
    :return: updated dict
    """
    for k, v in updateDict.items():
        if isinstance(v, collections.Mapping):
            dictionary[k] = update(dictionary.get(k, {}), v)
        else:
            dictionary[k] = v

    return dictionary


def main():
    logger.info("Running Main()")
    param_path = working_dir + ident
    local_params = json.load(open(param_path + "Input_files" + ident + "input" + ident +
                                  "Default_config.json", "r"))

    try:
        os.stat(working_dir + ident + 'Results' + ident)
    except OSError as e:
        os.mkdir(working_dir + ident + 'Results' + ident)
        logger.error(e, exc_info=True)
    except:
        logger.error("uncaught exception: %s", traceback.format_exc())

    now = datetime.datetime.now()

    number_of_arguments = len(sys.argv)
    config_used = "Default_config.json"
    if number_of_arguments == 1:
        logger.debug("Loading config file: %s", config_used)
        pass

    elif number_of_arguments == 2:
        input_filename = sys.argv[1]  # first argument should be the parameters filename
        config_used = input_filename
        logger.debug("Loading config file: %s", config_used)
        updated_config = json.load(open(param_path + ident + input_filename,
                                        'r'))  # loads a dictionary written in a JSON file as a python dictionary
        local_params = update(local_params, updated_config)

    framework = PeakBlock(local_params)
    framework.run()


if __name__ == "__main__":
    main()
