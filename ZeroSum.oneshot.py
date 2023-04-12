# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 13:48:09 2023

@author: Korisnik
"""

#Import libraries
import nashpy as nash
import numpy as np

#Create a game
A = np.array([[1, -1], [-1, 1]])
matching_pennies = nash.Game(A)
matching_pennies

#Create utilities
sigma_r = np.array([1, 0])
sigma_c = np.array([1, 0])
matching_pennies[sigma_r, sigma_c]

#Check if the strategy is the best response
matching_pennies.is_best_response(sigma_r, sigma_c)