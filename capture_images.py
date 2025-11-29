import cv2
import os
import tkinter as tk
from tkinter import simpledialog

# Ask for class names
root_input = tk.Tk()
root_input.withdraw()
class1 = simpledialog.askstring("Input", "Enter first class name : ")
class2 = simpledialog.askstring("Input", "Enter second class name : ")
root_input.destroy()


classes = [class1, class2]

# Create dataset folders
for c in classes:
    os.makedirs(f'dataset/{c}', exist_ok=True)

# Initialize camera
cap = cv2.VideoCapture(0)
counters = {c:0 for c in classes}

# Capture function
def capture(class_name):
    ret, frame = cap.read()
    if ret:
        img_name = f"dataset/{class_name}/{counters[class_name]}.jpg"
        cv2.imwrite(img_name, frame)
        counters[class_name] += 1
        print(f"{img_name} saved!")

# Close app
def close_app():
    cap.release()
    cv2.destroyAllWindows()
    root.destroy()

# Tkinter GUI
root = tk.Tk()
root.title("Capture Images")

for c in classes:
    btn = tk.Button(root, text=f"Capture {c}", command=lambda c=c: capture(c), width=20, height=2)
    btn.pack(pady=10)

close_btn = tk.Button(root, text="Close", command=close_app, bg="red", fg="white", width=20, height=2)
close_btn.pack(pady=10)

# Show camera feed
def show_camera():
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Camera", frame)
    if cv2.waitKey(1) & 0xFF != 27:
        root.after(10, show_camera)
    else:
        close_app()

show_camera()
root.mainloop()
