import pandas as pd
import glob
import numpy as np

# Load and merge all CSV files
file = glob.glob('C:/Users/Ly Trung Hao/OneDrive - Charles Darwin University/Units/Software now/Assignment 2/temperatures/*.csv')
full_data = []
for filename in file:
    data_temp = pd.read_csv(filename)
    full_data.append(data_temp)

# Merge all data into one DataFrame
dataframes = pd.concat(full_data, ignore_index = True)

# Convert month columns to rows
dataframes= dataframes.set_index(['STATION_NAME','STN_ID','LAT','LON']).stack().reset_index()
dataframes.columns = ['STATION_NAME','STN_ID','LAT','LON','Month','Temp']

# Define season mapping logic
conditions = [
                dataframes['Month'].isin(['December', 'January', 'February']),
                dataframes['Month'].isin(['March','April','May']),
                dataframes['Month'].isin(['June','July','August']),
                dataframes['Month'].isin(['September','October','November']),
]
choices = ['Summer','Autumn','Winter','Spring']

# Assign 'Season' column based on logic
dataframes['Season'] = np.select(conditions,choices)

# Calculate average temperature per season
grouped = dataframes.groupby('Season')['Temp']
season_ave_temp = grouped.mean().reset_index()
season_ave_temp = season_ave_temp.iloc[[1,2,0,3]]

# Save result
with open ('average_temp.txt','w',encoding='utf-8') as f:
    for index,row in season_ave_temp.iterrows():
        f.write(f"{row['Season']}: {row['Temp']:.1f}°C\n")

# # Calculate Max, Min, and Range per station
station_stats = pd.DataFrame()
grouped = dataframes.groupby('STATION_NAME')['Temp']
station_stats['Max_Ever'] = grouped.max()
station_stats['Min_Ever'] = grouped.min()
station_stats['Range'] = station_stats['Max_Ever'] - station_stats['Min_Ever']
max_temp_range = station_stats['Range'].max()

# Export station with largest range
with open('largest_temp_range_station.txt', 'w', encoding='utf-8') as f:
    for station_name, row in station_stats.iterrows():
        if row['Range'] == max_temp_range:
            mi = row['Min_Ever']
            ma  = row['Max_Ever'] 
            f.write(f'Station {station_name}: Range {max_temp_range:.1f}°C (Max: {ma:.1f}°C, Min: {mi:.1f}°C)\n')

# Calculate stability (Standard Deviation)
station_stats['Stability']=grouped.std()
min_std = station_stats['Stability'].min()
max_std = station_stats['Stability'].max()

# Export most and least stable stations
with open('temperature_stability_stations.txt', 'w', encoding='utf-8') as f:
    for station_name,row in station_stats.iterrows():
        if row['Stability'] == min_std:
            f.write(f'Most Stable: Station {station_name}: StdDev {min_std:.1f}°C\n')
        elif row['Stability'] == max_std:
            f.write(f'Most Variable: Station {station_name}: StdDev {max_std:.1f}°C')