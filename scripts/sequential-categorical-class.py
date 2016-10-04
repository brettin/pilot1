#!/usr/bin/env python

import numpy as np
import sys

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils

from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score
from sklearn.pipeline import Pipeline

if (len(sys.argv) != 3):
	print 'requires arg1=X_fname and arg2=Y_fname'
	sys.exit(1)
 
X_fname = sys.argv[1] 
Y_fname = sys.argv[2]


print 'X_train file is "', X_fname
print 'y_train file is "', Y_fname


X_train = np.loadtxt(open(X_fname, "rb"), dtype=float, delimiter='\t')
Y_train = np.loadtxt(open(Y_fname, "rb"), dtype=int, delimiter='\t')


print 'Shape of X_train: ', X_train.shape
print 'Shape of Y_Train: ', Y_train.shape


encoder = LabelEncoder()
encoder.fit(Y_train)				# internally map labels to ints.
encoded_Y = encoder.transform(Y_train)		# get int representation of labels.
dummy_Y = np_utils.to_categorical(encoded_Y)	# get binary class matrix for use
						# with categorical_crossentropy.

# print Y_train
# print encoded_Y
# print dummy_Y
print 'Shape of one-hot-encoding: ', dummy_Y.shape


# fix random seed for reproducibility
seed = 7
np.random.seed(seed)


# define baseline model
def baseline_model():

	# create model: the input_dim of the first layer is the number of features.
	#               the output_dim of the last layer is the number of classes.
	#		using sigmoid function in last layer gives probablities 0-1
	#		and can be used as predicted probablities.
	model = Sequential()
	model.add(Dense(6, input_dim=10, init='normal', activation='relu'))
	model.add(Dense(4, init='normal', activation='sigmoid'))

	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model


# create model
estimator = KerasClassifier(build_fn=baseline_model, nb_epoch=200, batch_size=5, verbose=0)

# define the model evaluation procedure to be k-Fold Cross Validation
# set the number of folds to be 10 and to shuffle the data before partitioning it.
kfold = KFold(n=len(X_train), n_folds=10, shuffle=True, random_state=seed)

# evaluate our model (estimator) on our dataset using a 10-fold cross validation
results = cross_val_score(estimator, X_train, dummy_Y, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.sctd()*100))
