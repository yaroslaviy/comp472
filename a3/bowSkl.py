import pandas as pd
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer

# Declare the training set dataframe provided of 400 instances
dfTraining = pd.read_csv("./covid_training.tsv", sep="\t", nrows=400, header=0)

# Only select classification label-1
xdf2 = dfTraining[["tweet_id", "text", "q1_label"]]

# Make text columns into a list of tweets
tweets = dfTraining["text"].tolist()

# Implementing Bag-Of-Words with sklearn
vect = CountVectorizer()
vect.fit(tweets)
# each word will be a column of the matrix
feat_names = vect.get_feature_names()
doc_array = vect.transform(tweets)
doc_array.toarray()
frequency_matrix = pd.DataFrame(doc_array.toarray(), columns=feat_names)

# pd.options.print.max_columns = None # BE CAREFUL: These 2 lines will remove the limits of the nb# of rows & columns that will print
# pd.options.print.max_rows = None # so it may freeze you computer & take longer to print

print(frequency_matrix)
