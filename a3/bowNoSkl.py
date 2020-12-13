import pandas as pd
import re
from collections import Counter
import numpy


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


# Declare the training set dataframe provided of 400 instances
dfTraining = pd.read_csv("./covid_training.tsv", sep="\t",
                         nrows=400, header=0, encoding="ISO-8859-1")

# Only select classification label-1
#xdf2 = dfTraining[["tweet_id", "text", "q1_label"]]
xdf2 = dfTraining[["text", "q1_label"]]


vocabulary = getvocabulary(dfTraining)

# count occurences
count_dict = Counter(vocabulary)

#print(count_dict)

# removed dupes
original_voc = []
[original_voc.append(x) for x in vocabulary if x not in original_voc]

# filtered unique
filter_voc = numpy.copy(original_voc)
filter_voc = filter_voc.tolist()

for key, val in count_dict.items():
    if(val == 1):
        filter_voc.remove(key)


print(len(filter_voc))
print(len(original_voc))
print(len(vocabulary))

yesTweets = dfTraining[dfTraining.q1_label == "yes"]    # len(yesTweets) will give you total number of "yes"
noTweets = dfTraining[dfTraining.q1_label == "no"]      # len(noTweets) will give you total number of "no"
yesVoc = getvocabulary(yesTweets)
yesCounters = Counter(yesVoc)
noVoc = getvocabulary(yesTweets)
noCounters = Counter(noVoc)
#print(noCounters)
#print(yesCounters)
print(len(noTweets))

# Used to get the total number of "yes" and "no" classes in the training set.  # of Yes > # of no
#label_count = dfTraining["q1_label"].tolist()
#yes_count = 0
#no_count = 0

#for label in label_count:
#    if label == "yes": yes_count += 1
#    else: no_count +=1 

#print("Number of yes in training: " + str(yes_count) + ", number of no: " + str(no_count))  #Used to get TP/TN
