import pandas as pd
import re
from collections import Counter
import numpy

# Declare the training set dataframe provided of 400 instances
dfTraining = pd.read_csv("./covid_training.tsv", sep="\t",
                         nrows=400, header=0, encoding="ISO-8859-1")

# Only select classification label-1
#xdf2 = dfTraining[["tweet_id", "text", "q1_label"]]
xdf2 = dfTraining[["text", "q1_label"]]

# Make text columns into a list of tweets
tweets = dfTraining["text"].tolist()

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

vocabulary = [item for sublist in nested_voc for item in sublist]
count_dict = Counter(vocabulary)

print(count_dict)

original_voc = []
[original_voc.append(x) for x in vocabulary if x not in original_voc]

filter_voc = numpy.copy(original_voc)
filter_voc = filter_voc.tolist()

for key, val in count_dict.items():
    if(val == 1):
        filter_voc.remove(key)


print(len(filter_voc))
print(len(original_voc))
print(len(vocabulary))

# # 'Counter' counts the occurrences of each item in the list and returns a dictionary
# frequency_list = []
# for i in vocabulary:
#     frequency_list.append(dict(Counter(i)))
# # pprint.pprint(frequency_list) # this will print alphabetically
# print(frequency_list)  # this will print as it is
