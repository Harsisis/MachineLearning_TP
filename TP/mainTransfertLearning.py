import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam

def transfertLearning():
    # Chargement et prétraitement du jeu de données CIFAR-10
    (train_images, train_labels), (test_images, test_labels) = cifar10.load_data()
    train_images = train_images / 255.0
    test_images = test_images / 255.0

    # Chargement du modèle VGG16 préentraîné (sans la couche de classification)
    base_model = VGG16(weights='imagenet', include_top=False, input_shape=(32, 32, 3))

    # Création du modèle personnalisé en remplaçant la couche de classification
    model = Sequential([
        base_model,
        Flatten(),
        Dense(256, activation='relu'),
        Dense(10, activation='softmax')
    ])

    # Gel des couches du modèle VGG16 (ne pas les réentraîner)
    for layer in base_model.layers:
        layer.trainable = False

    # Compilation du modèle
    model.compile(optimizer=Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Entraînement de la nouvelle couche de classification
    model.fit(train_images, train_labels, batch_size=64, epochs=10, validation_split=0.1)

    # Évaluation du modèle sur l'ensemble de test
    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print("Accuracy on test set:", test_acc)
    return test_acc
