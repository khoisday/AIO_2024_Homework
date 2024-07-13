import pandas as pd
import numpy as np

df = pd.read_csv('advertising.csv')
data = df.to_numpy()
print(np.mean(df[df["Sales"] >= 15]["Radio"]))
sum_value = df[df['Newspaper'] > df['Newspaper'].mean()]['Sales'].sum()
print(sum_value)