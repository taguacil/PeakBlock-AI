"""
=============================================================================
Title    : Main peakblock script
Project  : PeakBlock
File     : run.py
-----------------------------------------------------------------------------

    Description:

    This file contains the main generic routines useful for any diagnosis
    algorithm


-----------------------------------------------------------------------------
Major Revisions:
    Date            Version     Name        Description
    28-Mar-2020     1.0         Ramy        First iteration of the script
"""
# Python library import
from abc import *


class MasterPredictor:
    def __init__(self, config):
        self.name = 'Generic'

    @abstractmethod
    def feature_selection(self, features):
        pass

    @abstractmethod
    def predict(self, input):
        pass

    def train(self):
        pass
