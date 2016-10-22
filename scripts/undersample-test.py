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

# muck with command line args
if (len(sys.argv) < 4):
	print 'requires arg1=X_fname and arg2=Y_fname and bal_strategy'
	sys.exit(1)

X_fname      = sys.argv[1]
y_fname      = sys.argv[2]
bal_strategy = sys.argv[3]
learn_rate   = sys.argv[4]
# optimizer   = sys.argv[5]

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


# set up the optimizer TODO: look into sweeping over optimizers
optimizer = SGD(lr=learn_rate)


# define baseline model
def baseline_model(opt):
	model = Sequential()
	# opt = SGD(lr=learn_rate)
	model.add(Dense(2000, input_dim=60483, init='normal', activation='sigmoid'))
	model.add(Dropout(.10))
	model.add(Dense(200, init='normal', activation='sigmoid'))
	model.add(Dropout(.10))
	model.add(Dense(2, init='normal', activation='sigmoid'))
	
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
	return model


baseline_model = baseline_model(optimizer)
baseline_model.fit(X_train, y_onehot, nb_epoch=5, batch_size=32, verbose=1)
scores = baseline_model.evaluate(X_test, y_test_onehot)
print("%s: %.2f%%" % (baseline_model.metrics_names[1], scores[1]*100))

