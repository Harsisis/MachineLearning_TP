import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import accuracy_score

def preTrained():
    # Chargement du jeu de données CIFAR-10
    (train_images, train_labels), (test_images, test_labels), (validation_images, validation_labels) = cifar10.load_data()

    # Affichage des dimensions des ensembles d'entraînement et de test
    print("Dimensions des images d'entraînement:", train_images.shape)
    print("Dimensions des étiquettes d'entraînement:", train_labels.shape)
    print("Dimensions des images de test:", test_images.shape)
    print("Dimensions des étiquettes de test:", test_labels.shape)

    # prétraitement du jeu de données CIFAR-10
    train_images = train_images / 255.0
    test_images = test_images / 255.0
    validation_images = validation_images / 255.0

    train_labels = to_categorical(train_labels, num_classes=10)
    test_labels = to_categorical(test_labels, num_classes=10)
    validation_labels = to_categorical(validation_labels, num_classes=10)

    # Chargement du modèle préentraîné MobileNetV2 sans la couche de classification
    base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(32, 32, 3))

    # Ajout de couches de classification personnalisées au modèle
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(256, activation='relu')(x)
    predictions = Dense(10, activation='softmax')(x)

    model = Model(inputs=base_model.input, outputs=predictions)

    # Compilation du modèle
    model.compile(optimizer=tf.keras.optimizers.Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

    # Entraînement du modèle
    model.fit(train_images, train_labels, validation_labels, batch_size=64, epochs=10, validation_split=0.1)

    # Évaluation du modèle sur l'ensemble de test
    test_loss, test_acc = model.evaluate(test_images, test_labels, validation_labels)
    print("Accuracy on test set:", test_acc)

    # Prédictions sur l'ensemble de test
    predictions = model.predict(test_images)
    predicted_labels = predictions.argmax(axis=1)
    true_labels = test_labels.argmax(axis=1)

    # Calcul de la précision
    accuracy = accuracy_score(true_labels, predicted_labels)
    print("Accuracy:", accuracy)
    return accuracy
