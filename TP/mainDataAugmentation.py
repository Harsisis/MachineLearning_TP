import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def dataAugmentation():
    # Chargement et prétraitement du jeu de données CIFAR-10
    (train_images, train_labels), (test_images, test_labels) = cifar10.load_data()
    train_images = train_images / 255.0
    test_images = test_images / 255.0

    # Création du modèle CNN simple
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(10, activation='softmax')
    ])

    # Compilation du modèle
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Augmentation de données sur l'ensemble d'entraînement
    datagen = ImageDataGenerator(
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True
    )
    datagen.fit(train_images)

    # Entraînement du modèle avec augmentation de données
    model.fit(datagen.flow(train_images, train_labels, batch_size=64),
            steps_per_epoch=len(train_images) / 64, epochs=10,
            validation_data=(test_images, test_labels))

    # Évaluation du modèle sur l'ensemble de test
    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print("Accuracy on test set:", test_acc)
    return test_acc
