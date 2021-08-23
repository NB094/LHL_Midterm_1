import pandas as pd
import numpy as np

passengers_all_car = pd.read_csv('passengers_all_2019.csv')
flights_data_car = pd.read_csv('flights_data_all_2019_Months.csv')
fuel_car = pd.read_csv('fuel_comsumption_all_2019.csv')

#print(passengers_all[['passengers','unique_carrier', 'airline_id', 'unique_carrier_name']])

print(passengers_all_car['unique_carrier'].unique())
print(flights_data_car['op_unique_carrier'].unique())
print(fuel_car['unique_carrier'].unique())









