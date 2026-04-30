import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import cv2

# load model
model = tf.keras.models.load_model("sugarcane_model.h5")

classes = ['Healthy','Mosaic','RedRot','Rust','Yellow']

# define function FIRST
def blur_background(img):
    img_np = np.array(img)

    # convert to HSV
    hsv = cv2.cvtColor(img_np, cv2.COLOR_RGB2HSV)

    # green mask
    lower_green = np.array([25, 40, 40])
    upper_green = np.array([90, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # blur background
    blurred = cv2.GaussianBlur(img_np, (21,21), 0)

    result = np.where(mask[:,:,None]==255, img_np, blurred)
    return result


st.title("Sugarcane Disease Detection 🌱")

uploaded_file = st.file_uploader("Upload sugarcane leaf image", type=["jpg","jpeg","png"])

if uploaded_file is not None:

    img = Image.open(uploaded_file).convert("RGB")

    # apply blur
    processed_img = blur_background(img)

    st.image(processed_img, caption="Processed Image", width=500)

    # preprocess
    img = Image.fromarray(processed_img)
    img = img.resize((224,224))
    img_array = np.array(img)/255.0

    # FIX: add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    # METHOD 3: GREEN CHECK
    green_ratio = np.mean(
        (img_array[:,:,:,1] > img_array[:,:,:,0]) &
        (img_array[:,:,:,1] > img_array[:,:,:,2])
    )

    if green_ratio < 0.2:
        st.error("❌ Not a sugarcane leaf image")
    else:
        # prediction only if valid
        pred = model.predict(img_array)[0]

        index = np.argmax(pred)
        confidence = pred[index]

        # confidence check
        if confidence < 0.55:
            st.warning("Low confidence prediction. Try another image.")
        else:
            st.success(f"Disease: {classes[index]}")
            st.write(f"Confidence: {confidence*100:.2f}%")

            st.subheader("Prediction Probabilities")

            for i, c in enumerate(classes):
                st.write(f"{c}: {pred[i]*100:.2f}%")

            solutions = {
                "RedRot":"Use resistant varieties and remove infected plants.",
                "Rust":"Apply fungicide and maintain field hygiene.",
                "Mosaic":"Control aphids and remove infected plants.",
                "Yellow":"Improve soil nutrition and remove infected leaves.",
                "Healthy":"Plant is healthy."
            }

            st.subheader("Suggested Action")
            st.info(solutions[classes[index]])