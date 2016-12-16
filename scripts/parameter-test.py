import sys
import numpy as np
import oversample as osmpl
import undersample as usmpl
import models as mdl

from keras.utils import np_utils

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# muck with command line args allowing one param string 
if (len(sys.argv) == 2):
	args = sys.argv[1].split()
	sys.argv.append(args)

if (len(sys.argv) < 7):
	print 'requires:'
	print 'arg1=X_fname'
	print 'arg2=y_fname'
	print 'arg3=bal_strategy'
	print 'arg4=learn_rate'
	print 'arg5=dropout'
	print 'arg6=optimizer'
	sys.exit(1)


X_fname      = sys.argv[1]
y_fname      = sys.argv[2]
bal_strategy = sys.argv[3]
learn_rate   = sys.argv[4]
dropout      = sys.argv[5]
optimizer    = sys.argv[6]
nb_epoch=50


# write the command line args to output
print "Using ", X_fname, " as data"
print "Using ", y_fname, " as labels"
print "Using ", bal_strategy, " as undersample strategy"
print "Using ", learn_rate, " as the learning rate"
print "Using ", dropout, " as the dropout rate"
print "Using ", optimizer, " as the optimizer"
print "Using ", nb_epoch, " as the number of epochs"

X = np.loadtxt(open(X_fname, "rb"), dtype=float, delimiter='\t')
y = np.loadtxt(open(y_fname, "rb"), dtype=int, delimiter='\t')

# balance using undersampling technique
X_resampled, y_resampled = osmpl.oversample(X, y, bal_strategy)

acc=[]
loss=[]

for i in range(10):
	# split the sample into training and test data
	rs = np.random.randint(10,100)
	X_train, X_test, y_train, y_test = train_test_split(  X_resampled, y_resampled, test_size=0.33, random_state=rs)

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

	args={ 'lr': learn_rate, 'dropout': dropout }

	model = mdl.baseline_model(optimizer, input_dim, output_dim, **args)
	model.fit(X_train, y_onehot, nb_epoch=nb_epoch, batch_size=32, verbose=0)
	scores = model.evaluate(X_test, y_test_onehot)
	print scores
	loss.append(scores[0])
	acc.append(scores[1])

print ("mean acc: %.2f%%" % (np.mean(acc)*100))
print ("mean loss: %.2f%%" %  (np.mean(loss)*100))
