# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 13:36:29 2023

@author: Korisnik
"""

#create a game (non-zero sum)

import nashpy as nash
import numpy as np
PlayerA = np.array([[3, 0], [5, 1]])
PlayerB = np.array([[3, 5], [0, 1]])
prisoners_dilemma = nash.Game(PlayerA, PlayerB)
print(prisoners_dilemma)

#Utility when both players are playing first

sigma_r = np.array([1, 0])
sigma_c = np.array([1, 0])
prisoners_dilemma[sigma_r, sigma_c]

#Check if the strategy best response

prisoners_dilemma.is_best_response(sigma_r, sigma_c)