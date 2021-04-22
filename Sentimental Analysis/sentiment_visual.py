# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 21:58:41 2021

@author: Aditya Sarkar
"""
import plotly
import plotly.graph_objects as go
import pandas as pd
import plotly.offline as pyo
from plotly.offline import init_notebook_mode
# Read csv data
dataFrame = pd.read_csv("Bangkok_cluster.csv")
# Create initial arrays for hotels score
actual_hotel_score = list()
polarity_hotel_score = list()
base_content = list()

# Append the data to the lists

dataFrame1 = dataFrame['avg_rating']
for i in dataFrame1:
    actual_hotel_score.append(i)

dataFrame2 = dataFrame['comment_avg_rating']
for i in dataFrame2:
    polarity_hotel_score.append(i)

for i in range(1, len(dataFrame1) + 1):
    base_content.append("H" + str(i))


fig = go.Figure()
fig.add_trace(go.Bar(x=base_content,
                y = actual_hotel_score,
                name = 'Actual Score',
                marker_color='rgb(225, 119, 12)'
                ))
fig.add_trace(go.Bar(x=base_content,
                y = polarity_hotel_score,
                name = 'Polarity Score',
                marker_color='rgb(12, 15, 225)'
                ))

fig.update_layout(
    title='Bangkok Hotels Ratings Sentiment Analysis',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Ratings',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    autosize = True,
    width = 1200,
    height = 800,
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig.show()