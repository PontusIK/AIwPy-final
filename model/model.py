from keras.src.utils import to_categorical
import scipy.io
import numpy
from keras import layers, models

data = scipy.io.loadmat("model/data/emnist-balanced.mat")

x_train = data["dataset"][0][0][0][0][0][0]
y_train = data["dataset"][0][0][0][0][0][1]
x_test = data["dataset"][0][0][1][0][0][0]
y_test = data["dataset"][0][0][1][0][0][1]

x_train = x_train.reshape((-1, 28, 28))
x_test = x_test.reshape((-1, 28, 28))

x_train = numpy.transpose(x_train, (0, 2, 1))
x_test = numpy.transpose(x_test, (0, 2, 1))

x_train = numpy.expand_dims(x_train, axis=-1).astype("float32") / 255.0
x_test = numpy.expand_dims(x_test, axis=-1).astype("float32") / 255.0

y_train = y_train.flatten()
y_test = y_test.flatten()

y_train = to_categorical(y_train, 47)
y_test = to_categorical(y_test, 47)

model = models.Sequential([    
    layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation="relu"),
    layers.Dropout(0.3),
    layers.Flatten(),
    layers.Dense(256, activation="relu"),
    layers.Dropout(0.3),
    layers.Dense(47, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

history = model.fit(
    x_train, y_train,
    epochs=10,
    batch_size=256,
    validation_data=(x_test, y_test)
)

model.save("HTR.keras")
