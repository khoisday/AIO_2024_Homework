import pandas as pd
import numpy as np

df = pd.read_csv('advertising.csv')
A = df['Sales'].mean()
scores = []
for i in df['Sales']:
    if i > A:
        scores.append('Good')
    elif i == A:
        scores.append('Average')
    else:
        scores.append('Bad')
print(scores[7:10])

mean_value = df['Sales'].mean()
arr = df.iloc[(df['Sales'] - mean_value).abs().argsort()[:1]]
A = arr['Sales'].values[0]

score = []
for i in df['Sales']:
    if i > A:
        score.append('Good')
    elif i == A:
        score.append('Average')
    else:
        score.append('Bad')
print(score[7:10])