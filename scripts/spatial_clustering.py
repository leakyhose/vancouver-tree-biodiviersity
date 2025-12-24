import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import shape
import json
import hdbscan

from species_effective_count import effective_species_count

df = pd.read_csv("./data/public-trees.csv", sep=";")

df["geom"] = df["geom"].apply(lambda x: shape(json.loads(x)))
gdf = gpd.GeoDataFrame(df, geometry="geom", crs="EPSG:4326")
gdf = gdf.to_crs("EPSG:32610")

coords = np.array([[geom.x, geom.y] for geom in gdf.geometry])

clusterer = hdbscan.HDBSCAN(min_cluster_size=30, min_samples=10, cluster_selection_epsilon=10, cluster_selection_method='eom', metric='manhattan')
labels = clusterer.fit(coords).labels_

gdf['cluster'] = labels

# Simple visualization, delete later
mask = gdf['cluster'] != -1
filtered = gdf[mask]

plt.scatter(
    filtered.geometry.x,
    filtered.geometry.y,
    c=filtered['cluster'],
    cmap='tab20',
    s=10,
    alpha=0.6
)

plt.show()


# For each cluster, calculate effective species count

