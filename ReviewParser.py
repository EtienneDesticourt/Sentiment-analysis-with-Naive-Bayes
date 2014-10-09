'''
Created on 1 Oct 2014
Handles parsing reviews and sorting words in the neg and pos classes.
@author: Etienne
'''
import re

    
def parseReview(review):
    review = review.lower() #For now we ignore the difference between Great, GREAT and great.
    #Split by sentence to avoid linking unrelated words if I decide to get higher dimensional features later on.
    punctuation = re.compile("[?.!]") #Should probably add parentheses handling later
    sentences = punctuation.split(review)
    
    #We don't care for word repetition in a single review
    words = []
    
    for sentence in sentences:
        for word in sentence.split(" "):
            if word not in words: words.append(word)
    return words

def parseDataset(dataset):        
    classes = [{},{}] #positive,negative        
    
    for (review,sentiment) in dataset:
        #sentiment -> 0:positive, 1:negative
        words = parseReview(review)
        for word in words:
            try:
                classes[sentiment][word] += 1
            except KeyError:
                classes[sentiment][word] = 1
                
    return classes