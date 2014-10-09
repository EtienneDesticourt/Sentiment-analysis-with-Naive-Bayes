'''
Created on 9 Oct 2014
@author: Etienne
'''


"""
4397 good 
4000 great
1337 bad
125 awful
4410
1918
3985
1059
"""

from operator import mul

goodReviewClass = {"good":10,
                   "great":5,
                   "bad":2,
                   "awful":1}

badReviewClass = {"good":2,
                  "great":1,
                   "bad":10,
                   "awful":5}

classes = [goodReviewClass, badReviewClass]

numberOfGoodWords = sum(goodReviewClass.values()) #Doesn't count number of different words, counts total number of words
numberOfBadWords = sum(badReviewClass.values())



goodReview = "great good good good bad bad bad"
badReview = "bad bad bad awful good"



probaGoodClass = 0.5 #1 good review, 2 reviews total 1/2
probaBadClass = 0.5 #1 bad review, 2 reviews total 1/2


def isReviewGood(review,classes):    
    words = review.split(" ")    
    
    probaWordsBelongGoodClass = []
    probaWordsBelongBadClass = []  
    for word in words:
        wordCountGood = float(goodReviewClass[word]) #float to not get a 0 from python 2.6 int/int division                
        probaWordsBelongGoodClass.append(  wordCountGood / numberOfGoodWords   )
        
        
        wordCountBad = float(badReviewClass[word]) 
        probaWordsBelongBadClass.append(  wordCountBad / numberOfBadWords   )    
    
    
    print probaWordsBelongBadClass
    probaGoodReview =  reduce(mul, probaWordsBelongGoodClass)*probaGoodClass #reduce(mul,list) multiplies the elements of list to each others
    probaBadReview =  reduce(mul, probaWordsBelongBadClass)*probaBadClass 
    
    print probaGoodReview
    print probaBadReview
    
    if probaGoodReview>probaBadReview:
        return True
    return False
    
print isReviewGood(goodReview,classes)
print isReviewGood(badReview,classes)
    
    
# #Train
# goodReviewClass = {"good":10,
#                    "great":5,
#                    "bad":2,
#                    "awful":1}
# badReviewClass = {"good":2,
#                   "great":1,
#                    "bad":10,
#                    "awful":5}
# classes = [goodReviewClass, badReviewClass]
# NBC = NBClassifier(classes,2)
# #Test
# goodReview = "great good good good bad bad bad"
# badReview = "bad bad bad awful good"
# testDataset = [ (goodReview,0), (badReview,1)]
# 
# correct = 0.0
# total = len(testDataset)
# for review in testDataset:
#     words = parseReview(review[0])
#     result = NBC.classify(words)
#     if result == review[1]: correct += 1
# 
# accuracy = correct/total*100
# print accuracy
# 
# raw_input("Press enter for full test.")
        