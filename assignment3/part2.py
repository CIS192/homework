""" CIS 192 Python Programming 
    Do not distribute. Collaboration is permitted with one person.
"""

from collections import defaultdict
import gzip

'''
# 1. Evaluation Metrics

Input: y_pred, a list of length n with the predicted labels,
y_true, a list of length n with the true labels
'''


def get_accuracy(y_pred, y_true):
    # Write your code to calculate accuracy of the predicted labels
    pass

'''
# 2. Baseline Models
We have provided the function below that takes in the file name `data_file` of one of the datasets 
and loads in the words and labels of that dataset.
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


'''
# 2.1 All Complex
In the following functions, you will implement 3 baseline models: one that classifies all the words 
as complex and one that uses word length thresholding.
'''


def all_complex_feature(words):
    # Write your code here to labels every word complex and returns the feature matrix for all complex
    pass


def all_complex(data_file):
    # Write your code here to return the accuracy performance score of the all_complex baseline model 
    pass


'''
# 2.2 Length threshold
'''


def length_threshold_feature(words, threshold):
    # Write your code here to makes feature matrix for word_length_threshold
    # e.g. if the threshold is 9, any words with less than 9 characters will be labeled simple,
    # and any words with 9 characters or more will be labeled complex.
    pass


def word_length_threshold(training_file, development_file):
    # Write your code to return the training and development accuracy score. Your code should find
    # the best length threshold by accuracy, and uses this threshold to classify the training and development set
    training_performance = taccuracy
    development_performance = daccuracy
    return training_performance, development_performance


'''
# 2.3 Frequency threshold
The provided helper function loads Google NGram counts from our provided file `ngram_counts.txt` as 
a dictionary of word frequencies.
'''


def load_ngram_counts(ngram_counts_file):
    counts = defaultdict(int)
    with gzip.open(ngram_counts_file, 'rt') as f:
        for line in f:
            token, count = line.strip().split('\t')
            if token[0].islower():
                counts[token] = int(count)
    return counts


def frequency_threshold_feature(words, threshold, counts):
    # Write your code here to make feature matrix for word_frequency_threshold
    pass


def word_frequency_threshold(training_file, development_file, counts):
    # Write your code to return the training and development accuracy score. Your code should find
    # the best frequency threshold by accuracy, and uses this threshold to classify the
    # training and development set
    training_performance = test_accuracy
    development_performance = development_accuracy
    return training_performance, development_performance


'''
# 3 Naive Bayes and Logistic Regression
For our first actual machine learning classifier, use the built-in Naive Bayes model from sklearn to train 
a classifier. Refer to the sklearn documentation: 
https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html

Some important notes:
-- Since sklearn classifiers take in numpy arrays, convert your lists liks this: `X = np.array([1,2,3,4,5])`
-- Make sure you use this import: `from sklearn.naive_bayes import GaussianNB`
    and `from sklearn.linear_model import LogisticRegression`
-- To train a classifier, you need two numpy arrays:
    1. X_train (m x n), where m is the number of words and n is the nubmer of features for each word
    2. Y (m x 1) for the labels of each of the m words
-- Before training and testing a classifier, it is generally important to normalize your features. 
    This means that you need to find the mean and standard deviation (sd) of a feature. 
    Then, for each row, perform the following transformation:
    X_scaled = (X_original - mean)/sd
    Be sure to always use the means and standard deviations from the training data
'''

# Trains a Naive Bayes classifier using length and frequency features


def naive_bayes(training_file, test_file, counts):
    # TODO: train a Naive Bayes classification model
    # using word length and word frequency as features

    training_performance = training_accuracy
    test_performance = test_accuracy
    return training_performance, test_performance

# Trains a Logistic Regression classifier using length and frequency features


def logistic_regression(training_file, development_file, counts):
    # TODO: train a Logistic Regression classification model

    training_performance = training_accuracy
    test_performance = test_accuracy
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
