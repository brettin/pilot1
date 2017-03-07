import oversample as osmpl
import undersample as usmpl
import sys

def sample(X, y, bal_strategy="NONE"):

	if (bal_strategy == "SMOTESVN"  or bal_strategy == "SMOTE" or bal_strategy == "ADASYN"):
		X_resampled, y_resampled = osmpl.oversample(X, y, bal_strategy)

	elif( bal_strategy == "RANDOM" or bal_strategy == "TOMEK" 
		X_resampled, y_resampled = usmpl.oversample(X, y, bal_strategy)

	elif(bal_strategy == 'NONE'):
		X_resampled = X
		y_resampled = y

	else:
		print 'bal_stragegy not in SMOTESVN, SMOTE, ADASYN, ALL, NONE'
		print 'bal_stragegy not in ALL, RANDOM, TOMEK, NONE'
		sys.exit(1)

	return (X_resampled, y_resampled)
