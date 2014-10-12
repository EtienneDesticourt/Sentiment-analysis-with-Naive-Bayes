'''
Created on 1 Oct 2014
@author: Etienne
'''

from NBClassifier import NBClassifier
from ReviewParser import parseDataset, parseReview, exportClasses, cleanDataset
from DatasetLoader import loadDataset, loadReview

import os, random

TRAINPATHS = ["C:\\Users\\Etienne\\workspace\\Sentiment-analysis-with-Naive-Bayes\\aclImdb\\train\\pos",
         "C:\\Users\\Etienne\\workspace\\Sentiment-analysis-with-Naive-Bayes\\aclImdb\\train\\neg"]

TESTPATHS = ["C:\\Users\\Etienne\\workspace\\Sentiment-analysis-with-Naive-Bayes\\aclImdb\\test\\pos",
         "C:\\Users\\Etienne\\workspace\\Sentiment-analysis-with-Naive-Bayes\\aclImdb\\test\\neg"]




#Train
dataset = loadDataset(TRAINPATHS)
# print "Done loading"

classes = parseDataset(dataset)
# print "Len before cleaning:", len(classes[0])
# # classes = cleanDataset(classes)
# print "Len after cleaning:", len(classes[0])
# print "Done parsing"

# exportClasses(classes)
# print "Done exporting"

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

