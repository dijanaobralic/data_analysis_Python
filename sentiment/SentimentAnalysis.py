# text mining in social media
# the basic task of SA is classifying a review as positive or negative
# text classification methods using machine learning can be divided in to supervised and unsupervised learning

import nltk
# national language toolkit

import random
import pickle
import json


from nltk.tokenize import word_tokenize
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode


class listener(StreamListener):
