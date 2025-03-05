import pandas as pd
import numpy as np
import dask.dataframe as dd


# Read the CSV files into Pandas and Dask DataFrames
TripsFullDataPandas = pd.read_csv('./DataSources/TripsFullData.csv')
TripsByDistancePandas = pd.read_csv('./DataSources/TripsByDistance.csv')
TripsFullDataDask = dd.read_csv('./DataSources/TripsFullData.csv')
TripsByDistanceDask = dd.read_csv('./DataSources/TripsByDistance.csv')
