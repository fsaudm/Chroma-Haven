
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

# Define color palettes (black and white)
monochroma_hex = ['9CA1B3', 'CFD1FA', 'EBECEF', '58586F']
monostyle_hex = ['444251', '8D89A3', 'E4E3E5', 'CBCBCF']
monolight_hex = ['BEBCCB', 'F1EFF2', 'DDD7DC', 'A994A7']
monodark_hex = ['56514B', 'E7E5DD', 'BDBBAD', '999990']
lima_hex = ['575965', 'C3C4C8', 'F8F8F6', '939498']


# Define color palettes (colorful)
redblue_hex = ['F01159', 'DFF8FE', '82CDE5', '003458']
tokyo_hex = ['2C3D63', 'ADDCCA', 'F7F8F3', 'FF6F5E']
berlin_hex = ['252324', 'FA3283', 'EAF7DF', '72EFD9']
santiago_hex = ['2F404F', '3894A1', 'F0F1EE', 'C7DAD3']
rio_hex = ['2C2627', 'BC2C3D', 'F8F3E6', 'EFD2BC']
bogota_hex = ['062639', 'E7301C', 'EDF4EA', 'C9D4C5']
illinois_hex = ['2E364F', '2D5D7C', 'F3F0E2', 'EF5939']

# User input
# ==============================================================================
colors_hex = illinois_hex
# ==============================================================================

# Transforming colors to RGB
colors_rgb = [hex_rgb(color) for color in colors_hex]

# ______________________________________________________
# Visualizations

# Generate random data for visualization
np.random.seed(4)  # For reproducibility
data_line = np.random.rand(4, 8)  # Generate 4 datasets
data_bar = np.random.rand(4, 4)  # Generate 4 datasets
markers = ['o', 'o', 'o', 'o']

# Create line plot with markers
plt.figure(figsize=(4, 3), dpi=300)
for i in range(data_line.shape[0]):
    plt.plot(data_line[i], marker=markers[i], linestyle='-', color=[c/255. for c in colors_rgb[i]], 
             markeredgecolor='black', markeredgewidth=0.5, markersize=5, label=f'D{i+1}', )
plt.title('Line Plot', fontweight=str('bold'))
plt.xlabel('X axis', fontweight=str('bold'))
plt.ylabel('Y axis', fontweight=str('bold'))
plt.grid(True, linestyle='--', linewidth=0.5, color='lightgray')
plt.legend(loc='best')
plt.show()

# Create bar chart plot with markers
fig, ax = plt.subplots(figsize=(4, 3), dpi=300)
bar_width = 0.2
index = np.arange(data_bar.shape[1])
for i in range(data_bar.shape[0]):
    ax.bar(index + i*bar_width, data_bar[i], bar_width, color=[c/255. for c in colors_rgb[i]], 
           label=f'D{i+1}', edgecolor='black', linewidth=0.5)
plt.title('Bar Chart', fontweight=str('bold'))
plt.xlabel('X axis', fontweight=str('bold'))
plt.ylabel('Y axis', fontweight=str('bold'))
plt.xticks(index + bar_width, index)
ax.yaxis.grid(True, linestyle='--', linewidth=0.25, color='lightgray')
plt.legend(loc='best')
plt.show()

# Create pie chart
plt.figure(figsize=(4, 3), dpi=300)
normalized_colors = [(r/255., g/255., b/255.) for (r, g, b) in colors_rgb]
slices, texts, autotexts = plt.pie([1, 2, 3, 4], colors=normalized_colors, 
                                   autopct='%1.1f%%', startangle=140, 
                                   wedgeprops={'edgecolor': 'black', 'linewidth': 0.5})

for autotext in autotexts:
    autotext.set_color('black')  # Change color to make percentage labels more visible if needed
    autotext.set_bbox(dict(facecolor='white', alpha=0.6, edgecolor='none', boxstyle='round,pad=0.2'))
    
plt.title('Pie Chart', fontweight='bold')
plt.legend(slices, [f'D{i+1}' for i in range(4)], title="Datasets", loc="upper center", bbox_to_anchor=(0.50, 0.05), ncol=4)
plt. tight_layout()
plt.show()

# ______________________________________________________