# 😷 Face Mask Detection using CNN

A Deep Learning project built for a college internship that detects whether a person is **wearing a face mask** or **not** using a Convolutional Neural Network (CNN).  
The project includes a trained model, Colab training notebook, and a Streamlit-based web app interface.

---

## 📸 Web App Interface

<div align="center">
  <img src="![streamlit-ui](https://github.com/user-attachments/assets/015e97b3-5cc5-43a2-a6d6-3ae79f5dabd2)
" alt="Face Mask Detection UI" width="700"/>
  <p><em>👆 Upload an image and get mask detection results in real-time</em></p>
</div>

---

## 📊 Sample Output

<div align="center">
  <img src="![ui-on-sample-data](https://github.com/user-attachments/assets/91305244-e0e2-40a3-a115-7a60d0d78ae6)
" alt="Prediction Output" width="700"/>
  <p><em>🧠 Prediction: <code>with_mask</code> | 🔍 Confidence: 98.12%</em></p>
</div>

---

## 🔗 Links

- 📦 [Dataset – Kaggle](https://www.kaggle.com/datasets/omkargurav/face-mask-dataset)  
---

## 🧠 How It Works

1. The CNN model is trained on the **Face Mask Dataset** containing two classes: `with_mask` and `without_mask`.
2. Images are resized and normalized before being passed to the network.
3. The model predicts the label and confidence based on the input image.
4. A Streamlit interface allows interactive image uploads and visual results.

---

## ▶️ How to Run Locally

1. **Clone this repo**
   ```bash
   git clone https://github.com/rajwant-raj/face-mask-detection.git
   cd face-mask-detection
2. Create a virtual environment (optional but recommended)

3. Install dependencies

bash
pip install -r requirements.txt
Run the app

`bash
streamlit run app.py

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **TensorFlow / Keras**
- **Streamlit**
- **NumPy, Pillow, Matplotlib**
- **Kaggle API**


🙋‍♂️ Author
Developed by [rajwant-raj] as part of a Deep Learning internship project at Scalezix.
Feel free to ⭐ this repo if you found it helpful!

📜 License
This project is licensed under the MIT License.



