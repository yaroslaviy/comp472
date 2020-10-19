from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import PredefinedSplit
from sklearn.metrics import accuracy_score, confusion_matrix, precision_recall_fscore_support, f1_score
from numpy import concatenate
from util import *

# number of dataset to use
dsnum = 1
# read training
training = readFileWithLabel(f'./Dataset/train_{dsnum}.csv')
val = readFileWithLabel(f'./Dataset/val_{dsnum}.csv')
# initialize PER
X_grid = concatenate((training[0], val[0]))
y_grid = concatenate((training[1], val[1]))
separation_boundary = [-1 for _ in training[1]] + [0 for _ in val[1]]
ps = PredefinedSplit(separation_boundary)

param_grid = {
    'activation': ['logistic', 'identity', 'tanh', 'relu'],
    'hidden_layer_sizes': [(40, 40), (15, 15, 15)],
    'solver': ['adam', 'sgd']
}

clf = GridSearchCV(MLPClassifier(), param_grid=param_grid, cv=ps, n_jobs=-1)
model = clf.fit(X_grid, y_grid)


# input test data
input_data = readFileWithLabel(f'./Dataset/test_with_label_{dsnum}.csv')

# get prediction array
result = clf.predict(input_data[0])
output_file = f'./output/BestMLP_DS{dsnum}.csv'
writeResult(result, output_file)

writeMatrix(confusion_matrix(input_data[1], result), output_file)

writePRF(precision_recall_fscore_support(
    input_data[1], result), output_file)


acc_score = accuracy_score(input_data[1], result)
macro_f1 = f1_score(input_data[1], result, average='macro')
weigthed_f1 = f1_score(input_data[1], result, average='weighted')
writeAccuracyAvgF1s([acc_score, macro_f1, weigthed_f1], output_file)
