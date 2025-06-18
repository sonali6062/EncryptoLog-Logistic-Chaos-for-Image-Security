def calculate_entropy_from_array(img_array):
    def entropy(channel_data):
        flat = channel_data.flatten()
        counts = Counter(flat)
        total = len(flat)
        return -sum((count / total) * math.log2(count / total) for count in counts.values())

    if img_array.ndim == 2:  # Grayscale image
        ent = entropy(img_array)
        print(f"Entropy: {ent:.4f} bits")
    elif img_array.ndim == 3 and img_array.shape[2] == 3:  # RGB image
        r_ent = entropy(img_array[:, :, 0])
        g_ent = entropy(img_array[:, :, 1])
        b_ent = entropy(img_array[:, :, 2])
        print(f"Red Channel Entropy   : {r_ent:.4f} bits")
        print(f"Green Channel Entropy : {g_ent:.4f} bits")
        print(f"Blue Channel Entropy  : {b_ent:.4f} bits")
        avg_ent = (r_ent + g_ent + b_ent) / 3
        print(f"Average Entropy       : {avg_ent:.4f} bits")
    else:
        raise ValueError("Unsupported image format")

# After XOR encryption:
# encrypted_img = encrypted_flat.reshape(img.shape)
calculate_entropy_from_array(encrypted_img)
