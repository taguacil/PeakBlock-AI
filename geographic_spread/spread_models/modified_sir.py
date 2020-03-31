"""
=============================================================================
Title    : Main peakblock script
Project  : PeakBlock
File     : run.py
-----------------------------------------------------------------------------

    Description:

    This file contains the main routines for a modified SIR model to predict
    the geographic spread of an infection


-----------------------------------------------------------------------------
Major Revisions:
    Date            Version     Name        Description
    28-Mar-2020     1.0         Ramy        First iteration of the script
"""
# Python library import
import pandas as pd
import numpy as np


class SpreadPredictor:
    def __init__(self):
        self.name = 'sir'
        self.hyperparameters = {
            "beta" : 0.5,
            "gamma": 0.1,
            "public_trans": 0.01,
            "steps": 7
        }

    def predict_spread(self, S_pop, I_pop, R_pop, od_matrix):
        """

        :param S_pop: pd.DataFrame (1xN) containing the susceptible population at t0 in each of the N locations considered
        :param I_pop: pd.DataFrame (1xN) containing the infected population at t0 in each of the N locations considered
        :param R_pop: pd.DataFrame (1xN) containing the recovered population at t0 in each of the N locations considered
        :param od_matrix: np.array (NxN) containing the origin-destination flow matrix between the N location
        :return: latest_S, latest_I, latest_R, 3 pd.Series (N) containing the latest numbers for the susceptible,
        infected and recovered populations
        """
        # simulation parameters
        n_locations = S_pop.size
        beta = self.hyperparameters['beta']
        gamma = self.hyperparameters['gamma']
        public_trans = self.hyperparameters['public_trans']
        steps = self.hyperparameters['steps']
        beta_vec = np.random.gamma(beta, 2, n_locations)

        # initialize simulation
        S_arr = S_pop.values[0]
        I_arr = I_pop.values[0]
        R_arr = R_pop.values[0]
        N_k = S_arr + I_arr + R_arr
        normalization = od_matrix.sum(axis=1) + N_k

        # run simulation
        for time_step in range(steps):
            new_infections = (beta_vec * S_arr * I_arr / N_k) + (
                        public_trans * S_arr * np.dot(od_matrix, (I_arr * beta_vec / N_k)) / normalization)
            new_infections = np.ceil(new_infections).astype(int)
            new_infections = np.where(new_infections > S_arr, S_arr, new_infections)
            temp_S = S_arr - new_infections
            temp_I = I_arr + new_infections
            new_recovered = gamma * I_arr
            new_recovered = np.ceil(new_recovered).astype(int)
            new_recovered = np.where(new_recovered > temp_I, temp_I, new_recovered)
            temp_I = temp_I - new_recovered
            temp_R = R_arr + new_recovered
            I_arr = temp_I
            R_arr = temp_R
            S_arr = temp_S
            S_pop = S_pop.append(pd.Series(S_arr), ignore_index=True)
            I_pop = I_pop.append(pd.Series(I_arr), ignore_index=True)
            R_pop = R_pop.append(pd.Series(R_arr), ignore_index=True)

        return S_pop.iloc[-1], I_pop.iloc[-1], R_pop.iloc[-1]
