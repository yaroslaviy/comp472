import pandas as pd
import string, re
import pprint
from nltk.tokenize import word_tokenize
from collections import Counter

# Declare the training set dataframe provided of 400 instances
dfTraining = pd.read_csv("../472a3/covid_training.tsv", sep="\t", nrows=400, header=0)

# Only select classification label-1
#xdf2 = dfTraining[["tweet_id", "text", "q1_label"]]
xdf2 = dfTraining[["text", "q1_label"]]
display(xdf2)

# Make text columns into a list of tweets
tweets = dfTraining["text"].tolist()

# Turn tweets to lower case
lower_case_tweets = []
for i in tweets:
    lower_case_tweets.append(i.lower())

# Remove spaces
split_tweets = []
for i in lower_case_tweets:
    split_tweets.append(re.sub(r"\s+", " ", i)) # (r"[^a-zA-Z0-9]", " ", i) in case you want to ignore punctuation
    
# Tokenize tweet list
vocabulary = []
for i in split_tweets:
    vocabulary.append(word_tokenize(i))

# 'Counter' counts the occurrences of each item in the list and returns a dictionary
frequency_list = []
for i in vocabulary:
    frequency_list.append(dict(Counter(i)))
#pprint.pprint(frequency_list) # this will print alphabetically
display(frequency_list) # this will print as it is