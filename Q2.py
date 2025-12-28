import pandas as pd
import numpy as np
from pathlib import Path

# Load and merge all CSV files
base_direct = Path(__file__).resolve().parent
data_direct = base_direct / "temperatures"
file = sorted(data_direct.glob("stations_group_*.csv"))
full_data = []
for filename in file:
    data_temp = pd.read_csv(filename)
    full_data.append(data_temp)

# Merge all data into one DataFrame
dataframes = pd.concat(full_data, ignore_index = True)

# Convert month columns to rows
id_cols = dataframes.columns[0:4]
month_cols = dataframes.columns[4:16]
dataframes = dataframes.melt(
    id_vars = id_cols,
    value_vars = month_cols,
    var_name="Month",                   
    value_name="Temp"                   
)

# Ignore missing values (NaN)
dataframes["Temp"] = pd.to_numeric(dataframes["Temp"], errors="coerce")
dataframes = dataframes.dropna()

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
grouped = dataframes.groupby("Season")["Temp"].mean().reindex(["Summer", "Autumn", "Winter", "Spring"])
season_ave_temp = grouped.reset_index()

# Save result
with open ('average_temp.txt','w',encoding='utf-8') as f:
    for index,row in season_ave_temp.iterrows():
        f.write(f"{row['Season']}: {row['Temp']:.1f}°C\n")

# Calculate Max, Min, and Range per station
station_stats = dataframes.groupby('STATION_NAME')['Temp'].agg(["min","max"])
station_stats['Range'] = station_stats['max'] - station_stats['min']
max_temp_range = station_stats['Range'].max()

# Export station with largest range
with open('largest_temp_range_station.txt', 'w', encoding='utf-8') as f:
    for station_name, row in station_stats.iterrows():
        if row['Range'] == max_temp_range:
            mi = row['min']
            ma  = row['max']
            f.write(f'Station {station_name}: Range {max_temp_range:.1f}°C (Max: {ma:.1f}°C, Min: {mi:.1f}°C)\n')

# Calculate stability (Standard Deviation)
grouped = dataframes.groupby('STATION_NAME')['Temp']
station_stats['Stability']=grouped.std()
min_std = station_stats['Stability'].min()
max_std = station_stats['Stability'].max()
most_stable = station_stats[station_stats['Stability'] == min_std]
most_variable = station_stats[station_stats['Stability'] == max_std]

# Export most and least stable stations
with open('temperature_stability_stations.txt', 'w', encoding='utf-8') as f:
    f.write("Most Stable:\n")
    for station_name,row in most_stable.iterrows():
        f.write(f'{station_name}: StdDev {min_std:.1f}°C\n')

    f.write("\nMost Variable:\n")
    for station_name,row in most_variable.iterrows():        
        f.write(f'{station_name}: StdDev {max_std:.1f}°C\n')