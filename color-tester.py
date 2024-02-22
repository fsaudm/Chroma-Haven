
import matplotlib.pyplot as plt
import numpy as np

# Define function to convert hex color to RGB
def hex_rgb(hex_color):
    """
    Convert a hex color string to an RGB tuple.

    Parameters:
    - hex_color: A string representing a hex color, e.g., '9CA1B3'

    Returns:
    - A tuple of integers representing the RGB values, e.g., (156, 161, 179)
    """
    hex_color = hex_color.lstrip('#')  # Remove '#' if it's there
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Define color palettes
monochroma_hex = ['9CA1B3', 'CFD1FA', 'EBECEF', '58586F']
redblue_hex = ['F01159', 'DFF8FE', '82CDE5', '003458']

# User input
# ==============================================================================
colors_hex = redblue_hex
# ==============================================================================

# Transforming colors to RGB
colors_rgb = [hex_rgb(color) for color in colors_hex]

# ______________________________________________________
# Visualizations

# Generate random data for visualization
np.random.seed(0)  # For reproducibility
data = np.random.rand(4, 8)  # Generate 4 datasets
markers = ['o', 'o', 'o', 'o']

# Create line plot with markers
plt.figure(figsize=(4, 3), dpi=300)
for i in range(data.shape[0]):
    plt.plot(data[i], marker=markers[i], linestyle='-', color=[c/255. for c in colors_rgb[i]], 
             markeredgecolor='black', markeredgewidth=0.5, markersize=5, label=f'D{i+1}', )
plt.title('Line Plot', fontweight=str('bold'))
plt.xlabel('X axis', fontweight=str('bold'))
plt.ylabel('Y axis', fontweight=str('bold'))
plt.legend(loc='best')
plt.show()

# Create bar chart plot with markers
fig, ax = plt.subplots(figsize=(4, 3), dpi=300)
bar_width = 0.2
index = np.arange(data.shape[1])
for i in range(data.shape[0]):
    ax.bar(index + i*bar_width, data[i], bar_width, color=[c/255. for c in colors_rgb[i]], 
           label=f'D{i+1}', edgecolor='black', linewidth=0.5)
plt.title('Bar Chart', fontweight=str('bold'))
plt.xlabel('X axis', fontweight=str('bold'))
plt.ylabel('Y axis', fontweight=str('bold'))
plt.xticks(index + bar_width, index)
plt.legend(loc='best')
plt.show()

# ______________________________________________________