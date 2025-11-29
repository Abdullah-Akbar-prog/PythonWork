Below is a **complete, professional, clean README.md** for your project.
You can copy-paste this file directly into **README.md**.

I also included all the **commands**, folder structure, installation steps, and run instructions.

---

# 📌 Real-Time Object Classification Using OpenCV + TensorFlow + Tkinter

This project allows you to **capture images**, **train a deep learning model**, and **perform real-time object prediction** using your webcam.

You can dynamically choose **two classes at runtime**, capture photos for each class, train the model, and detect objects live.

---

# 📁 Project Structure

```
project/
│
├── capture_images.py
├── train_model.py
├── predict_realtime.py
│
└── dataset/
    ├── class1/
    └── class2/
```

---

# ⚙️ 1. Requirements / Installation

### **Install Python packages**

Run this command:

```bash
pip install tensorflow opencv-python numpy tkinter
```

> 📝 Note: Tkinter comes pre-installed with Python. If not, install it based on your OS.

---

# 📸 2. Capture Images

Script: **capture_images.py**

### ✔ Features

* Ask user for class names (e.g., "bottle", "hand").
* Automatically creates folders.
* Opens webcam.
* Buttons to capture photos.
* Saves images as:
  `dataset/class_name/0.jpg`, `1.jpg`, `2.jpg` ...

### ▶ Run command:

```bash
python capture_images.py
```

### 💡 How it works

1. A popup asks:

   * **Enter first class name**
   * **Enter second class name**
2. Webcam opens in a Tkinter window.
3. Buttons appear:

   * **Capture Class 1**
   * **Capture Class 2**
   * **Close**
4. Photos are saved automatically with counters.

---

# 🧠 3. Train the Model

Script: **train_model.py**

### ✔ Features

* Reads all images from the dataset folder.
* Trains a simple CNN model.
* Saves model as:
  **bottle_hand_classifier.h5**

### ▶ Run command:

```bash
python train_model.py
```

### 💡 Training Output

* Shows accuracy and loss.
* Saves the trained model automatically.

---

# 🔍 4. Real-Time Prediction

Script: **predict_realtime.py**

### ✔ Features

* Loads the saved model.
* Opens webcam.
* Predicts object in real time.
* If object does not match any class → shows **"Not Found"**.
* Has a **Close button** to stop webcam + exit.

### ▶ Run command:

```bash
python predict_realtime.py
```

### 💡 Output

Live prediction appears on video feed:

```
bottle
hand
Not Found
```

---

# 📝 How Each Script Works

## **✔ capture_images.py**

* Asks for class names using Tkinter dialogs.
* Creates folders automatically:

  ```
  dataset/class1
  dataset/class2
  ```
* Opens camera and lets you capture photos.

## **✔ train_model.py**

* Loads dataset from folders.
* Applies image preprocessing.
* Builds & trains a CNN classifier.
* Saves the final model.

## **✔ predict_realtime.py**

* Opens webcam.
* Classifies each frame.
* Displays predicted label OR “Not Found”.
* Close button safely stops everything.

---

# 🚀 Future Improvements

You can enhance this project with:

* More than two classes
* Better CNN architecture
* Transfer learning (MobileNetV2)
* GUI for the entire workflow
* Saving dataset counts
* Exporting model for mobile apps

If you want, I can upgrade any part for you.

---

# 🎉 You're Ready to Use Your Own AI Classifier!

If you'd like, I can also:

✅ Make the UI beautiful
✅ Add sound alerts
✅ Add model accuracy graphs
✅ Create one-click `.exe` file
✅ Add third class (runtime)

Just tell me — I’ll build it step by step.
