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

# alcohol to magnesium with color intensity as size
fig, axes = plt.subplots(1, 1, figsize=(5, 5))

axes.scatter(df['alcohol'], df['magnesium'], s=(df['color_intensity']) ** 2,
             label=f'alcohol to magnesium', color='red', marker='x', edgecolors='w', alpha=0.7)

axes.set_xlabel(f'Alcohol')
axes.set_ylabel(f'Magnesium')
axes.set_title(f'Alcohol, Magnesium and Color Intensity')

axes.legend()
plt.savefig(f'plots/alcohol_magnesium_scatter_with_size.png', dpi=300)

# total_phenols to proanthocyanins with color intensity as size
fig, axes = plt.subplots(1, 1, figsize=(5, 5))

axes.scatter(df['total_phenols'], df['proanthocyanins'], s=(df['color_intensity']) ** 2,
             label=f'total phenols to proanthocyanins', color='blue', marker='X', edgecolors='b', alpha=0.7)

axes.set_xlabel(f'Total Phenols')
axes.set_ylabel(f'Proanthocyanins')
axes.set_title(f'Total Phenols, Proanthocyanins and Color Intensity')

axes.legend()
plt.savefig(f'plots/total_phenols_proanthocyanins_scatter_with_size.png', dpi=300)

# total_phenols to proanthocyanins with alcohol as size
fig, axes = plt.subplots(1, 1, figsize=(5, 5))

axes.scatter(df['total_phenols'], df['proanthocyanins'], s=(df['alcohol']) ** 1.5,
             label=f'total phenols to proanthocyanins', color='grey', marker='o', edgecolors='b', alpha=0.7)

axes.set_xlabel(f'Total Phenols')
axes.set_ylabel(f'Proanthocyanins')
axes.set_title(f'Total Phenols, Proanthocyanins and Alcohol')

axes.legend()
plt.savefig(f'plots/total_phenols_proanthocyanins_scatter_with_alcohol.png', dpi=300)

# multiple plots on the same axes, to get some perspective on their comparisons
fig, axes = plt.subplots(1, 1, figsize=(5, 5))

axes.scatter(df['alcohol'], df['flavanoids'], alpha=0.7, label='Flavanoids')
axes.scatter(df['alcohol'], df['hue'], alpha=0.7, label='Hue')
axes.scatter(df['alcohol'], df['ash'], alpha=0.7, label='Ash')

axes.set_xlabel('Alcohol')
axes.set_ylabel('Flavanoids / Hue / Ash')
axes.set_title(f'Alcohol comparisons')
axes.legend()
plt.savefig(f'plots/multiplot_alcohol_flavanoids_hue_ash_scatter.png', dpi=300)

# The figsize parameter allows us to configure the figure size in inches
fig, axes = plt.subplots(2, 1, figsize=(10, 5))

# Selectively plotting the axes
axes[0].plot(df['total_phenols'])
axes[1].plot(df['color_intensity'])

axes[0].set_xlabel(f'Sample #')
axes[0].set_ylabel(f'Total Phenols')
axes[0].set_title(f'Total Phenols')

axes[1].set_xlabel(f'Sample #')
axes[1].set_ylabel(f'Color Intensity')
axes[1].set_title(f'Color Intensity')

plt.tight_layout()

plt.savefig('plots/2_plots_same_image.png', dpi=300)


# 2 plots same graph
fig, axes = plt.subplots(1, 1, figsize=(10, 5))

# When creating plots there are several parameters we can use to optimize the visualization
# https://matplotlib.org/gallery/lines_bars_and_markers/line_styles_reference.html
# https://matplotlib.org/api/markers_api.html
axes.plot(df['alcohol'], label='Alcohol', color='blue', linestyle='--', linewidth=2, alpha=0.6, marker='2')

axes.plot(df['alcalinity_of_ash'], label='Alcalinity', color='red', linestyle='dotted', linewidth=2, alpha=0.6, marker='d')
axes.set_title('Alcalinity and Alcohol Plot')
axes.set_xlabel('Sample #')
axes.set_ylabel('Index')
axes.legend()

plt.savefig('plots/alcalinity_and_Alcohol_same_plot.png', dpi=300)

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


# seaborn

os.makedirs('plots/seaborn', exist_ok=True)

sea.set()

fig, ax = plt.subplots(figsize=(20,20))
sea.heatmap(df.corr(), annot=True, cmap='winter')
ax.set_xticklabels(df.columns)
ax.set_yticklabels(df.columns)
plt.savefig('plots/seaborn/wine_heatmap.png')

plt.clf()

sea.set()

fig, ax = plt.subplots(figsize=(10,10))
sorted_by_alcohol_content_df = df.sort_values('alcohol')

sea.lineplot('alcohol', 'color_intensity', data=sorted_by_alcohol_content_df)
sea.lineplot('alcohol', 'alcalinity_of_ash', data=sorted_by_alcohol_content_df)
plt.legend(['alcohol vs color_intensity', 'alcohol vs alcalinity_of_ash'])
plt.savefig('plots/seaborn/alcohol_lineplot.png')
plt.clf()

#joint plot
for jointplot_kind in ['reg', 'hex', 'kde', 'scatter']:
    sea.jointplot('flavanoids', 'proanthocyanins', data=df, kind=jointplot_kind)
    plt.savefig(f'plots/seaborn/flavanoids_to_proanthocyanins_jointplot_{jointplot_kind}.png')
    plt.clf()

# Pairplot

sea.pairplot(df, hue='class', diag_kind='hist')
plt.savefig('plots/seaborn/wine_pairplot.png')
plt.close()
