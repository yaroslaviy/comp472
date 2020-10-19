from pandas import DataFrame, read_csv, Index
from numpy import array, delete


def readFileWithLabel(pathToFile):
    df = read_csv(pathToFile, sep=',', header=None)
    result = df.iloc[:, 1024].to_numpy()
    data = df.drop(df.columns[1024], axis=1).to_numpy()
    return (data, result)


def writeResult(result, path):
    result_df = DataFrame(result)

    # make index start from 1
    result_df.index += 1

    # write result to csv
    result_df.to_csv(path, header=None)


def writeMatrix(cmatrix, path):
    f = open(path, "a")
    f.write("\nConfusion Matrix\n")
    f.close()

    matrix_df = DataFrame(cmatrix)

    # make index start from 1
    matrix_df.index += 1

    # write result to csv
    matrix_df.to_csv(path, mode='a',
                     header=matrix_df.index)


def writePRF(prf, path):
    f = open(path, "a")
    f.write('\n')
    f.close()
    # remove support from array
    prf = delete(array(prf), 3, 0)
    index_label = Index(["Precision", "Recall", "F-score"], name="")
    prf_df = DataFrame(prf, index=index_label)

    # write result to csv
    prf_df.to_csv(path, mode='a',
                  header=list(range(1, prf[0].size+1)))


def writeAccuracyAvgF1s(af1, path):
    f = open(path, "a")
    f.write('\n')
    f.close()
    # remove support from array
    index_label = Index(["Accuracy", "Macro-average f1",
                         "Weighted-average f1"], name="")
    prf_df = DataFrame(af1, index=index_label)

    # write result to csv
    prf_df.to_csv(path, mode='a',
                  header=None)
