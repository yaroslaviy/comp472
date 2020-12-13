from collections import Counter
import numpy
import re


class MultinomialNaiveBayes:
    def __init__(self):
        self.counts = {}
        self.classes = ("yes", "no")

    def fit(self, dataTrain):
        self.yesTweets = dataTrain[dataTrain.q1_label == "yes"]          #Len(yesTweets) will give you total number of tweets classified as yes same for noTweets
        self.noTweets = dataTrain[dataTrain.q1_label == "no"]
        yesVoc = getvocabulary(self.yesTweets)
        self.counts['yes']['total'] = len(yesVoc)
        self.counts['yes'] = dict(Counter(yesVoc))
        noVoc = getvocabulary(self.noTweets)
        self.counts['no']['total'] = len(noVoc)
        self.counts['no'] = dict(Counter(noVoc))
        self.counts['grandTotal'] = dataTrain.shape()[0]

    def calculateProb(self, text, className):
        prob = numpy.log10(self.count[className]) - \
            numpy.log10(self.count[className])

    def getMetrics(self, fact, pred):
        # put metrics func here                                  
        TP = len(self.yesTweets); TN = len(self.noTweets);               
        FP = 0;              FN=0;                                 #FP are predictions wrongly classified as yes,  FN are predictions wrongly classified as no

        for i in range(len(fact)):
            if fact[i] == "no" and pred[i] == "yes":               # If Real is no and prediction classifies as yes then increment FP
                FP += 1
            elif fact[i] == "yes" and pred[i] == "no":             # If Real is yes and prediction classifies as no then increment FN
                FN += 1

        accuracy = (TP + TN)/(TP + TN + FP + FN)                   #Accuracy = TP + TN / (TP + TN + FP + FN)

        yes_P = (TP/(TP + FP))                                     #Precision = TP / (TP + FP) , calculate for both yes and no class
        no_P  = (TN/(TN + FN))

        yes_R = (TP/(TP + FN))                                     #Recall = TP/ (TP + FN), calculate for both yes and no class.
        no_R  = (TN/(TN + FP))
        
        yes_F = (2*(yes_P * yes_R)/(yes_P + yes_R))                #F1-Measure = 2(Precision * Recall)/(Precision + Recall)
        no_F  = (2*(no_P * no_R)/(no_P + no_R))
        return None


def getvocabulary(data):
    # Make text columns into a list of tweets
    tweets = data["text"].tolist()
    # Turn tweets to lower case
    lower_case_tweets = []
    for i in tweets:
        lower_case_tweets.append(i.lower())

    # Remove spaces
    split_tweets = []
    for i in lower_case_tweets:
        # (r"[^a-zA-Z0-9]", " ", i) in case you want to ignore punctuation
        split_tweets.append(re.sub(r"\s+", " ", i))

    # Tokenize tweet list
    nested_voc = []
    for i in split_tweets:
        nested_voc.append(i.split())

    # flatten list
    vocabulary = [item for sublist in nested_voc for item in sublist]
    return vocabulary
