"""
=============================================================================
Title    : Main peakblock script
Project  : PeakBlock
File     : run.py
-----------------------------------------------------------------------------

    Description:

    This file contains the main routines for a naive bayesian inference
    of probability of COVID 19 diagnosis given a set of features


-----------------------------------------------------------------------------
Major Revisions:
    Date            Version     Name        Description
    28-Mar-2020     1.0         Ramy        First iteration of the script
"""

# Python library import
import numpy as np
import pandas as pd
from abc import *

# User-defined library import
from .generic_algorithm import MasterPredictor

likelihoods = {
    'dry_cough': 0.99,
    'fever': 0.5,
    'difficulty_breathing': 0.99
}

likelihoodsc = {
    'dry_cough': 0.02,
    'fever': 0.01,
    'difficulty_breathing': 0.005
}


def bayes_estimator(features, likelihoods, likelihoodsc):
    prior = features['prior']
    probability = prior
    priorc = 1-prior
    numerator = 1
    product = 1
    product_c = 1
    for name, feature in features.items():
        if name == "prior":
            pass
        else:
            if feature:
                numerator *= likelihoods[name]
            else:
                numerator *= (1-likelihoods[name])
            product *= likelihoods[name]
            product_c *= likelihoodsc[name]

    denominator = prior*product + priorc*product_c
    probability *= numerator/denominator
    return probability


class PredictorClass(MasterPredictor):
    def __init__(self, config):
        super(PredictorClass, self).__init__(config)
        self.name = 'Naive Bayes'
        self.hyperparameters = {
        }

    def feature_selection(self, features):
        """
        Any feature preprocessing can be done here if desired
        :param features: Pandas dataframe
        :return:
        """
        return features

    def predict(self, input):
        probabilities = input.apply(lambda x: bayes_estimator(x, likelihoods, likelihoodsc), axis=1)
        return probabilities



