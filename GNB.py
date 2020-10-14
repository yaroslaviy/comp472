from pandas import *
from sklearn.naive_bayes import GaussianNB
from numpy import *

# function to import and format csv files. Returns a pair of data and expected result for each row


def readFileWithLabel(pathToFile):
    df = read_csv(pathToFile, sep=',', header=None)
    result = df.iloc[:, 1024].to_numpy()
    data = df.drop(df.columns[1024], axis=1).to_numpy()
    return (data, result)


# read training
training = readFileWithLabel('./Dataset/train_1.csv')

# initialize GNB
clf = GaussianNB()
clf.fit(training[0], training[1])

# input validation data
input_data = readFileWithLabel('./Dataset/val_1.csv')

# get prediction array
result = clf.predict(input_data[0])
