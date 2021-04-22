# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 00:23:23 2021

@author: Aditya Sarkar
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Bangkok_cluster.csv")
names = df['Hotels'].values
x = np.arange(len(names))
w = 0.3
plt.bar(x-w, df['score'].values, width=w, label='Initial Scores')
plt.bar(x, df['polarity_score'].values, width=w, label='Polarity Scores')
plt.xticks(x, names)
plt.ylim([0,10])
plt.tight_layout()
plt.xlabel('Bangkok Hotels Analysis')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, ncol=5)
plt.savefig("CSVBarplots.png", bbox_inches="tight")
plt.show()