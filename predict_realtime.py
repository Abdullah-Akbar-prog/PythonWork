import cv2
import tensorflow as tf
import numpy as np
import os
import tkinter as tk

# Automatically get classes from dataset folder
dataset_path = 'dataset'
classes = [folder for folder in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, folder))]
print(f"Detected classes: {classes}")

# Load trained model
model = tf.keras.models.load_model('classifier.h5')

# Initialize camera
cap = cv2.VideoCapture(0)

# Function to close app
def close_app():
    cap.release()
    cv2.destroyAllWindows()
    root.destroy()

# Tkinter window with Close button
root = tk.Tk()
root.title("Real-Time Prediction")

close_btn = tk.Button(root, text="Close", command=close_app, bg="red", fg="white", width=20, height=2)
close_btn.pack(pady=20)

# Threshold for detection
THRESHOLD = 0.6

# Show camera feed and prediction
def show_camera():
    ret, frame = cap.read()
    if ret:
        img = cv2.resize(frame, (224,224))
        img = np.expand_dims(img/255.0, axis=0)
        
        prediction = model.predict(img)[0]
        max_prob = np.max(prediction)
        if max_prob < THRESHOLD:
            class_name = "Not Found"
            color = (0,0,255)
        else:
            class_name = classes[np.argmax(prediction)]
            color = (0,255,0)
        
        cv2.putText(frame, class_name, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        cv2.imshow('Real-Time Object Detection', frame)
    
    if cv2.waitKey(1) & 0xFF != 27:
        root.after(10, show_camera)
    else:
        close_app()

show_camera()
root.mainloop()
