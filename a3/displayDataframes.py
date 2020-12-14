import pandas as pd

### TEST SET ###
# Declare the test set dataframe provided of 55 instances
df1 = pd.read_csv("../472a3/covid_test_public.tsv", sep="\t", nrows=55, header=None) # header=None will label each column with numbers ranging from 0 to length-1

# Label the columns as in the assignment
df1.rename({0:"tweet_id", 1:"text", 2:"q1_label", 3:"q2_label", 4:"q3_label", 5:"q4_label", 6:"q5_label", 7:"q6_label", 8:"q7_label"}, axis='columns', inplace=True)

# Only select classification label-1 (all its labels are binary: Fact = yes, notFact = no)
xdf1 = df1[["tweet_id", "text", "q1_label"]]

# All columns
#display(df1)

# Only required columns
#display(xdf1)





### TRAINING SET ###
# Declare the test set dataframe provided of 400 instances
df2 = pd.read_csv("../472a3/covid_training.tsv", sep="\t", nrows=400, header=0) # header=0 will take the first row as the labels of each column

# Only select classification label-1 (all its labels are binary: Fact = yes, notFact = no)
xdf2 = df2[["tweet_id", "text", "q1_label"]]

# All columns
#display(df2)

# Only required columns
#display(xdf2)