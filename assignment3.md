# Assignment 3: Learning Machine Learning
> Due Tuesday, March 31st at 11:59 PM on Gradescope

### Preface
In this assignment, we will be taking a deep dive into machine learning. This is NOT a machine learning class, so very little math is expected in this assignment, however thinking about the questions rationally and exercising proper debugging will help.

This assignment will be completed in a iPython notebook. Feel free to use Google Colab or your own machine. Be warned that the second part of this assignment involves neural network training, which is computationally expensive and may take a long time on a laptop.

This assignment will be graded by the staff, so make sure to comment your code and document design considerations. You are allowed to use external libraries if you wish (e.g. `math` or `numpy`) but obviously implementations must be done yourself without importing from libraries like Sci-Kit Learn. 

## Deep Learning Training
In this section, we will be optimizing the parameters for neural network training, particularly in an image classification task Note: if you are using Google Colab make sure to change the **Runtime Type to GPU** to speed up your training time!

**TODO:** Try out **at least three different parameter alterations** and note each final accuracy. In addition, write a sentence or two describing what your high-level intuition is for explaining the performance difference (if any). We’re not looking for any particular accuracy, just an exploration of different hyperparameter tunings which lead to some change. 

For some inspiration changing your network architecture, consider changing:
- `batch_size` (smaller batch size = more parameter updates)
- `Dropout(p)` (randomly zeros neurons with probability `p` to prevent overfitting)
- `SGD` (stochastic gradient descent) to `Adadelta` (different optimizers [here](https://keras.io/optimizers/))
- `lr` (larger learning rate = more changes per instance, less granularity)
- `epochs` (more passes through the data)

There is a lot of nomenclature involved, so you may consult external resources, and ask as many questions as you would like on Piazza. Feel free to make any architecture change (e.g. `model.add()`), if you’re feeling adventurous! However, just changing the hyperparameters (with explanation) is sufficient for full credit.

```python
'''Trains a simple convnet on the MNIST dataset. Credit: Keras Team'''
from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D

# DEFINING *SOME* HYPERPARAMETERS
batch_size = 256
num_classes = 10
epochs = 2 

# DATA CLEAN-UP
img_rows, img_cols = 28, 28

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
input_shape = (img_rows, img_cols, 1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# MODEL DEFINITION (some hardcodede hyperparameters)
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.9))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.9))
model.add(Dense(num_classes, activation='softmax'))

# MODEL COMPILATION AND TRAINING
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(lr=0.001),
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))

# MODEL EVALUATION
score = model.evaluate(x_test, y_test, verbose=0)

print('Test loss:', score[0])
print('Test accuracy:', score[1])
```

## Word Embeddings
In this section, we will explore different word embeddings systems using the [Magnitude](https://github.com/plasticityai/magnitude) package and pre-trained word embeddings. 

A brief installation (works in Google Colab):

1. `pip install pymagnitude`
2. `!wget http://magnitude.plasticity.ai/word2vec/light/GoogleNews-vectors-negative300.magnitude`

We can now instantiate a query-able Magnitude vectors object as follows:

```python
from pymagnitude import *

file_path = "GoogleNews-vectors-negative300.magnitude"
vectors = Magnitude(file_path)
print(vectors.distance("cat", "dog"))
```

For this question, create a text cell in your iPython notebook answering the following questions by referring to the Magnitude [documentation](https://github.com/plasticityai/magnitude#using-the-library): 

1. What is the dimensionality of these word embeddings? Provide an integer answer.
2.  What are the top-5 most similar words to picnic (not including picnic itself)?
3. According to the word embeddings, which of these words is not like the others? `[tissue', 'papyrus', 'manila', 'newsprint', 'parchment', 'gazette’]`
4. Solve the following analogy: “leg is to jump as `X` is to throw”.
5. Is the word `alumni` in the vocabulary? What about `alumnus`?
6. How many words are in the vocabulary?
