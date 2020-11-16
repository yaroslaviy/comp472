from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score, confusion_matrix, precision_recall_fscore_support, f1_score
from numpy import concatenate
from util import *

# number of dataset to use
dsnum = input("Which dataset to use?\n")
# read training
training = readFileWithLabel(f'./Dataset/train_{dsnum}.csv')

# initialize PER
clf = Perceptron()
clf.fit(training[0], training[1])

# input test data
input_data = readFileWithOutLabel(f'./Dataset/34.csv')

# get prediction array
result = clf.predict(input_data)
output_file = f'./output/PER_DEMO{dsnum}.csv'
writeResult(result, output_file)

# writeMatrix(confusion_matrix(input_data[1], result), output_file)

# writePRF(precision_recall_fscore_support(
#     input_data[1], result), output_file)


# acc_score = accuracy_score(input_data[1], result)
# macro_f1 = f1_score(input_data[1], result, average='macro')
# weigthed_f1 = f1_score(input_data[1], result, average='weighted')
# writeAccuracyAvgF1s([acc_score, macro_f1, weigthed_f1], output_file)
