# Logistic Map Key Generator
def logistic_map_key(x0, r, size):
    key = np.zeros(size)
    key[0] = x0
    for i in range(1, size):
        key[i] = r * key[i - 1] * (1 - key[i - 1])
    return (np.floor(key * 1e14) % 256).astype(np.uint8)  # Scale and convert to uint8
