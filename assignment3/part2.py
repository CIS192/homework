"""
    CIS 192 Python Programming
    Do not distribute. Collaboration is permitted with one person.
"""

from collections import defaultdict
import gzip


"""
    Section 0: Data
"""


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


"""
    Section 1: Evaluation Metrics
"""


def get_accuracy(predictions, labels):
    # TODO: write your code to calculate the accuracy of the predicted labels,
    # according to the true labels that are provided.
    pass


"""
    Section 2: Baseline Models
"""


def all_complex(test_file):
    # TODO: write your code here to return the accuracy performance score
    # of the baseline model that classifies each instance as being complex.
    pass


def word_length_threshold(train_file, test_file):
    # TODO: write your code here to classify words based on their length
    # and a given threshold. e.g. if the threshold is 9, any words with
    # less than 9 characters will be labeled simple, and any words with 9
    #  characters or more will be labeled complex.

    # Write your code to return the training and testing accuracy score. Your
    # code should find the best length threshold by accuracy, and uses this
    # threshold to classify the training and test set.

    return training_performance, test_performance


def word_frequency_threshold(train_file, test_file, counts):
    # TODO: write your code to return the training and development
    # accuracy score. Your code should find the best frequency threshold by
    # accuracy, and uses this threshold to classify the training
    # and testing set.

    return training_performance, development_performance


"""
    Section 3: Machine Learning Models
"""


def naive_bayes(train_file, test_file, counts):
    # TODO: train a Naive Bayes classification model

    return training_performance, test_performance


def logistic_regression(train_file, test_file, counts):
    # TODO: train a Logistic Regression classification model

    return training_performance, test_performance


if __name__ == "__main__":
    train_file = "data/complex_words_training.txt"
    test_file = "data/complex_words_test.txt"

    train_data = load_file(training_file)
    test_file = load_file(test_file)

    # should take around 20 seconds due to size
    ngram_counts_file = "data/ngram_counts.txt.gz"
    counts = load_ngram_counts(ngram_counts_file)

    # TODO: your testing code here
