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
    "fever": 0.83,
    "cough": 0.82,
    "pain_in_throat": 0.05,
    "dyspnea_at_rest": 0.31,
    "headache": 0.08,
    "diarrhea": 0.02,
    "nausea": 0.01,
    "muscle_ache": 0.11,
    "chest_pain": 0.02,
    "runny_nose": 0.04,
    "confusion": 0.09
}

likelihoodsc = {
    "fever": 0.005,
    "cough": 0.02,
    "pain_in_throat": 0.02,
    "dyspnea_at_rest": 0.005,
    "headache": 0.05,
    "diarrhea": 0.01,
    "nausea": 0.02,
    "muscle_ache": 0.05,
    "chest_pain": 0.01,
    "runny_nose": 0.01,
    "confusion": 0.03
}


def bayes_estimator(features, likelihoods, likelihoodsc):
    prior = features['prior']
    probability = prior
    priorc = 1-prior
    numerator = 1
    product = 1
    product_c = 1
    if features['immune']:
        return 0
    else:
        for name, feature in features.items():
            if name == "prior":
                pass
            elif name not in likelihoods.keys():
                pass
            else:
                if feature:
                    numerator *= likelihoods[name]
                    product *= likelihoods[name]
                    product_c *= likelihoodsc[name]
                else:
                    numerator *= (1-likelihoods[name])
                    product *= (1-likelihoods[name])
                    product_c *= (1-likelihoodsc[name])

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
        if type(input) is pd.DataFrame:
            probabilities = input.apply(lambda x: bayes_estimator(x, likelihoods, likelihoodsc), axis=1)
        elif type(input) is pd.Series:
            probabilities =  bayes_estimator(input, likelihoods, likelihoodsc)
        return probabilities

    def process_api_data(self, dict):
        output_series = pd.Series(dict['symptoms'])
        output_series['immune'] = dict['excorona']
        output_series['fever'] = output_series['bodyTemperature'] > 38
        output_series['prior'] = dict['confirmedCases'] / 100.0   # Total population is hard-coded just for testing

        return output_series



