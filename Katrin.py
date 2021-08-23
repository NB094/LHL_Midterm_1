import pandas as pd
import numpy as np

flights_data = pd.read_csv('flights_data.csv', low_memory=False)
df_9 = flights_data[['origin', 'flights']].copy()
df_9 = df_9.groupby('origin').agg(flights_count = ('flights', 'size')).reset_index().sort_values('flights_count', ascending=False)
print(df_9[0:10])








