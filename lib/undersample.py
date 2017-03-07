import sys
from imblearn.under_sampling import RandomUnderSampler
from imblearn.under_sampling import TomekLinks

def undersample(X, y, bal_strategy):
	print 'Shape of X: ', X.shape
	print 'Shape of y_Train: ', y.shape

	if(bal_strategy == "RANDOM" or bal_strategy == "ALL"):
		# apply random under-sampling
		rus = RandomUnderSampler()
		X_sampled, y_sampled = rus.fit_sample(X, y)

		print 'Shape of X_sampled: ', X_sampled.shape
		print 'Shape of y_sampled: ', y_sampled.shape

	elif(bal_strategy == "TOMEK" or bal_strategy == "ALL"):
		# Apply Tomek Links cleaning
		tl = TomekLinks()
		X_sampled, y_sampled = tl.fit_sample(X, y)

		print 'Shape of X_sampled: ', X_sampled.shape
		print 'Shape of y_sampled: ', y_sampled.shape

	elif(bal_strategy == 'NONE'):
		X_sampled = X
		y_sampled = y

		print 'Shape of X_sampled: ', X_sampled.shape
		print 'Shape of y_sampled: ', y_sampled.shape

	else:
		print 'bal_stragegy not in ALL, RANDOM, TOMEK, NONE'
		sys.exit(1)

	return (X_sampled, y_sampled)

