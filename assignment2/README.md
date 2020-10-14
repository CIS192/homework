
# Assignment 2: Learning Machine Learning

In this assignment, we will be exploring the field of computational linguistics, also known as **Natural Language Processing**. The goal of this assignment is to have you become familiar with reading/writing to files, and working with third party packages. We'll explore these Python ideas through the lens of Data Science and Machine Learning.

## Part 0: Setup

Skim through the assignment and install the relevant packages for this assignment through pip (e.g. [Sci-Kit Learn](https://github.com/scikit-learn/scikit-learn) and [NumPy](https://github.com/numpy/numpy)). Next, download the homework datasets [here](https://github.com/CIS192/homework/raw/master/assignment2/data.zip) (or from the GitHub repository). Finally, download the skeleton code, as well as the report template from the [assignment's GitHub repository](https://github.com/CIS192/homework/tree/master/assignment2).

## Part 1: NLP Basics

For the first part of the homework you will be implementing a couple of basic NLP tasks in `part1.py`, including raw text analysis with CSV, text tokenizing, and word importance with a score called TF-IDF. The data file `raven.txt` is located in the `data.zip` file, so make sure to unzip it to `/data`! The remaining dataset files will be used for Part 2, so be sure to keep those handy.

**TODO:** Implement the incomplete stubs in `part1.py`.

## Part 2: Classification with Sci-Kit Learn

> Adapted from CIS 530 - Computational Linguistics

### Preamble

The second part of the homework will be a longer project: building a text classifier. Now that we have seen tokenizing, text cleaning, and word importance with TF-IDF, let's train a text classifier that will be able to classify a word as being simple (e.g. *easy*, *act*, *blue*) or complex (e.g. *ostentatious*, *esoteric*, *aberration*). This is an important step in a larger NLP task to simply texts to make text more readable.

In the provided code template with proveded helper and unimplemented functions, you will need to:

0. Look at the dataset! Try to understand the information that is conveyed to better understand the task.
1. Implement the machine learning evaluation metric we discussed in class (accuracy).
2. Perform data pre-processing for our dataset. You will need to parse the provided pre-labeled data in training/test sets, and implement a simple baseline model.
3. Use the Sci-Kit Learn package to train machine learning models which classify words as simple or complex.

We have provided the dataset of labelled words split between training/test sets in (.txt) format. Some notes on the dataset:

1. The training set is disjoint, so a word in `complex_words_training.txt` will not appear in the other two.
2. Stop-words and proper nouns are already removed, leaving only nouns, verbs, and adjectives.
3. There are 4,000 training words, and 922 testing words.
4. The relevant columns are WORD (the word to be classified), and LABEL (0 for simple, 1 for complex). Note that LABEL is not included in the test dataset.

We have also provided frequencies (a contiguous sequence of 1 item from a given sample of text or speech) from the [Google N-Gram Corpus](https://books.google.com/ngrams/info). This is to provide you another feature for classification. Consider why this extra information is useful for distinguishing between simple and complex words.

Be sure to install `numpy` and `sklearn` before starting.

### Section 0: Data (0 points)

We have provided the function `load_file` that takes in the file name `data_file` of one of the datasets and returns the words and labels of that dataset. The second provided helper function `load_ngram_counts` loads Google N-Gram counts from our provided file `ngram_counts.txt` as a dictionary of word frequencies.

**TODO:** Inspect these functions, print out what they return and make sure you understand what they're providing before moving on.

### Section 1: Evaluation (5 points)

We will be implementing **accuracy**, a standard evaluation metric that we discussed in class. We will use this function later in the assignment, so be sure that this function works before moving on.

**TODO:** Implement `get_accuracy`, which should return a value between 0 and 1 that corresponds to the amount of predictions that match the true labels.

### Section 2: Baseline Models (20 points)

In the following functions, you will implement 3 baseline models. Recall that baseline models are used to benchmark our own machine learning models against.

1. The first baseline model `all_complex` classifies ALL words as complex (think back to the coin-flipping example from class).
2. The second baseline model `word_length_threshold` uses word length thresholding: if a word is longer than the given threshold, we consider it to be complex, and vice versa.
3. The third baseline model `word_frequency_threshold` is similar to the second, but we will use frequencies from the Google N-Gram counts dataset as the metric to threshold against.

**TODO:** Implement the three baseline models, and report their accuracies (using the function you implemented earlier).

### Section 3: Machine Learning Models (20 points)

For our machine learning classifiers, we will use the built-in Naive Bayes and Logistic Regression models from Sci-Kit Learn to train a classifier. Refer to the [Sci-Kit Learn Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html) for more information about the Sci-Kit Learn API. Feel free to experiment with other models for extra credit!

For features, you'll want to use both word length and word frequency. However, feel free to use any other features that you want! Be sure to document any extra features in `REPORT.md`. Extra credit is available for the inclusion of any other interesting features!

You can import the relevant models from Sci-Kit Learn using:

```python
from sklearn.naive_bayes import GaussianNB
```

for Naive Bayes and

```python
from sklearn.linear_model import LogisticRegression
```

for Logistic Regression. To train a classifier, you need two numpy arrays:

1. `X_train`: size (`m` x `n`), where `m` is the number of words and `n` is the number of features for each word.
2. `Y_train`: size (`m` x `1`) for the labels of each of the `m` words.

Since Sci-Kit Learn classifiers take in `numpy` arrays, always wrap your lists in a `np.array`:

```python
my_array = np.array([1, 2, 3, 4, 5])
```

As such, you'll want to import `numpy` using:

```python
import numpy as np
```

**TODO:** Implement `logistic_regression` and `naive_bayes`, where you will train the machine learning models and report their accuracies on the testing data.

### Section 4: Report (5 points)

**TODO:** Complete `REPORT.md` with information about your implementations and your accuracies for each section. Write a few comments comparing the performace of your Naive Bayes classifier and your Logistic Regression classifier. Include any details about extra credit you've completed.

Be sure to complete the report in [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) format. Remember to indicate which member worked on which sections for full credit.

## Submission

Submit all your code and potentially extra data to Gradescope. If you have a partner, YOU MUST MARK THEM AS A COLLABORATOR ON GRADESCOPE. If you fail to do this, you may get a 0 on this assignment.

## Attributions

This homework was adapted from [CIS 530: Computational Linguistics at the University of Pennsylvania](https://computational-linguistics-class.org/) by Arun Kirubarajan and Kevin Sun.
