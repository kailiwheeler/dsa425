
# Blue Jay data to illustrate PCA
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

#install these the usual way, for example:   pip install pandas
# or    pip3 install pandas     [MAC]
import matplotlib.pyplot as plt
df = pd.read_csv('blue_jays.csv', index_col='bird_id')
print(df.head())

import seaborn as sns
sns.scatterplot(data=df, x='bill_length_mm', y='body_mass_g', hue='sex')
plt.xlabel('Length of bill in mm')
plt.title('Relationship between bill length and body mass by sex')
plt.show()

# drop the male/female column since it isn't numerical
df_reduced = df.drop('sex', axis = 1)

# center and scale the data
df_scaled = (df_reduced - df_reduced.mean(axis=0))/(df_reduced.std(axis=0)) # You fill in this part. Normalize the entire dataframe (df_reduced) all at once in one line.

print(df_scaled.head())
# Calculate the PCA
df_pca = PCA().fit(df_scaled)
print(f"Proportion of variance explained by each principal component:\n{df_pca.explained_variance_ratio_}")

scores = df_pca.transform(df_scaled)

fig, ax = plt.subplots(figsize=(8, 8))
for i in range(df_pca.components_.shape[1]):
    ax.arrow(
        0,
        0,
        df_pca.components_[0, i],
        df_pca.components_[1, i],
        head_width=0.03,
        head_length=0.03,
        linewidth=2,
        color="red",
    )
    ax.text(
        df_pca.components_[0, i] + 0.1,
        df_pca.components_[1, i],
        df_reduced.columns[i],
        color="red",
        ha="center",
        va="center",
    )

ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
plt.show()

