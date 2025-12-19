import pandas as pd
import glob

file = glob.glob('C:/Users/Ly Trung Hao/OneDrive - Charles Darwin University/Units/Software now/Assignment 2/temperatures/*.csv')
full_data = []

for filename in file:
    data_temp = pd.read_csv(filename)
    full_data.append(data_temp)

dataframes = pd.concat(full_data, ignore_index = True)

seasons = {
            'Summer': ['December', 'January', 'February'], 
            'Autumn': ['March','April','May'],
            'Winter':['June','July','August'],
            'Spring':['September','October','November']
           }

with open ('average_temp.txt','w',encoding='utf-8') as f:
    for season_name, months in seasons.items():
        season_data = dataframes[months]
        avg_temp = season_data.stack().mean()
        f.write(f'{season_name}: {avg_temp:.1f}°C\n')

all_months_name = dataframes.columns[4:16]
grouped = dataframes.groupby('STATION_NAME')[all_months_name]
station_stats = pd.DataFrame()
station_stats['Max_Ever'] = grouped.max().max(axis=1)
station_stats['Min_Ever'] = grouped.min().min(axis=1)
station_stats['Range'] = station_stats['Max_Ever'] - station_stats['Min_Ever']
max_temp_range = station_stats['Range'].max()

with open('largest_temp_range_station.txt', 'w', encoding='utf-8') as f:
    for station_name, row in station_stats.iterrows():
        if row['Range'] == max_temp_range:
            mi = row['Min_Ever']
            ma  = row['Max_Ever'] 
            f.write(f'Station {station_name}: Range {max_temp_range:.1f}°C (Max: {ma:.1f}°C, Min: {mi:.1f}°C)\n')

station_stats['Stability']=grouped.mean().std(axis = 1)
min_std = station_stats['Stability'].min()
max_std = station_stats['Stability'].max()

with open('temperature_stability_stations.txt', 'w', encoding='utf-8') as f:
    for station_name,row in station_stats.iterrows():
        if row['Stability'] == min_std:
            f.write(f'Most Stable: Station {station_name}: StdDev {min_std:.1f}°C\n')
        elif row['Stability'] == max_std:
            f.write(f'Most Variable: Station {station_name}: StdDev {max_std:.1f}°C')

