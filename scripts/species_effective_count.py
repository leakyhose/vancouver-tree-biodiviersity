import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import shape
import json


def effective_species_count(species):
    counts = species.value_counts()
    p = counts / counts.sum()
    H = -(p * np.log(p)).sum()           
    effective_species = np.exp(H)        
    return effective_species

if __name__ == "__main__":
    
    df = pd.read_csv("./data/public-trees.csv", sep=";")
    df["geom"] = df["geom"].apply(lambda x: shape(json.loads(x)))
    gdf = gpd.GeoDataFrame(df, geometry="geom", crs="EPSG:4326")

    city_effective_species = effective_species_count(gdf['SPECIES_NAME'])
    print(city_effective_species)
