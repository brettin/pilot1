from keras.optimizers import SGD
from keras.optimizers import RMSprop
from keras.optimizers import Adagrad
from keras.optimizers import Adadelta
from keras.optimizers import Adam
from keras.optimizers import Adamax
from keras.optimizers import Nadam

def OptBuilderlr=0.01, momentum=0.0, decay=0.0, nesterov=Falses)
	if (optimizer == "SGD" ):
		opt = SGD(lr=lr, momentum=momentum, decay=decay, nesterov=nesterov);

if (optimizer == "RMSprop" or optimizer == "ALL") ):

if (optimizer == "Adagrad" or optimizer == "ALL") ):

if (optimizer == "Adadelta" or optimizer == "ALL") ):

if (optimizer == "Adam" or optimizer == "ALL") ):

if (optimizer == "Adamax" or optimizer == "ALL") ):

if (optimizer == "Nadam" or optimizer == "ALL") ):

	print "Using optimizer: ", opt;

