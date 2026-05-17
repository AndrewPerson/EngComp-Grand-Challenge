import pandas as pd
import geopandas as geo_pd

power_stations_df = pd.read_csv("data/power_stations.csv")

power_stations_df.index = power_stations_df["objectid"]
power_stations_df.drop("objectid", axis=1, inplace=True)

transmission_lines_df = pd.read_csv("data/power_stations.csv")

transmission_lines_df.index = transmission_lines_df["objectid"]
transmission_lines_df.drop("objectid", axis=1, inplace=True)

x = geo_pd.read_file("data/ASGS_2021_MAIN_STRUCTURE/ASGS_2021_Main_Structure_GDA2020.gpkg")
print(x.head())