from collections import Counter
import numpy
import re


class MultinomialNaiveBayes:
    def __init__(self):
        self.counts = {}
        self.classes = ("yes", "no")

    def fit(self, dataTrain):
        yesTweets = dataTrain[dataTrain.q1_label == "yes"]
        noTweets = dataTrain[dataTrain.q1_label == "no"]
        yesVoc = getvocabulary(yesTweets)
        self.counts['yes']['total'] = len(yesVoc)
        self.counts['yes'] = dict(Counter(yesVoc))
        noVoc = getvocabulary(noTweets)
        self.counts['no']['total'] = len(noVoc)
        self.counts['no'] = dict(Counter(noVoc))
        self.counts['grandTotal'] = dataTrain.shape()[0]

    def calculateProb(self, text, className):
        prob = numpy.log10(self.count[className]) - \
            numpy.log10(self.count[className])

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
