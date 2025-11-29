import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Automatically get class names from dataset folder
dataset_path = 'dataset'
classes = [folder for folder in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, folder))]
print(f"Found classes: {classes}")

# Check dataset
for c in classes:
    path = os.path.join(dataset_path, c)
    print(f"{c} images: {len(os.listdir(path))}")

# Image preprocessing
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_gen = datagen.flow_from_directory(
    dataset_path,
    target_size=(224,224),
    batch_size=16,
    class_mode='categorical',
    subset='training'
)

val_gen = datagen.flow_from_directory(
    dataset_path,
    target_size=(224,224),
    batch_size=16,
    class_mode='categorical',
    subset='validation'
)

# MobileNetV2 base
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224,224,3),
    include_top=False,
    weights='imagenet'
)
base_model.trainable = False

# Add classification layers
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(len(classes), activation='softmax')
])

# Compile and train
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(train_gen, validation_data=val_gen, epochs=10)

# Save model
model.save('classifier.h5')
print("Model trained and saved as classifier.h5")
