# Generate default colormaps available in Matplotlib
# Suitable for countour plots, heatmaps, etc.

import numpy as np
import matplotlib.pyplot as plt

cmaps = plt.colormaps()
cmaps.sort()

# Creating a figure to display examples of colormaps
fig, axes = plt.subplots(nrows=len(cmaps)//10, ncols=10, figsize=(30, 32), dpi=300)
fig.subplots_adjust(top=0.98, bottom=0.02, left=0.2, right=0.99, hspace=0.3, wspace=0.1)

for ax, cmap in zip(axes.flatten(), cmaps):
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(cmap))
    ax.set_title(cmap, fontsize=16)
    ax.axis('off')

plt.tight_layout()
fig.savefig('colormaps.png', dpi=500)
plt.show()
