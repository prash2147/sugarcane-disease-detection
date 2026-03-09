import numpy as np
from tensorflow.keras.preprocessing import image
import tensorflow as tf

model = tf.keras.models.load_model("sugarcane_model.h5")

class_names = ['Healthy','Mosaic','RedRot','Rust','Yellow']

img_path = input("Enter image path: ")

img = image.load_img(img_path, target_size=(224,224))
img_array = image.img_to_array(img)
img_array = img_array/255.0
img_array = np.expand_dims(img_array, axis=0)

prediction = model.predict(img_array)

print("Raw prediction:", prediction)

predicted_class = class_names[np.argmax(prediction)]
confidence = np.max(prediction)*100

print("====== RESULT ======")
print("Disease:", predicted_class)
print("Confidence:", confidence,"%")
print("====================")
