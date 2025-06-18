#Colored image
import matplotlib.pyplot as plt
from skimage import data

# Load the sample image
img = data.astronaut()  # shape: (512, 512, 3)

# Split the image into R, G, B channels
r_channel = img[:, :, 0]
g_channel = img[:, :, 1]
b_channel = img[:, :, 2]

# Create subplots
plt.figure(figsize=(15, 4))

# Red channel histogram
plt.subplot(1, 3, 1)
plt.hist(r_channel.ravel(), bins=256, range=[0, 256], color='red')
plt.title("Red Channel Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.grid(True)

# Green channel histogram
plt.subplot(1, 3, 2)
plt.hist(g_channel.ravel(), bins=256, range=[0, 256], color='green')
plt.title("Green Channel Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.grid(True)

# Blue channel histogram
plt.subplot(1, 3, 3)
plt.hist(b_channel.ravel(), bins=256, range=[0, 256], color='blue')
plt.title("Blue Channel Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.grid(True)

# Show all plots
plt.tight_layout()
plt.show()


#GrayScale image
plt.hist(img.ravel(), bins=256, range=[0, 256], color='blue')
plt.title("Plain  Image")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()


