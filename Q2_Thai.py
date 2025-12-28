from pathlib import Path
import pandas as pd
base_direct = Path(__file__).resolve().parent
data_direct = base_direct / "temperatures"
files = sorted(data_direct.glob("stations_group_*.csv"))
identifier_cols = ["STATION_NAME", "STN_ID", "LAT", "LON", "YEAR"]
month_cols = ["January","February","March","April","May","June",
              "July","August","September","October","November","December"]
dfs = []
for f in files:
    df = pd.read_csv(f)
    df["YEAR"] = int(f.stem.split("_")[-1])
    df[month_cols] = df[month_cols].apply(pd.to_numeric, errors="coerce")
    dfs.append(df)
data = pd.concat(dfs, ignore_index=True)
print(data.shape)
data.head()
long_df = data.melt(
    id_vars = identifier_cols,
    value_vars = month_cols,
    var_name="MONTH",                   
    value_name="TEMP"                   
)
long_df.head()                          
month_to_season = {                                                             
    "December": "Summer", "January": "Summer", "February": "Summer",
    "March": "Autumn", "April": "Autumn", "May": "Autumn",
    "June": "Winter", "July": "Winter", "August": "Winter",
    "September": "Spring", "October": "Spring", "November": "Spring"
}
long_df["SEASON"] = long_df["MONTH"].map(month_to_season)
season_avg = long_df.groupby("SEASON")["TEMP"].mean().reindex(
    ["Summer", "Autumn", "Winter", "Spring"]
)
with open("average_temp.txt", "w", encoding="utf-8") as f:
    for season, avg in season_avg.items():
        f.write(f"{season}: {avg:.1f}°C\n")
station_stats = long_df.groupby("STATION_NAME")["TEMP"].agg(["min", "max"])
station_stats["range"] = station_stats["max"] - station_stats["min"]
max_range = station_stats["range"].max()
winners = station_stats[station_stats["range"] == max_range]
with open("largest_temp_range_station.txt", "w", encoding="utf-8") as f:
    for station, row in winners.iterrows():
        f.write(
            f"{station}: Range {row['range']:.1f}°C "
            f"(Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)\n"
        )
std_by_station = long_df.groupby("STATION_NAME")["TEMP"].std()
min_std = std_by_station.min()
max_std = std_by_station.max()
most_stable = std_by_station[std_by_station == min_std]
most_variable = std_by_station[std_by_station == max_std]
with open("temperature_stability_stations.txt", "w", encoding="utf-8") as f:
    f.write("Most Stable:\n")
    for station, val in most_stable.items():
        f.write(f"- {station}: StdDev {val:.1f}°C\n")

    f.write("\nMost Variable:\n")
    for station, val in most_variable.items():
        f.write(f"- {station}: StdDev {val:.1f}°C\n")
