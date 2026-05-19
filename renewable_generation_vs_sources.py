from matplotlib.pylab import Axes
import matplotlib as mpl
import pandas as pd
import geopandas as geo_pd


def plot(axes: Axes, power_stations_df: geo_pd.GeoDataFrame, lga_df: geo_pd.GeoDataFrame):
    lga_df.boundary.plot(ax=axes)

    renewable_power_stations_df = power_stations_df[power_stations_df["primaryfueltype"].isin(["Water", "Wind", "Solar", "Biogas", "Biomass"])]
    renewable_power_stations_df = renewable_power_stations_df[renewable_power_stations_df["operationalstatus"] == "Operational"]

    greens = mpl.colormaps["viridis"]

    print(pd.factorize(renewable_power_stations_df["primaryfueltype"])[0] / (len(renewable_power_stations_df["primaryfueltype"].cat.categories) - 1))

    axes.scatter(
        renewable_power_stations_df["geometry"].x,
        renewable_power_stations_df["geometry"].y,
        c=greens(pd.factorize(renewable_power_stations_df["primaryfueltype"])[0] / (len(renewable_power_stations_df["primaryfueltype"].cat.categories) - 1))
    )
