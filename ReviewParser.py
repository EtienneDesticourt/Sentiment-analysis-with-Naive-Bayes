'''
Created on 1 Oct 2014
Handles parsing reviews and sorting words in the neg and pos classes.
@author: Etienne
'''
import re,csv


#List compiled from parsing original reviews and looking at the most frequent words
WORTHLESSWORDS=[',','(',')','\"','might', 'anyone', 'once', 'goes', 'however,', 'our', 'am', 'nothing', 'away', '/>this', 'comedy', 'rather', 'having', 'fact', 'although', 'far', 'yet', 'takes', 'enough', 'music', 'whole', 'wonderful', "isn't", "that's", 'job', 'worth', 'comes', 'true', 'played', 'found', 'interesting', 'shows', 'plays', ')', 'beautiful', 'fun', 'probably', 'different', 'family', 'done', 'pretty', '"', "can't", 'funny', 'since', 'last', 'feel', 'each', 'especially', 'it,', 'long', 'gets', "i've", 'times', 'thought', 'seems', 'director', 'right', 'thing', 'down', 'excellent', 'almost', 'want', 'role', 'around', 'big', 'must', 'bad', "i'm", 'come', 'give', 'got', 'again', 'bit', 'why', 'without', 'take', 'us', 'going', 'things', 'saw', '/>i', 'part', 'movie,', 'may', 'look', 'now', 'between', 'own', 'another', 'though', 'watching', 'same', 'young', 'always', 'here', 'something', 'show', 'before', 'scene', 'scenes', 'lot', 'both', 'say', 'should', 'off', 'film,', 'find', 'man', 'your', 'through', 'end', 'go', 'back', '-0', 'those', 'makes', 'years', 'these', 'over', 'while', 'did', 'ever', 'know', 'movies', 'then', 'films', 'where', 'does', 'any', 'still', 'being', 'could', 'them', 'two', 'too', 'make', 'him', 'seen', 'she', '/>the', 'way', 'after', 'made', 'we', 'because', 'people', 'do', 'many', 'its', 'how', 'been', 'no', 'were', 'me', 'get', 'other', 'her', 'had', 'will', 'also', 'would', 'their', 'which', 'only', 'up', 'time', 'can', 'my', 'see', 'there', "it's", 'what', 'or', 'some', 'if', 'when', 'just', 'they', 'out', 'about', 'so', 'he', 'has', 'who', 'his', 'from', 'by', 'all', 'you', 'at', 'an', 'be', 'have', 'movie', 'film', 'one', 'are', '<br', '/><br', 'on', 'was', 'as', 'but', 'with', 'for', 'i', 'that', 'it', 'this', 'in', 'is', 'to', 'of', 'a', 'and', 'the']

def cleanReview(review):
    #Preparsing word removal
    for word in WORTHLESSWORDS:
        while word in review:
            review = review.replace(word,"")
    return review    

    
def parseReview(review,dim=1):
    review = review.lower() #For now we ignore the difference between Great, GREAT and great.
    review = cleanReview(review)    
    #Split by sentence to avoid linking unrelated words if I decide to get higher dimensional features later on.
    punctuation = re.compile("[?.!]") #Should probably add parentheses handling later
    sentences = punctuation.split(review)
    
    #We don't care for word repetition in a single review
    words = []
    
    if dim == 1:
        for sentence in sentences:
            for word in sentence.split(" "):
                if word not in words: words.append(word)
    elif dim == 2:
        for sentence in sentences:
            for word1 in sentence.split(" "):
                for word2 in sentence.split(" "):
                    words.append(word1+" "+word2)
    else:
        raise ValueError("Dimension argument needs to be either 1 or 2.")
    
    return words


def cleanDataset(dataset): #Only decreases accuracy
    newDataset = [{},{}]
    for i in xrange(len(dataset)):
        for feature in dataset[i]:
            if dataset[i][feature] > 100:
                newDataset[i][feature] = dataset[i][feature]
    return newDataset


def parseDataset(dataset,dim=1):        
    classes = [{},{}] #positive,negative        
    
    for (review,sentiment) in dataset:
        #sentiment -> 0:positive, 1:negative
        words = parseReview(review,dim)
        for word in words:
            try:
                classes[sentiment][word] += 1
            except KeyError:
                classes[sentiment][word] = 1
                
    return classes

def exportClasses(classes): #To get some insight into word frquencies and help with feature selection.
    f = open('features2.csv','wb') #wb to avoid emtpy row every other row
    writer = csv.writer(f)
    #Format in row tuples
    col1=list(classes[0])
    col2=list(classes[0].values())
    rows = zip(col1,col2)
    rows.sort(key=lambda tup: tup[1],reverse=True) #Sort by value
    #Write rows, no write col options
    writer.writerows(rows)
    f.close()
    
    
    
    
    