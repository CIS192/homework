""" CIS 192 Python Programming 
    Do not distribute. 
"""


'''
# Problem 1. Text Analysis

The task of taking text data and making it usable is tricky and can sometimes be time consuming.  
Today, we'll keep it pretty simple.

1. First, open the text file `raven.txt`, and copy its contents into a single string.
2. Then, remove any character that isn't a letter, `\n`, or punctuation. 
3. `split` the text by "sentence" (more likely by line for this particular text file).  
    The "sentences" will become the rows of your dataset, and the occurrence of certain words will be your columns.  
    It might help to further `split` your sentences by word.
4. Create a dataset from this based upon whether the words `of`, `nothing`, `raven`, and/or `chamber` 
    appear in each sentence: each entry in your dataset will be `0` 
    (this word/column **not** in this sentence/row) or `1` (this word/column appears in this sentence/row).
5. Output your dataset to a CSV, named `*raven.csv*`.

To build your dataset and export as CSV, feel free to use Python packages such as CSV 
(https://docs.python.org/3/library/csv.html) or Pandas (https://pandas.pydata.org/docs/).
'''

# Write your code for Problem 1 here

'''
Problem 2. NLTK and Tokenizing
The below code preprocesses text in the form of strings by removing capitalization. 
It also tokenizes the test into an array of words by removing punctuation. 
Your task is to complete the tokenize(text) function below this code to complete a common tokenizer function. 
The output should have the filtered and stemmed tokens from the Washington text. 
Feel free to look things up on the NLTK documentation: https://www.nltk.org/.
'''


'''
Installing Packages
Make sure you install the necessary pip packages for this assignment and the code below runs properly. 
Feel free to add in your own imports here.
'''




import nltk
import string
from collections import Counter
from nltk.corpus import inaugural
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import RegexpTokenizer
def get_tokens():
    ''' Returns a list of lowercase strings representing the tokens for input str `text`. 
    The regex automatically removes punctuation for you.
    '''
    text = inaugural.raw('1789-Washington.txt')
    text = text.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    return tokens


def tokenize():
    '''Given input str `text`, return a list of lowercase, no punctuation, filtered, and stemmed tokens. 
    Make sure you use `get_tokens()`.
    '''
    pass


'''
Problem 3. Implementing TF-IDF For Two Texts
Machine learning algorithms cannot work with raw text directly. Rather, the text must be converted into vectors 
of numbers. In natural language processing (NLP), a common technique for extracting features from text is to 
place all of the words that occur in the text in a bucket. This approach is called a bag of words model (BoW). 
In BoW, any information about the structure of the sentence is lost. In this assignment, you will implement 
TF-IDF, a numerical statistic that is intended to reflect how important a word is to a document in a collection 
or corpus. Make sure your complete each function in order for the final implementation of TFIDF to work.
'''


def get_bow(document1, document2):
    '''Return the bag of words set for str `document1` and str `document2` using `document.split(' ')` 
    to tokenize each document. No need to deal with text cleaning, punctuation, etc. 
    e.g. get_bow('hello world', 'hello cis192')
    returns {'cis192', 'hello', 'world'}
    '''
    bow1 = document1.split(' ')  # bag of words for document1
    bow2 = document2.split(' ')  # bag of words for document2
    pass


def get_word_counts(document, bow):
    ''' For input str `document`, output a dictionary containing each word in bow and its count according to 
    the given document. 
    e.g. get_word_counts('hello world', {'hello', 'world', 'cis192'})
    returns {'cis192': 0, 'hello': 1, 'world': 1} 
    '''
    pass


def compute_tf(d, bow):
    ''' For a given dictionary of words and their counts `d` (output of get_word_counts), as well as the 
    bag of words `bow`, output a dictionary of the TF score for each word in BoW.
    For information about tf-df, refer to: http://www.tfidf.com/.
    Your output should contain the TF scores for each word in BoW for the given word counts of a document.
    '''
    pass


def compute_idf(documents):
    '''For a given list of documents represented as a dictionary of BoW words and their counts 
    (from get_word_counts), return the IDF dictionary for each word in BoW. Each document in documents 
    should have the same keys (each word in BoW).
    '''
    pass


def compute_tfidf(document_tf, idfs):
    '''
    Finally, given the TF dictionary for each word in BoW for a particular document, and the idf dictionary 
    for each word in BoW, return the tdidf dictionary
    e.g. 
    document1 = 'hello world'
    document2 = 'hello cis192'
    bow = get_bow(document1, document2)
    d1 = get_word_count(document1, bow)
    d2 = get_word_count(document2, bow)
    print(compute_tfidf(compute_tf(d1, bow), compute_idf([d1, d2])))
    # should print {'cis192': 0.0, 'hello': 0.0, 'world': 0.34657359027997264} 
    print(compute_tfidf(compute_tf(d2, bow), compute_idf([d1, d2])))
    # should print {'cis192': 0.34657359027997264, 'hello': 0.0, 'world': 0.0}
    What do you notice about words with low or 0 tf-idf scores in both documents?
    '''
    pass
