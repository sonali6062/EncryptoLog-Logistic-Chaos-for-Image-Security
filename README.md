
# 🔐 EncryptoLog: Logistic Chaos for Image Security

![Encryption Badge](https://img.shields.io/badge/Image%20Encryption-Chaotic%20Maps-blueviolet)

*A chaos-inspired approach to secure your images with unpredictability and precision.*

---

## 🚀 Overview

**EncryptoLog** is a Python-based image encryption and analysis project that uses the **Logistic Map**, a classic chaotic system, to generate pseudo-random keys for **secure image encryption and decryption**. The project also performs statistical evaluations like **Entropy**, **NPCR**, **UACI**, **PSNR**, and **MSE** to assess the robustness of the encryption method.

Whether you're a student, researcher, or cybersecurity enthusiast, this project offers a lightweight but powerful foundation for chaos-based image security.

---

## 🧠 Why Chaos?

> “In chaos, there is security.”

Chaotic maps like the **Logistic Map** are extremely sensitive to initial conditions, which makes them ideal for encryption. A minor change in the key can lead to entirely different encrypted images—offering strong confusion and diffusion properties.

---

## 🛠 Features

- 📷 Image Loading (from local files or built-in datasets)
- 🔑 Logistic Map Key Generation
- 🧩 Bitwise XOR Encryption & Decryption
- 📊 Histogram Analysis
- 📈 Entropy Calculation
- 📌 NPCR & UACI Evaluation
- 🎯 PSNR & MSE Computation

---

## 📊 Short Info on Evaluation Metrics

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
