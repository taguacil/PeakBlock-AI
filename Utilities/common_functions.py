"""
=============================================================================
Title    : Common functions for the framework
Project  : PeakBlock
File     : common_functions.py
-----------------------------------------------------------------------------

    Description:

    This file contains the common generic functions and utilities that are
    useful in running the framework


-----------------------------------------------------------------------------
Major Revisions:
    Date            Version     Name        Description
    28-Mar-2020     1.0         Ramy        First iteration of the script
"""
# Python library import
import collections


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