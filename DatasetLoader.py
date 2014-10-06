'''
Created on 1 Oct 2014
Loads the dataset into a list usable by the review parser.
@author: Etienne
'''

import os


def loadReview(path):
    f = open(path)
    data = f.read()
    f.close()
    return data


def loadDataset(paths):
    dataset = []
    
    sentiment = 0
    for path in paths:
        reviewNames = os.listdir(path)
        for name in reviewNames:
            data = loadReview(path+"\\"+name)
            dataset.append( (data,sentiment) )
        sentiment += 1
        
    return dataset