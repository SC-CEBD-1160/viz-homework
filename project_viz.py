import os

import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('data/wine.data',
                 sep=',',
                 header=0)

df.columns = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids',
              'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280 od315_of_diluted_wines',
              'proline']


os.makedirs('plots', exist_ok=True)

plt.style.use("ggplot")

fig, axes = plt.subplots(1, 1, figsize=(5, 5))

# This time we plot multiple plots on the same axes, to get some perspective on their comparisons
# The size parameter can be either a fixed value or another columns as in here
axes.scatter(df['alcohol'], df['malic_acid'], s=(df['color_intensity']) ** 2.5,
             label=f'Alcohol to Malic Acid', color='orange', marker='o', edgecolors='w', alpha=0.7)

axes.set_xlabel(f'Alcohol')
axes.set_ylabel(f'Malic Acid')
axes.set_title(f'Alcohol, Malic Acid and Color Intensity (Size)')

axes.legend()
plt.savefig(f'plots/multiplot_scatter_with_size.png', dpi=300)


os.makedirs('plots/exploration/', exist_ok=True)

# Another useful dataset exploration technique involves comparing multiple columns of the dataset
# The enumerate functions will generate pairs of indexes elements
for col1_idx, column1 in enumerate(df.columns):
    for col2_idx, column2 in enumerate(df.columns):
        if col1_idx < col2_idx:
            print(f'Generating {column1} to {column2} plot')
            fig, axes = plt.subplots(1, 1, figsize=(5, 5))
            axes.scatter(df[column1], df[column2], label=f'{column1} to {column2}', color='green', marker='x')
            axes.set_title(f'{column1} to {column2}')
            axes.set_xlabel(column1)
            axes.set_ylabel(column2)
            axes.legend()
            plt.savefig(f'plots/exploration/wine_{column1}_{column2}_scatter.png', dpi=300)
            plt.close(fig)

plt.close()
