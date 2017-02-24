from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

import optimizer

def baseline_model(opt, input_dim, output_dim, **kwargs):
	if 'dropout' in kwargs:
		do_rate = kwargs['dropout']
	else:
		do_rate=.01
	print "using ", do_rate, "as dropout rate"
	model = Sequential()
	model.add(Dense(2000, input_dim=input_dim, init='normal', activation='sigmoid'))
	model.add(Dropout(do_rate))
	model.add(Dense(200, init='normal', activation='sigmoid'))
	model.add(Dropout(do_rate))
	model.add(Dense(output_dim, init='normal', activation='sigmoid'))

	# Create the optimizer
	o = optimizer.opt_builder(opt, **kwargs)
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
	return model
