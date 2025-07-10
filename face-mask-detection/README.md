# 😷 Face Mask Detection using CNN

> A Deep Learning project that detects whether a person is wearing a face mask or not using a Convolutional Neural Network (CNN). Built for internship submission, deployed with Streamlit.

---

## 📌 Project Overview

This project is part of a college internship where we train a CNN model to classify images as either:

- **with_mask**
- **without_mask**

The dataset is obtained via the Kaggle API and the model is built and trained in Google Colab using TensorFlow. The final model is deployed using a Streamlit web app where users can upload images and receive predictions in real-time.

---

## 🧠 Technologies Used

- Python
- TensorFlow / Keras
- Google Colab
- Kaggle API
- Splitfolders
- Streamlit
- Seaborn & Matplotlib

---

## 📁 Folder Structure

face-mask-detection/
│
├── app.py # Streamlit app
├── mask_detector_model.h5 # Trained CNN model
├── README.md # Project documentation
├── requirements.txt # Python dependencies
├── utils.py # Helper functions (e.g., predict)
├── /data # (optional) Local data folder
│ ├── with_mask/
│ └── without_mask/
└── /notebooks
└── Face_Mask_Detection.ipynb # Google Colab notebook

---

## 🚀 Getting Started

### ✅ 1. Clone this repo

```bash
git clone https://github.com/yourusername/face-mask-detection.git
cd face-mask-detection
✅ 2. Install Dependencies
Make sure you have Python ≥ 3.8 and install all requirements:

bash

pip install -r requirements.txt
If TensorFlow fails to install, install Microsoft C++ Redistributable and check Python version compatibility.

📦 Model Training (Colab)
Open the Face_Mask_Detection.ipynb notebook in Google Colab and:

Automatically download dataset using Kaggle API

Preprocess & augment images

Build and train CNN

Plot accuracy/loss graphs

Save model as .h5 file

🖥️ Run the Web App Locally
bash
Copy
Edit
streamlit run app.py
Once running, visit:  http://localhost:8501
You can upload an image and get instant predictions for:

😷 With Mask

😡 Without Mask

🧠 Model Architecture
3 Convolutional + MaxPooling layers

Flatten → Dense (128 units)

Dropout(0.5)

Output: 2 neurons with softmax

Trained with:

categorical_crossentropy loss

Adam optimizer

10 epochs

📊 Confusion Matrix & Evaluation
Evaluate on test data using:

Accuracy

Loss

Confusion Matrix

Classification Report

📌 Dataset
Face Mask Dataset by Omkar Gurav

Classes:

with_mask 😷

without_mask 😡

🌐 Deployment Options
✅ Localhost via Streamlit

✅ Public share with ngrok

✅ Free HTTPS hosting via Streamlit Cloud

📸 Sample Output


## 📊 Dataset

- **Kaggle Dataset**: [Face Mask Dataset by Omkar Gurav](https://www.kaggle.com/datasets/omkargurav/face-mask-dataset)
- Contains 2 categories: `with_mask` and `without_mask`
- Images are split into Train (80%), Validation (10%), and Test (10%) using `splitfolders`

---

## 🚀 How to Run the Streamlit App Locally

1. Clone this repository:

```bash
git clone https://github.com/your-username/face-mask-detection.git
cd face-mask-detection/streamlit_app
Install required packages:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
streamlit run app.py
🧪 Sample Output
Test Accuracy: ~97–99%

Includes accuracy/loss plots, confusion matrix, and classification report

Real-time prediction on uploaded images using mask_detector_model.h5

✅ Features
CNN-based real-time image classification

Trained with Kaggle API dataset in Colab

Automatic dataset split (Train/Val/Test)

Confusion matrix and F1-report included

Streamlit web interface for live predictions

📚 Internship Use
This project was developed as part of a college internship to demonstrate:

Applied deep learning skills 

Used ai tools

Model evaluation with metrics

Deployment-ready web interface using Streamlit

🤝 Acknowledgements
Omkar Gurav - Dataset Creator

Kaggle

Streamlit

🧑‍💻 Developed By
Rajwant-Raj
Summer-Intern @ [Scalezix]
Guided by: [Sir Harsh Singh ]
