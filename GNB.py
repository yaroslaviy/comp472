from pandas import *
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import *
from numpy import *
from util import writeResult, readFileWithLabel

# function to import and format csv files. Returns a pair of data and expected result for each row


# read training
training = readFileWithLabel('./Dataset/train_1.csv')

# initialize GNB
clf = GaussianNB()
clf.fit(training[0], training[1])

# input test data
input_data = readFileWithLabel('./Dataset/test_with_label_1.csv')

# get prediction array
result = clf.predict(input_data[0])

writeResult(result, './output/GNB_DS1.csv')

matrix_df = DataFrame(confusion_matrix(input_data[1], result))

# make index start from 1
matrix_df.index += 1

# write result to csv
matrix_df.to_csv('./output/GNB_DS1.csv', mode='a', header=list(range(1, 27)))

prf = precision_recall_fscore_support(training[1], result)
