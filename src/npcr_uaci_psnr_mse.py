# NPCR Calculation
def calculate_npcr(img1, img2):
    return np.sum(img1 != img2) / img1.size * 100

# UACI Calculation
def calculate_uaci(img1, img2):
    diff = np.abs(img1.astype(np.int32) - img2.astype(np.int32))
    return np.mean(diff / 255.0) * 100

# PSNR and MSE Calculation
def calculate_psnr(img1, img2):
    mse = np.mean((img1.astype(np.float32) - img2.astype(np.float32)) ** 2)
    if mse == 0:
        return float('inf'), 0
    psnr = 10 * log10((255.0 ** 2) / mse)
    return psnr, mse

# Wrapper to evaluate all metrics
def evaluate_encryption_metrics(original_img, encrypted_img):
    if original_img.ndim == 3:  # Color image
        npcr_total, uaci_total, psnr_total, mse_total = 0, 0, 0, 0
        for c in range(3):
            npcr = calculate_npcr(original_img[:, :, c], encrypted_img[:, :, c])
            uaci = calculate_uaci(original_img[:, :, c], encrypted_img[:, :, c])
            psnr, mse = calculate_psnr(original_img[:, :, c], encrypted_img[:, :, c])

            print(f"Channel {c} - NPCR: {npcr:.2f}%, UACI: {uaci:.2f}%, PSNR: {psnr:.2f} dB, MSE: {mse:.2f}")

            npcr_total += npcr
            uaci_total += uaci
            psnr_total += psnr
            mse_total += mse

        print(f"Average - NPCR: {npcr_total/3:.2f}%, UACI: {uaci_total/3:.2f}%, PSNR: {psnr_total/3:.2f} dB, MSE: {mse_total/3:.2f}")

    else:  # Grayscale image
        npcr = calculate_npcr(original_img, encrypted_img)
        uaci = calculate_uaci(original_img, encrypted_img)
        psnr, mse = calculate_psnr(original_img, encrypted_img)

        print(f"NPCR: {npcr:.2f}%, UACI: {uaci:.2f}%, PSNR: {psnr:.2f} dB, MSE: {mse:.2f}")


evaluate_encryption_metrics(original_img, encrypted_img)
