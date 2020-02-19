""" CIS 192 Python Programming 
    Do not distribute. Collaboration is permitted with one person.
"""

from collections import defaultdict
import gzip

'''
# 0. Data
We have provided the function below that takes in the file name `data_file` of one of the datasets 
and returns the words and labels of that dataset.

The second provided helper function loads Google N-Gram counts from our provided file `ngram_counts.txt` as 
a dictionary of word frequencies.
'''

def load_file(data_file):
    words = []
    labels = []
    with open(data_file, 'rt', encoding="utf8") as f:
        i = 0
        for line in f:
            if i > 0:
                line_split = line[:-1].split("\t")
                words.append(line_split[0].lower())
                labels.append(int(line_split[1]))
            i += 1
    return words, labels

def load_ngram_counts(ngram_counts_file):
    counts = defaultdict(int)
    with gzip.open(ngram_counts_file, 'rt') as f:
        for line in f:
            token, count = line.strip().split('\t')
            if token[0].islower():
                counts[token] = int(count)
    return counts

'''
# 1. Evaluation Metrics

Input: 
predictions (a list of length n with the predicted labels),
labels (a list of length n with the true labels)
'''

def get_accuracy(predictions, labels):
    # Write your code to calculate accuracy of the predicted labels
    pass


'''
# 2. Baseline Models

In the following functions, you will implement 3 baseline models. The first 
classifies ALL words as complex (think back to the coin-flipping example from class). 
The second uses word length thresholding: if a word is longer than the given threshold, 
we consider to be complex, and vice versa. The third baseline is similar to the second,
but we will use frequencies from the Google N-Gram counts dataset as the metric
to threshold against.
'''

'''
# 2.1 All Complex
'''

def all_complex(data_file):
    # Write your code here to return the accuracy performance score of the all_complex baseline model 
    pass


'''
# 2.2 Length threshold
'''

def word_length_threshold(training_file, test_file):
    # Write your code here to classify words based on their length and a given threshold.
    # e.g. if the threshold is 9, any words with less than 9 characters will be labeled simple,
    # and any words with 9 characters or more will be labeled complex.
    
    # Write your code to return the training and development accuracy score. Your code should find
    # the best length threshold by accuracy, and uses this threshold to classify the training and test set

    return training_performance, test_performance


'''
# 2.3 Frequency threshold

'''

def word_frequency_threshold(training_file, test_file, counts):
    # Write your code to return the training and development accuracy score. Your code should find
    # the best frequency threshold by accuracy, and uses this threshold to classify the
    # training and development set

    return training_performance, development_performance


'''
# 3 Naive Bayes and Logistic Regression
For our first actual machine learning classifier, use the built-in Naive Bayes model from sklearn to train 
a classifier. Refer to the sklearn documentation: 
https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html

Some important notes:
-- Make sure you use these imports: `from sklearn.naive_bayes import GaussianNB`
    and `from sklearn.linear_model import LogisticRegression`
-- To train a classifier, you need two numpy arrays:
    1. X_train: (m x n), where m is the number of words and n is the nubmer of features for each word
    2. Y: (m x 1) for the labels of each of the m words
-- Since sklearn classifiers take in numpy arrays, always wrap your lists in a `np.array`: `X = np.array([1, 2, 3, 4, 5])`
'''

# Trains a Naive Bayes classifier using length and frequency features

def naive_bayes(training_file, test_file, counts):
    # TODO: train a Naive Bayes classification model
    # using word length and word frequency as features

    return training_performance, test_performance

# Trains a Logistic Regression classifier using length and frequency features

def logistic_regression(training_file, test_file, counts):
    # TODO: train a Logistic Regression classification model

    return training_performance, test_performance


'''
# 4 Comparing Naive Bayes and Logistic Regression
Write a few comments here comparing the performace of your Naive Bayes classifier and your 
Logistic Regression classifier. Also include the performance of your 3 baseline models.
Additionally, write code below to print out the testing performance for all 5 models.
'''

if __name__ == "__main__":
    training_file = "data/complex_words_training.txt"
    development_file = "data/complex_words_development.txt"
    test_file = "data/complex_words_test_unlabeled.txt"

    train_data = load_file(training_file)

    # should take around 20 seconds due to size
    ngram_counts_file = "data/ngram_counts.txt.gz"
    counts = load_ngram_counts(ngram_counts_file)

    # TODO:
    # write your code for Part 4 here
