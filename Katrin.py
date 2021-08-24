import pandas as pd
import numpy as np

passengers_all_car = pd.read_csv('passengers_all_2019.csv')
flights_data_car = pd.read_csv('flights_data_all_2019_Months.csv')
fuel_car = pd.read_csv('fuel_comsumption_all_2019.csv')

passengers_all_car = passengers_all_car[['passengers', 'month', 'carrier']]
passengers_all_car['carrier'] = passengers_all_car['carrier'].astype(str)

# passengers_all_car.drop(['AS' 'B6' 'AA' 'DL' 'UA' 'NK' 'WN' 'HA' 'G4' 'F9'], columns=['carrier'], inplace=True)



# # group by each month average
# passengers_all_car = passengers_all_car.groupby(['carrier', 'month']).agg(monthly_passengers = ('passengers', 'sum')).reset_index()
#
# # average monthly number of passengers that were carried by different air carriers
# passengers_all_car = passengers_all_car.groupby(['carrier']).agg(av_monthly_passengers = ('monthly_passengers', 'mean')).reset_index()
# passengers_all_car['av_monthly_passengers'] = passengers_all_car['av_monthly_passengers'].astype(int)

print(passengers_all_car[passengers_all_car['carrier'].isin(['AS', 'B6', 'AA', 'DL', 'UA', 'NK', 'WN', 'HA', 'G4', 'F9'])])










