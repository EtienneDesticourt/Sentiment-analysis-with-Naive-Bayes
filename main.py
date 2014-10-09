'''
Created on 1 Oct 2014
@author: Etienne
'''

from NBClassifier import NBClassifier
from ReviewParser import parseDataset, parseReview
from DatasetLoader import loadDataset, loadReview

import os, random

TRAINPATHS = ["E:\\Program Files\\Dev\\workspace\\Sentiment analysis with Naive Bayes\\aclImdb\\train\\pos",
         "E:\\Program Files\\Dev\\workspace\\Sentiment analysis with Naive Bayes\\aclImdb\\train\\neg"]

TESTPATHS = ["E:\\Program Files\\Dev\\workspace\\Sentiment analysis with Naive Bayes\\aclImdb\\test\\pos",
         "E:\\Program Files\\Dev\\workspace\\Sentiment analysis with Naive Bayes\\aclImdb\\test\\neg"]




#Train
import time
start = time.time()
dataset = loadDataset(TRAINPATHS)
classes = parseDataset(dataset)
print time.time()-start
print len(classes[0])+len(classes[1])
NBC = NBClassifier(classes,len(dataset))

#Test
testDataset = loadDataset(TESTPATHS)

correct = 0.0
total = len(testDataset)
for review in testDataset:
    words = parseReview(review[0])
    result = NBC.classify(words)
    if result == review[1]: correct += 1
            

accuracy = correct/total*100
print accuracy

