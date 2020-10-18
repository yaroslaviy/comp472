from numpy.lib.function_base import average
from pandas import *
from sklearn.linear_model import Perceptron
from sklearn.metrics import *
from numpy import *
from util import *

# number of dataset to use
dsnum = 2
# read training
training = readFileWithLabel(f'./Dataset/train_{dsnum}.csv')

# initialize PER
clf = Perceptron()
clf.fit(training[0], training[1])

# input test data
input_data = readFileWithLabel(f'./Dataset/test_with_label_{dsnum}.csv')

# get prediction array
result = clf.predict(input_data[0])
output_file = f'./output/PER_DS{dsnum}.csv'
writeResult(result, output_file)

writeMatrix(confusion_matrix(input_data[1], result), output_file)

writePRF(precision_recall_fscore_support(
    input_data[1], result), output_file)


acc_score = accuracy_score(input_data[1], result)
macro_f1 = f1_score(input_data[1], result, average='macro')
weigthed_f1 = f1_score(input_data[1], result, average='weighted')
writeAccuracyAvgF1s([acc_score, macro_f1, weigthed_f1], output_file)
