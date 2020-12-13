from bowNoSkl import original_voc
from collections import Counter
import numpy
import re


class MultinomialNaiveBayes:
    def __init__(self, voc):
        self.original = voc
        self.counts = {}
        self.classes = ("yes", "no")

    def fit(self, dataTrain):
        yesTweets = dataTrain[dataTrain.q1_label == "yes"]
        noTweets = dataTrain[dataTrain.q1_label == "no"]
        yesVoc = getvocabulary(yesTweets)
        self.counts['yes']['total'] = len(yesVoc)
        noVoc = getvocabulary(noTweets)
        self.counts['no']['total'] = len(noVoc)
        self.counts['yes'] = dict(Counter(yesVoc))
        self.counts['no'] = dict(Counter(noVoc))
        if not self.original:
            self.counts['yes'] = filterVoc(dict(Counter(yesVoc)))
            self.counts['no'] = filterVoc(dict(Counter(noVoc)))
        self.counts['grandTotal'] = dataTrain.shape()[0]

    def calculateProb(self, text, className):
        prob = numpy.log10(self.count[className]/self.count['grandtotal'])
        text_arr = text.split()
        for word in text_arr:
            if word in self.counts[className]:
                word_prob = numpy.log10(
                    self.counts[className][word]/self.counts[className]['total'])
            else:
                word_prob = numpy.log10(
                    0.01/(self.counts[className]['total']+0.01))
            prob += word_prob
        return prob

    def predictOne(self, point):
        yesProb = self.calculateProb(point, 'yes')
        noProb = self.calculateProb(point, 'no')
        if yesProb > noProb:
            return 'yes'
        else:
            return 'no'

    def predict(self, data):
        pred = []
        for text in data:
            pred.append(self.predictOne(text))
        return pred

    def getMetrics(self, fact, pred):
        # put metrics func here
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


def filterVoc(original_voc):
    newDict = dict()
    for key, val in original_voc.items():
        if(val != 1):
            newDict[key] = val
    return newDict
