import numpy as np

class NaiveBayes():

    def __init__(self, X, y):
        self.num_of_tweets, self.num_of_features = X.shape
        self.num_of_labels = len(np.unique(y))
        self.delta = 0.01           # delta used for smoothing purposes 


    def fit(self, X):
        self.classes_mean = {}
        self.classes_var = {}
        self.classes_prior = {}


        for x in range(self.num_of_labels):

        self.classes_prior[str(c)] = X_class.shape[0]/self.num_of_features  # Divide frequency of word by total number of words in vocab to get priors for each word.

    
    def predict(self, X):
        prob = np.zeros((self.num_of_tweets, self.num_of_class))        #Track probability of each tweet depending on class and in the end choose the bigger one 