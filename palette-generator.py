import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter

# Load Reference Image
user = 'johan'
filename = 'source-image.jpg'
Path = 'C:/Users/' + user + '/Box/05 Repositories/color-palette/'

# Define Functions
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

# Function to sort palette and counts
def sort_palette(palette, counts):
    palette_list = list(palette)
    sorted_indices = sorted(range(len(counts)), key=lambda i: counts[i], reverse=True)
    sorted_palette = [palette_list[i] for i in sorted_indices]
    sorted_counts = [counts[i] for i in sorted_indices]
    return sorted_palette, sorted_counts


image = Image.open(Path+filename)
image = image.convert('RGB').resize((150, 150))
pixels = np.array(image).reshape((-1, 3))

# Use k-means clustering to find the most common colors in the new image
kmeans = KMeans(n_clusters=6)
labels = kmeans.fit_predict(pixels)
palette = kmeans.cluster_centers_.astype(int)

# Count how many times each color appears in the new image
counts= Counter(labels)

# Sort the palette by frequency of appearance
sorted_palette, sorted_counts = sort_palette(palette,counts)

# Convert the RGB colors to hex
sorted_palette_hex = [rgb_to_hex(color) for color in sorted_palette]

# Plot the sorted palette
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow([sorted_palette])
plt.axis('off')
plt.title('Refined Color Palette')

# Plot the sorted counts
plt.subplot(1, 2, 2)
plt.bar(range(len(sorted_palette)), sorted_counts, color=np.array(sorted_palette) / 255)
plt.title('Color Frequency')
plt.xlabel('Colors')
plt.ylabel('Frequency')
plt.xticks([])

plt.tight_layout()
plt.show()

# The result is the sorted palette in hex format
print(sorted_palette_hex)