import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sea


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

# phenols to flavanoids with size of color_intensity

fig, axes = plt.subplots(1, 1, figsize=(5, 5))

axes.scatter(df['total_phenols'], df['flavanoids'], s=(df['color_intensity']) ** 2.5,
             label=f'Phenols to Flavanoids', color='blue', marker='o', edgecolors='w', alpha=0.7)

axes.set_xlabel(f'Total Phenols')
axes.set_ylabel(f'Flavanoids')
axes.set_title(f'Total Phenols, Flavanoids and Color Intensity')

axes.legend()
plt.savefig(f'plots/phenols_flavanoids_scatter_with_size.png', dpi=300)


# The figsize parameter allows us to configure the figure size in inches
fig, axes = plt.subplots(2, 1, figsize=(10, 5))

# Selectively plotting the axes
axes[0].plot(df['total_phenols'])
axes[1].plot(df['color_intensity'])

axes[1].set_xlabel(f'Sample')
axes[0].set_ylabel(f'Total Phenols')
axes[0].set_title(f'Total Phenols')

axes[1].set_xlabel(f'Sample')
axes[1].set_ylabel(f'Color Intensity')
axes[1].set_title(f'Color Intensity')

plt.tight_layout()

plt.savefig('plots/2_plots_same_image.png', dpi=300)

# os.makedirs('plots/exploration/', exist_ok=True)

# Another useful dataset exploration technique involves comparing multiple columns of the dataset
# The enumerate functions will generate pairs of indexes elements
# for col1_idx, column1 in enumerate(df.columns):
#     for col2_idx, column2 in enumerate(df.columns):
#         if col1_idx < col2_idx:
#             print(f'Generating {column1} to {column2} plot')
#             fig, axes = plt.subplots(1, 1, figsize=(5, 5))
#             axes.scatter(df[column1], df[column2], label=f'{column1} to {column2}', color='green', marker='x')
#             axes.set_title(f'{column1} to {column2}')
#             axes.set_xlabel(column1)
#             axes.set_ylabel(column2)
#             axes.legend()
#             plt.savefig(f'plots/exploration/wine_{column1}_{column2}_scatter.png', dpi=300)
#             plt.close(fig)


# seaborn

# os.makedirs('plots/seaborn', exist_ok=True)
#
# sea.set()
#
# fig, ax = plt.subplots(figsize=(12,12))
# sea.heatmap(df.corr(), annot=True, cmap='winter')
# ax.set_xticklabels(df.columns, rotation=45)
# ax.set_yticklabels(df.columns, rotation=45)
# plt.savefig('plots/seaborn/wine_heatmap.png')

plt.close()
