import scipy.io
import tensorflow
from tensorflow.keras import layers, models

data = scipy.io.loadmat("model/data/emnist-balanced.mat")

x_train = data["dataset"][0][0][0][0][0][0]
y_train = data["dataset"][0][0][0][0][0][1]
x_test = data["dataset"][0][0][1][0][0][0]
y_test = data["dataset"][0][0][1][0][0][1]

x_train = x_train.reshape((-1, 28, 28, 1)).astype("float32") / 255.0
x_test = x_test.reshape((-1, 28, 28, 1)).astype("float32") / 255.0

y_train = y_train.flatten()
y_test = y_test.flatten()

model = models.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Conv2D(32, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation="relu"),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(47, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

history = model.fit(
    x_train, y_train,
    epochs=10,
    batch_size=256,
    validation_data=(x_test, y_test)
)

model.save("emnist_model.h5")
