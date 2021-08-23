import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

flights_data = pd.read_csv('flights_data.csv', low_memory=False)

# adding new column 'hour'

flights_data.dropna(subset=['dep_time', 'air_time'], inplace=True)
flights_data['hour'] = flights_data['dep_time'].floordiv(100).astype(int)

# adding new column 'flight_length'
# 1 for Short-Haul from 30 minutes to 3 hours
# 2 for Medium-Haul 3-6 hours
# 3 for Long-Haul over 6 hours
flights_data['flight_length'] = flights_data['air_time'].copy()
flights_data['flight_length'].mask(flights_data['flight_length'] < 180, 1, inplace=True)
flights_data['flight_length'].mask((flights_data['flight_length'] >= 180) & (flights_data['flight_length'] < 360), 2, inplace=True)
flights_data['flight_length'].mask(flights_data['flight_length'] >= 360, 3, inplace=True)

df_8 = flights_data[['flight_length', 'hour']].copy()

print(df_8[df_8['flight_length'] == 1.].mode())
print(df_8[df_8['flight_length'] == 2.].mode())
print(df_8[df_8['flight_length'] == 3.].mode())
    # mode()