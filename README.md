# AIwPy-final
Final assignment for AI dev with Python

---
## Handwritten Text Recognition (HTR) Demo

Included here is training script and interface-application for<br/>
a locally trained and executed HTR model.

### Training

The model was trained on the EMNIST-balanced dataset, which<br/>
includes handwritten samples of digits as well as both upper- and<br/>
lowercase letter. The image data was normalized before training to<br/>
better fit the CNN algorithm, such as scaling the pixel values from<br/>
the original range of 0-255 to 0-1.

The model was trained to a Convolutional Neural Network (CNN) that consists<br/>
of several convolutional layers for deature extraction,<br/>
pooling layers for downsampling, and dense layers for classification.<br/>
Training was done for 10 epochs using the Adam optimizer and<br/>
categorical crossentropy loss.

### Execution

Input image is segmented into individual characters and preprocessed<br/>
to resemble training data using opencv4. Later the images are normalized to an<br/>
array of float32 before being fed to the model.<br/>
Predictions are made of every image and the one with highest confidence of each image<br/>
is concatenated and displayed.

#### Examples

Input image and result:

![Input image and result](images/hello/hello.png)

Opencv4-processed images:

![H](images/hello/char_0.png) ![e](images/hello/char_1.png) ![l](images/hello/char_2.png) ![l](images/hello/char_3.png) ![o](images/hello/char_4.png)

Input image and result:

![Input image and result](images/pontus/pontus.png)

Opencv4-processed images:

![P](images/pontus/char_0.png) ![o](images/pontus/char_1.png) ![n](images/pontus/char_2.png) ![t](images/pontus/char_3.png) ![u](images/pontus/char_4.png) ![s](images/pontus/char_5.png)

### Reflections

The model isn't prefect but for a demonstration of HTR capabilities, it is good enough.<br/>
The model isn't entirely at fault for failed predictions either. Part of the blame<br/>
lies with the preprocessing done with opencv4, as it tends to accentuate features of othrewise<br/>
featureless characters.<br/>
*see the 2 'l's in "Hello"*

Improvements to the models performance could include but is not limited to:
* adding more epochs to reduce underfitting.
* expanding the dataset to include more diverse writing styles.
* improving on the segmentation and preprocessing done with opencv4.
* or changing the model to one that can interpret characters in sequence.

---

#### Training data

[EMNIST-balanced](https://www.nist.gov/itl/products-and-services/emnist-dataset): Cohen, G., Afshar, S., Tapson, J., & van Schaik, A. (2017). EMNIST: an extension<br/>
of MNIST to handwritten letters. Retrieved from http://arxiv.org/abs/1702.05373
