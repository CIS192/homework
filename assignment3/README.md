# CIS 192 Homework 3
> Due March 3rd, 2020 at 11:59 PM. You may work in groups of up to 2 people.

## Part 1: NLP Basics


## Part 2: Text Classification with Sci-Kit Learn
> Adapted from CIS 530 - Computational Linguistics

The second part of the homework will be a longer project: building a text classifier. Now that we have seen tokenizing, text cleaning, and word importance with TF-IDF, let's train a text classifier that will be able to classify a word as being simple (e.g. *easy*, *act*, *blue*) or complex (e.g. *ostentatious*, *esoteric*, *aberration*). This is an important step in a larger NLP task to simply texts to make text more readable. 

In the provided code template with proveded helper and unimplemented functions, you will need to:
0. Look at the dataset! Try to understand the information that is conveyed to better understand the task.
1. Implement the machine learning evaluation metric we discussed in class (accuracy).
2. Perform data pre-processing for our dataset. You will need to parse the provided pre-labeled data in training/test sets, and implement a simple baseline model.
3. Use the Sci-Kit Learn package to train machine learning models which classify words as simple or complex.

### Datasets
We have provided the dataset of labelled words split between training/test sets in (.txt) format. Some notes on the dataset:

1. The training set is disjoint, so a word in `complex_words_training.txt` will not appear in the other two.
2. Stop-words and proper nouns are already removed, leaving only nouns, verbs, and adjectives.
3. There are 4,000 training words, and 922 testing words.
4. The relevant columns are WORD (the word to be classified), and LABEL (0 for simple, 1 for complex). Note that LABEL is not included in the test dataset.

We have also provided frequencies (a contiguous sequence of 1 item from a given sample of text or speech) from the [Google N-Gram Corpus](https://books.google.com/ngrams/info). This is to provide you another feature for classification. Consider why this extra information is useful for distinguishing between simple and complex words.

### Submission
You will be submitting your implementations for the functions in the template code and your model output for the test set to Gradescope. If you have a partner, YOU MUST MARK THEM AS A COLLABORATOR ON GRADESCOPE. If you fail to do this, you may get a 0 on this assignment.
