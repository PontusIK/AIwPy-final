import keras
import cv2
import numpy

def get_response(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    _, thresh = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    chars = []
    index = 0
    for char in sorted(contours, key=lambda x: cv2.boundingRect(x)[0]):
        x, y, w, h = cv2.boundingRect(char)
        char_img = thresh[y:y+h, x:x+w]
        char_img = cv2.resize(char_img, (28, 28))
        char_img = char_img.astype("float32")/255.0
        cv2.imwrite(f"char_{index}.png", (char_img * 255).astype("uint8"))
        index = index + 1
        char_img = numpy.expand_dims(char_img, axis=-1)
        chars.append(char_img)

    x = numpy.array(chars)

    predictions = model.predict(x)
    predicted_classes = numpy.argmax(predictions, axis=1)
    return "".join(CLASSES[c] for c in predicted_classes)

def load_classes():
    classes = {}
    with open("model/data/emnist-balanced-mapping.txt", "r") as file:
        for line in file:
            idx, ascii_code = line.strip().split()
            classes[int(idx)] = chr(int(ascii_code))
    return [classes[i] for i in range(len(classes))]

CLASSES = load_classes()
model = keras.models.load_model("HTR.keras")
