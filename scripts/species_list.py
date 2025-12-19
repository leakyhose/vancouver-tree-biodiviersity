import pandas as pd
df = pd.read_csv("./data/public-trees.csv", sep=";")

# Count occurrences
species_counts = df["SPECIES_NAME"].value_counts().sort_values(ascending=False)

for species, count in species_counts.items():
    print(species, count)

