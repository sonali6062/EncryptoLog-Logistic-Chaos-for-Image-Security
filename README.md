
# 📂 EncryptoLog: Logistic Chaos for Image Security

EncryptoLog is a lightweight yet highly effective image encryption system leveraging the chaotic behavior of the **Logistic Map**. It demonstrates the power of chaos theory to achieve high security, sensitivity, and randomness in image encryption.

---

## 🚀 Features
- 🔒 **Chaotic Logistic Map-Based Encryption**
- 🖼️ Supports both **grayscale and color images**
- 📊 Robust security metrics: NPCR, UACI, PSNR, MSE, and Entropy
- ⚙️ Simple, efficient, and suitable for real-time applications
- 🔑 Key-dependent encryption ensures strong protection

---

## 📚 Project Structure
- `Image Encryption Using Logistic Map Dynamics.ipynb` - Full implementation with step-by-step explanation
- 📊 Performance evaluations across multiple standard images

---

- **NPCR (Number of Pixel Change Rate):**  
  Measures the percentage of different pixel values between the original and encrypted images.  
  *Higher NPCR indicates better sensitivity and stronger encryption.*

- **UACI (Unified Average Changing Intensity):**  
  Measures the average intensity difference between the original and encrypted images.  
  *Higher UACI shows a stronger ability to significantly alter pixel intensities.*

- **PSNR (Peak Signal-to-Noise Ratio):**  
  Evaluates the quality of the decrypted image compared to the original image.  
  *Higher PSNR indicates better image recovery (lower distortion).*

- **MSE (Mean Squared Error):**  
  Quantifies the average squared difference between the original and decrypted images.  
  *Lower MSE means less error and higher decryption accuracy.*


## 📈 Encryption Metrics
- **NPCR > 99.6%**
- **UACI ~30-35%**
- **Entropy ~7.999 bits per channel**
- Strong resistance to statistical and differential attacks.

---

## 🔧 Prerequisites
```bash
pip install numpy matplotlib opencv-python
````

---

## 💻 How to Run

1. Clone the repository:

```bash
git clone https://github.com/sonali6062/EncryptoLog-Logistic-Chaos-for-Image-Security.git
```

2. Open the provided Jupyter Notebook:

```bash
Image Encryption Using Logistic Map Dynamics.ipynb
```

3. Run the cells to encrypt and decrypt images using the Logistic Map.

---

## 🌐 Future Work

This project can be **extended to:**

* 🔹 Image encryption using **higher-dimensional chaotic maps**
* 🔹 Hybrid schemes combining logistic maps with **other cryptographic techniques** (e.g., DNA coding, AES, SHA integration)
* 🔹 Real-time encrypted image transmission
* 🔹 Secure video encryption using multi-map chaotic systems

---







