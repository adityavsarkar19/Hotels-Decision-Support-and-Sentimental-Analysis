# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 04:17:44 2021

@author: Aditya Sarkar
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Bangkok_Polarity_Coords.csv')

#Calculating the Bounding Box Values
BBox = ((df.Longitudes.min(),   df.Longitudes.max(),      
         df.Latitudes.min(), df.Latitudes.max()))
print(BBox)