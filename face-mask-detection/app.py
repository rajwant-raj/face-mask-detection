import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image

st.set_page_config(page_title="😷 Face Mask Detection", layout="centered")
st.title("😷 Face Mask Detection using CNN")
st.markdown("Upload a face image and let the model predict whether the person is **wearing a mask** or **not**.")

@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("mask_detector_model.h5")
    return model

model = load_model()

class_labels = ['with_mask', 'without_mask']

uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert('RGB')
    st.image(img, caption='Uploaded Image', use_column_width=True)

    img_resized = img.resize((128, 128))
    img_array = image.img_to_array(img_resized)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    prediction = model.predict(img_array)
    predicted_label = class_labels[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    st.markdown(f"### 🧠 Prediction: `{predicted_label}`")
    st.markdown(f"### 🔍 Confidence: `{confidence:.2f}%`")

    if predicted_label == "with_mask":
        st.success("✅ Great! Mask is detected.")
    else:
        st.warning("⚠️ No mask detected!")
