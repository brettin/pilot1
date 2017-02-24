import sys
import numpy as np
import undersample as us

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.optimizers import SGD
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils

from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

X_fname      = '/vagrant/pilot1/problem_dirs/ByType.2/X.little.unb'
y_fname      = '/vagrant/pilot1/problem_dirs/ByType.2/y.little.unb'
bal_strategy = 'RANDOM' 
learn_rate   = 0.01
dropout      = 0.1
nb_epoch=50


# write the command line args to output
print "Using ", X_fname, " as data"
print "Using ", y_fname, " as labels"
print "Using ", bal_strategy, " as undersample strategy"
print "Using ", learn_rate, " as the learning rate"
print "Using ", nb_epoch, " as the number of epochs"
print "Using ", dropout, " as the dropout rate"

X = np.loadtxt(open(X_fname, "rb"), dtype=float, delimiter='\t')
y = np.loadtxt(open(y_fname, "rb"), dtype=int, delimiter='\t')

print 'Shape of X: ', X.shape
print 'Shape of y: ', y.shape


# balance using undersampling technique
X_resampled, y_resampled = us.undersample(X, y, bal_strategy)

# split the sample into training and test data
X_train, X_test, y_train, y_test = train_test_split(  X_resampled, y_resampled, test_size=0.33, random_state=42)

print 'Shape of X_train: ', X_train.shape
print 'Shape of y_train: ', y_train.shape
print 'Shape of X_test: ', X_test.shape
print 'Shape of y_test: ', y_test.shape


# one hot encode y
encoder = LabelEncoder()
encoder.fit(y_train)
y_encoded = encoder.transform(y_train)
y_onehot = np_utils.to_categorical(y_encoded)

encoder.fit(y_test)
y_test_encoded = encoder.transform(y_test)
y_test_onehot = np_utils.to_categorical(y_test_encoded)


# get the input diminsion for the first layer and output dim for last layer
input_dim = X_train.shape[1]
output_dim = np.unique(y_train).shape[0]

print 'input_dim: ', input_dim
print 'output_dim: ', output_dim

# define baseline model
def baseline_model(optimizer=SGD, learn_rate=.01, output_dim=0, input_dim=0, dropout=.1):
	opt = SGD(lr=learn_rate)
	print "Using ", learn_rate, " as the learning rate"
	print "Using ", dropout, " as the dropout rate"

	model = Sequential()
	model.add(Dense(2000, input_dim=input_dim, init='normal', activation='sigmoid'))
	model.add(Dropout(dropout))
	model.add(Dense(200, init='normal', activation='sigmoid'))
	model.add(Dropout(dropout))
	model.add(Dense(output_dim, init='normal', activation='sigmoid'))
	
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
	return model


baseline_model = baseline_model(SGD, learn_rate, output_dim, input_dim, dropout)
baseline_model.fit(X_train, y_onehot, nb_epoch=nb_epoch, batch_size=32, verbose=1)
scores = baseline_model.evaluate(X_test, y_test_onehot)
print("%s: %.2f%%" % (baseline_model.metrics_names[1], scores[1]*100))
