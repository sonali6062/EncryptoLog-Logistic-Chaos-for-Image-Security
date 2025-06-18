# Load and prepare image
#img=plt.imread("peppers.jpg")
img=data.astronaut()
#img = cv2.resize(img, (256, 256))  # Optional: Resize for consistency
original_img = img.copy()

# Flatten the image for encryption
flat_img = img.flatten()

# Key generation
x0 = 0.7
r = 3.59
key = logistic_map_key(x0, r, flat_img.size)

print(key[:20])

# Encryption using XOR
encrypted_flat = np.bitwise_xor(flat_img, key)
encrypted_img = encrypted_flat.reshape(img.shape)

# Show original image
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')
# Show encrypted image
plt.subplot(1, 2, 2)
plt.title("Encrypted Image")
plt.imshow(encrypted_img, cmap='gray')
plt.axis('off')
plt.show()
