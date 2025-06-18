#Color image
# Assuming encrypted_img is your encrypted RGB image (shape: H x W x 3)
# Split the encrypted image into R, G, B channels
r_enc = encrypted_img[:, :, 0]
g_enc = encrypted_img[:, :, 1]
b_enc = encrypted_img[:, :, 2]

# Create subplots for each channel
plt.figure(figsize=(15, 4))

# Red channel histogram
plt.subplot(1, 3, 1)
plt.hist(r_enc.ravel(), bins=256, range=[0, 256], color='red')
plt.title("Red Channel - Encrypted Image")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.grid(True)

# Green channel histogram
plt.subplot(1, 3, 2)
plt.hist(g_enc.ravel(), bins=256, range=[0, 256], color='green')
plt.title("Green Channel - Encrypted Image")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.grid(True)

# Blue channel histogram
plt.subplot(1, 3, 3)
plt.hist(b_enc.ravel(), bins=256, range=[0, 256], color='blue')
plt.title("Blue Channel - Encrypted Image")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.grid(True)

plt.tight_layout()
plt.show()



#Grayscale image
plt.hist(encrypted_img.ravel(), bins=256, range=[0, 256], color='blue')
plt.title("Histogram of Encrypted Image")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
  
