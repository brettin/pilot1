from imblearn.under_sampling import RandomUnderSampler


def undersample(X_train, y_train, bal_strategy):
	print 'Shape of X_train: ', X_train.shape
	print 'Shape of y_Train: ', y_train.shape

	if(bal_strategy == "RANDOM" or bal_strategy == "ALL"):
		# apply random under-sampling
		rus = RandomUnderSampler()
		X_resampled, y_resampled = rus.fit_sample(X_train, y_train)

		print 'Shape of X_resampled: ', X_resampled.shape
		print 'Shape of y_resampled: ', y_resampled.shape

	elif(bal_strategy == "TOMEK" or bal_strategy == "ALL"):
		# Apply Tomek Links cleaning
		tl = TomekLinks()
		X_resampled, y_resampled = tl.fit_sample(X, y)

		print 'Shape of X_resampled: ', X_resampled.shape
		print 'Shape of y_resampled: ', y_resampled.shape

	elif(bal_strategy == 'NONE'):
		X_resampled = X_train
		y_resampled = y_train

		print 'Shape of X_resampled: ', X_resampled.shape
		print 'Shape of y_resampled: ', y_resampled.shape

	else:
		print 'bal_stragegy not in ALL, RANDOM, TOMEK, NONE'
		sys.exit(1)

	return (X_resampled, y_resampled)

