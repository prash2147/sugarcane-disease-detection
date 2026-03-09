import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image

# load model
model = tf.keras.models.load_model("sugarcane_model.h5")

classes = ['Healthy','RedRot','Rust','Yellow','Mosaic']

st.title("Sugarcane Disease Detection 🌱")

uploaded_file = st.file_uploader("Upload sugarcane leaf image", type=["jpg","jpeg","png"])

if uploaded_file is not None:

    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", width=500)

    img = img.resize((224,224))
    img_array = np.array(img)/255.0
    img_array = np.expand_dims(img_array, axis=0)

    pred = model.predict(img_array)
    index = np.argmax(pred)

    st.success(f"Disease: {classes[index]}")
    st.write(f"Confidence: {pred[0][index]*100:.2f}%")

    st.subheader("Prediction Probabilities")

    for i, c in enumerate(classes):
        st.write(f"{c}: {pred[0][i]*100:.2f}%")

    solutions = {
    "RedRot":"Use resistant varieties and remove infected plants.",
    "Rust":"Apply fungicide and maintain field hygiene.",
    "Mosaic":"Control aphids and remove infected plants.",
    "Yellow":"Improve soil nutrition and remove infected leaves.",
    "Healthy":"Plant is healthy."
    }

    st.subheader("Suggested Action")
    st.info(solutions[classes[index]])
