from collections import Counter
import numpy
import math
import re
from decimal import Decimal


class MultinomialNaiveBayes:
    def __init__(self, voc):
        self.original = voc
        self.counts = {"yes": {}, "no": {}}
        self.classes = ("yes", "no")
        self.vocabulary = []
        if self.original:
            self.writeFile = open('./output/trace NB-BOW-OV.txt', 'w')
        else:
            self.writeFile = open('./output/trace NB-BOW-FV.txt', 'w')

    def fit(self, dataTrain):
        # Len(yesTweets) will give you total number of tweets classified as yes same for noTweets
        bow = getvocabulary(dataTrain)
        [self.vocabulary.append(x)
         for x in bow if x not in self.vocabulary]
        self.yesTweets = dataTrain[dataTrain.q1_label == "yes"]
        self.noTweets = dataTrain[dataTrain.q1_label == "no"]
        yesVoc = getvocabulary(self.yesTweets)
        noVoc = getvocabulary(self.noTweets)
        self.counts['yes'] = dict(Counter(yesVoc))
        self.counts['no'] = dict(Counter(noVoc))
        if not self.original:
            self.counts['yes'] = filterVoc(dict(Counter(yesVoc)))
            self.counts['no'] = filterVoc(dict(Counter(noVoc)))
            self.vocabulary = filterVocabulary(self.vocabulary, bow)
        self.counts['yes']['totalWordsInDataSet'] = len(yesVoc)
        self.counts['no']['totalWordsInDataSet'] = len(noVoc)
        self.counts['grandTotal'] = dataTrain.shape[0]

    def calculateProb(self, text, className):
        if className == "yes":
            prob = math.log10(len(self.yesTweets) /
                              len((self.yesTweets+self.noTweets)))
        else:
            prob = math.log10(len(self.noTweets) /
                              len((self.yesTweets+self.noTweets)))

        text_arr = text.split()
        for word in text_arr:
            word = word.lower()
            if word in self.vocabulary:
                if word in self.counts[className]:
                    word_prob = math.log10(
                        (self.counts[className][word]+0.01)/(self.counts[className]['totalWordsInDataSet'] + 0.01*len(self.vocabulary)))
                else:
                    word_prob = math.log10(
                        0.01/(self.counts[className]['totalWordsInDataSet'] + 0.01*len(self.vocabulary)))
                prob += word_prob
        return prob

    def predictOne(self, point):
        yesProb = self.calculateProb(point, 'yes')
        noProb = self.calculateProb(point, 'no')
        if yesProb > noProb:
            self.writeFile.write("yes  " + '%.2E' %
                                 Decimal(yesProb) + "  ")
            return 'yes'
        else:
            self.writeFile.write("no  " + '%.2E' %
                                 Decimal(noProb) + "  ")
            return 'no'

    def predict(self, dataF):
        pred = []
        dataArray = dataF.to_numpy()
        for i in range(dataF.shape[0]):
            self.writeFile.write(str(dataArray[i][0]) + "  ")
            prediction = self.predictOne(dataArray[i][1])
            self.writeFile.write(str(dataArray[i][2]) + "  ")
            if(prediction == dataArray[i][2]):
                self.writeFile.write("correct\n")
            else:
                self.writeFile.write("wrong\n")

            pred.append(prediction)
        self.writeFile.flush()
        self.writeFile.close()
        return pred

    def getMetrics(self, fact, pred):
        # put metrics func here
        TP = 0
        TN = 0
        FP = 0
        FN = 0  # FP are predictions wrongly classified as yes,  FN are predictions wrongly classified as no

        for i in range(len(fact)):
            # If Real is no and prediction classifies as yes then increment FP
            if fact[i] == "no" and pred[i] == "yes":
                FP += 1
            # If Real is yes and prediction classifies as no then increment FN
            elif fact[i] == "yes" and pred[i] == "no":
                FN += 1
            # If Real is yes and prediction is same then increment TP
            elif fact[i] == "yes" and pred[i] == "yes":
                TP += 1
            else:                                                  # If Real is no and prediction is also no then increment TN
                TN += 1

        # Accuracy = TP + TN / (TP + TN + FP + FN)
        accuracy = (TP + TN)/(TP + TN + FP + FN)

        # Precision = TP / (TP + FP) , calculate for both yes and no class
        yes_P = (TP/(TP + FP))
        no_P = (TN/(TN + FN))

        # Recall = TP/ (TP + FN), calculate for both yes and no class.
        yes_R = (TP/(TP + FN))
        no_R = (TN/(TN + FP))

        # F1-Measure = 2(Precision * Recall)/(Precision + Recall)
        yes_F = (2*(yes_P * yes_R)/(yes_P + yes_R))
        no_F = (2*(no_P * no_R)/(no_P + no_R))
        return {"accuracy": accuracy, "yes_P": yes_P, "no_P": no_P, "yes_R": yes_R, "no_R": no_R, "yes_F": yes_F, "no_F": no_F}


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


def filterVocabulary(original_voc, full_voc):
    filter_voc = numpy.copy(original_voc)
    filter_voc = filter_voc.tolist()
    count_dict = dict(Counter(full_voc))
    for key, val in count_dict.items():
        if(val == 1):
            filter_voc.remove(key)
    return filter_voc
