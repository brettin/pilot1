from keras.optimizers import SGD
from keras.optimizers import RMSprop
from keras.optimizers import Adagrad
from keras.optimizers import Adadelta
from keras.optimizers import Adam
from keras.optimizers import Adamax
from keras.optimizers import Nadam

from optimizer_defaults import defaults_for

def OptBuilder(optimizer='SGD',**kwargs):

	print "createing optimizer: ", optimizer
	if (optimizer == "SGD" ):
		vals = _arg_builder(optimizer, kwargs)
		print "preset defaults: ", defaults_for[optimizer]
		print "using params:     ", vals
		opt = SGD(**vals);
	
	if (optimizer == "RMSprop"):
		vals = _arg_builder(optimizer, kwargs)
		print "preset defaults: ", defaults_for[optimizer]
		print "using params:     ", vals
		opt = RMSprop(**vals)
	
	if (optimizer == "Adagrad"):
		vals = _arg_builder(optimizer, kwargs)
		print "preset defaults: ", defaults_for[optimizer]
		print "using params:     ", vals
		opt = Adagrad(**vals)

	if (optimizer == "Adadelta"):
		vals = _arg_builder(optimizer, kwargs)
		print "preset defaults: ", defaults_for[optimizer]
		print "using params:     ", vals
		opt = Adadelta(**vals)

	if (optimizer == "Adam"):
		vals = _arg_builder(optimizer, kwargs)
		print "preset defaults: ", defaults_for[optimizer]
		print "using params:     ", vals
		opt = Adam(**vals)

	if (optimizer == "Adamax"):
		vals = _arg_builder(optimizer, kwargs)
		print "preset defaults: ", defaults_for[optimizer]
		print "using params:     ", vals
		opt = Adamax(**vals)
	
	if (optimizer == "Nadam"):
		vals = _arg_builder(optimizer, kwargs)
		print "preset defaults: ", defaults_for[optimizer]
		print "using params:     ", vals
		opt = Nadam(**vals)
	
	print "Using optimizer: ", opt
	return opt



def _arg_builder(optimizer, kwargs):
	vals = defaults_for[optimizer].copy()
	print 'using vals as defaults: ', vals
	for k, v in kwargs.iteritems():
		if (k in vals):
			vals[k]=v			
	return vals
