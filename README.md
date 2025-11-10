# AIwPy-final
Final assignment for AI dev with Python

---
## Handwritten Text Recognition (HTR) Demo

Included here is training script and interface-application for<br/>
a locally trained and executed HTR model.

### Training

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

---

#### Training data

[EMNIST-balanced](https://www.nist.gov/itl/products-and-services/emnist-dataset): Cohen, G., Afshar, S., Tapson, J., & van Schaik, A. (2017). EMNIST: an extension<br/>
of MNIST to handwritten letters. Retrieved from http://arxiv.org/abs/1702.05373
