from pandas import *


def writeResult(result, path):
    result_df = DataFrame(result)

    # make index start from 1
    result_df.index += 1

    # write result to csv
    result_df.to_csv(path, header=None)


def readFileWithLabel(pathToFile):
    df = read_csv(pathToFile, sep=',', header=None)
    result = df.iloc[:, 1024].to_numpy()
    data = df.drop(df.columns[1024], axis=1).to_numpy()
    return (data, result)
