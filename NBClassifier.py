'''
Created on 1 Oct 2014
Implements the Naive Bayes algorithm.
@author: Etienne
'''


from operator import mul


class NBClassifier:
    def __init__(self,classes,datasetLength):
        self.classes = classes
        self.datasetLength = datasetLength
        #Prior probability
        self.probaPosClass = float(len(classes[0])) / ( len(classes[0]) + len(classes[1]) ) 
        self.probaNegClass = float(len(classes[1])) / ( len(classes[0]) + len(classes[1]) )
        #number of tokens in each class
        self.numbPosWords = len(self.classes[0])#Number of different words, not total number of words.
        self.numbNegWords = len(self.classes[1])#
        self.numbWords = [self.numbPosWords,self.numbNegWords]
        
    def getWordListProbability(self,words,sentiment):
#         numbWords = len(self.classes[sentiment])
        numbWords = self.numbWords[sentiment]
        wordProba = []
        for word in words:            
            try: #25 000 reviews dataset I assume it will encompass almost every "reviewy" word hence 'try' instead of 'if in'
                count = self.classes[sentiment][word]
            except KeyError:
                count = 0.5
                
            wordProba.append(float(count)/numbWords)
        return wordProba
    
    def classify(self,reviewWords,v=False):
        wordProbaPos = self.getWordListProbability(reviewWords,0) 
        wordProbaNeg = self.getWordListProbability(reviewWords,1)
        
        probaPosReview =  reduce(mul, wordProbaPos)*self.probaPosClass
        probaNegReview =  reduce(mul, wordProbaNeg)*self.probaNegClass 
        
        
        
        if v:
            print "wordProbaPos:",wordProbaPos 
            print "wordProbaNeg:",wordProbaNeg 
            print "probaPosReview",probaPosReview 
            print "probaNegReview",probaNegReview 
        
        
        if probaNegReview > probaPosReview: return 1
        
        return 0
        