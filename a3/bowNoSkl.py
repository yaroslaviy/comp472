import pandas as pd
from model import MultinomialNaiveBayes


# Declare the training set dataframe provided of 400 instances
dfTraining = pd.read_csv("./covid_training.tsv", sep="\t",
                         nrows=400, header=0)
dfTest = pd.read_csv("./covid_test_public.tsv", sep="\t",
                     header=None)
# Only select classification label-1
xdf2 = dfTraining[["text", "q1_label"]]
original = MultinomialNaiveBayes(True)
original.fit(xdf2)
fact = dfTest[2].to_numpy()
pred = original.predict(dfTest)
metrics = original.getMetrics(fact, pred)
ofile = open('./output/eval NB-BOW-OV.txt', 'w')
ofile.write(
    f"{metrics['accuracy']}\n{metrics['yes_P']}  {metrics['no_P']}\n{metrics['yes_R']}  {metrics['no_R']}\n{metrics['yes_F']}  {metrics['no_F']}\n")
ofile.flush()
ofile.close()
filtered = MultinomialNaiveBayes(False)
filtered.fit(xdf2)
pred = filtered.predict(dfTest)
metrics = filtered.getMetrics(fact, pred)
ffile = open('./output/eval NB-BOW-FV.txt', 'w')
ffile.write(
    f"{metrics['accuracy']}\n{metrics['yes_P']}  {metrics['no_P']}\n{metrics['yes_R']}  {metrics['no_R']}\n{metrics['yes_F']}  {metrics['no_F']}\n")
ffile.flush()
ffile.close()
