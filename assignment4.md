# Assignment 4: Learning Machine Learning
> Due Thursday October 31st at 11:59 PM on Gradescope

### Preface
In this assignment, we will be taking a deep dive into machine learning. This is NOT a machine learning class, so very little math is expected in this assignment, however thinking about the questions rationally and exercising proper debugging will help.

This assignment will be completed in a iPython notebook. Feel free to use Google Colab or your own machine. Be warned that the second part of this assignment involves neural network training, which is computationally expensive and may take a long time on a laptop.

This assignment will be graded by the staff, so make sure to comment your code and document design considerations. You are allowed to use external libraries if you wish (e.g. `math` or `numpy`) but obviously implementations must be done yourself without importing from libraries like Sci-Kit Learn. 

## Deep Learning Training (25 Points)
In this section, we will be optimizing the parameters for neural network training, particularly in an image classification task Note: if you are using Google Colab make sure to change the **Runtime Type to GPU** to speed up your training time!

Try out **at least three different parameter alterations** and note each final accuracy. In addition, write a sentence or two describing what your high-level intuition is for explaining the performance difference (if any). We’re not looking for any particular accuracy, just an exploration of different hyperparameter tunings which lead to some change. 

For some inspiration changing your network architecture, consider changing:
- `batch_size` (smaller batch size = more parameter updates)
- `Dropout(p)` (randomly zeros neurons with probability `p` to prevent overfitting)
- `SGD` (stochastic gradient descent) to `Adadelta` (different optimizers [here](https://keras.io/optimizers/))
- `lr` (larger learning rate = more changes per instance, less granularity)
- `epochs` (more passes through the data)

There is a lot of nomenclature involved, so you may consult external resources, and ask as many questions as you would like on Piazza. Feel free to make any architecture change (e.g. `model.add()`), if you’re feeling adventurous! However, just changing the hyperparameters (with explanation) is sufficient for full credit.

## Word Embeddings (25 Points)
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

## K-Nearest Neighbors (50 Points)
In this section, we will implement the K-Nearest Neighbors model. Recall that KNN is an algorithm that classifies a new instance by comparing its distance to other elements (within a certain range `k`) and then taking the majority class.

There are different ways of implementing the K-Nearest Neighbors model. One way of breaking down this problem is as follows:

1. Vectorizing instances (e.g. converting labels to numbers)
2. Computing distances (e.g. euclidean, hamming, manhattan)
3. Sorting dataset by distance to instance
4. Taking majority class of top `k` elements closest to instance

For this assignment, feel free to set `k = math.sqrt(n)` where `n = len(dataset)`. However, if you find a more optimal value for `k`, you may use it instead. Feel free to document this for a chance of more extra credit!

### Dataset
We will be using a dataset in the following format:

```python
dataset = [(50, 20, "cotton", "shorts"), (150, 50, "denim", "pants"), (100, 35, "polyester", "pants), (45, 15, "spandex", "shorts)]
```

Note this dataset is represented by tuples which indicate `(length, price, material, LABEL)`. It is up to you to design a model that can vectorize the input in a meaningful way and generate accurate predictions. 

1. Implement a class named `Model` that has a constructor which takes in the dataset. 
2. Implement a class method named `predict`, which takes a new instance as input (in the same format as the dataset - without the label) and returns the predicted class.
3. Implement a class method named `accuracy` which returns the accuracy of predictions against the true labels. This should be a percentage value (e.g. 75.55%). 
