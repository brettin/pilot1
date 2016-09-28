#!/usr/bin/env python

import numpy as np
import sys, getopt
import pandas

from keras.models import Sequential
from keras.layers import Dense

from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score
from sklearn.pipeline import Pipeline
from keras.wrappers.scikit_learn import KerasClassifier


# fix random seed for reproducibility
seed = 7
np.random.seed(seed)


# Load dataset using pandas because iris.csv contains strings and floats
# First create a dataframe which is a 2D size mutable heterogenous table
# Then call values on the dataframe to get a numpy ND frame and cast to numpy.dtype
# 
# 5.1,3.5,1.4,0.2,Iris-setosa
# 4.9,3.0,1.4,0.2,Iris-setosa
# 4.7,3.2,1.3,0.2,Iris-setosa

dataframe = pandas.read_csv("iris.csv", header=None)
dataset = dataframe.values
X = dataset[:,0:4].astype(float)
Y = dataset[:,4]

# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)					# internally map labels to ints.
encoded_Y = encoder.transform(Y)		# get int representation of labels.
dummy_y = np_utils.to_categorical(encoded_Y)	# convert integers to dummy variables 
						# (i.e. one hot encoded)
						# get binary class matrix for use
						# with categorical_crossentropy.

print 'Shape of X: ', X.shape
print 'Shape of y: ', Y.shape
print 'Shape of one-hot encoding: ', dummy_y.shape

# define baseline model
# dim = X.shape[1]
def baseline_model():
	# create model
	model = Sequential()
	model.add(Dense(4, input_dim=4, init='normal', activation='relu'))
	model.add(Dense(3, init='normal', activation='sigmoid'))
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model


estimator = KerasClassifier(build_fn=baseline_model, nb_epoch=200, batch_size=5, verbose=0)
print "estimator parameters: ", estimator.get_params()

# define the model evaluation procedure to be k-Fold Cross Validation
# set the number of folds to be 10 and to shuffle the data before partitioning it.
kfold = KFold(n=len(X), n_folds=10, shuffle=True, random_state=seed)

# evaluate our model (estimator) on our dataset using a 10-fold cross validation
results = cross_val_score(estimator, X, dummy_y, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
