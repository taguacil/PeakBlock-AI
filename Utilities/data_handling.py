"""
=============================================================================
Title    : Useful functions for general data handling
Project  : PeakBlock
File     : data_handling.py
-----------------------------------------------------------------------------

    Description:

    This file contains important functions for general data handling


-----------------------------------------------------------------------------
Major Revisions:
    Date            Version     Name        Description
    28-Mar-2020     1.0         Ramy        First iteration of the script
"""
# Python library import
from collections import OrderedDict
import pandas as pd


def fill_nan(old_data_panel, method):
    """
    fill NaN values in a pandas Panel
    :param pandas Panel, old_data_panel: pandas Panel with NaN
    :param method: string, method for filling ("ffill", "bfill", etc...)
    :return: new filled panel
    """
    new_object = OrderedDict()
    for item in old_data_panel.items:
        new_object[item] = old_data_panel[item].fillna(method=method)
    new_panel = pd.Panel(new_object)

    return new_panel
