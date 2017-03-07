from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import ADASYN
import sys
import numpy as np


def oversample(X, y, bal_strategy):

	if(bal_strategy == "SMOTESVN"  or bal_strategy == "ALL"):
		# Apply SMOTE SVM
		sm = SMOTE(kind='svm')
		X_sampled, y_sampled = sm.fit_sample(X, y)

		print 'Shape of X_sampled: ', X_sampled.shape
		print 'Shape of y_sampled: ', y_sampled.shape

	elif(bal_strategy == "SMOTE"  or bal_strategy == "ALL"):
		# Apply regular SMOTE
		sm = SMOTE(kind='regular')
		X_sampled, y_sampled = sm.fit_sample(X, y)

		print 'Shape of X_sampled: ', X_sampled.shape
		print 'Shape of y_sampled: ', y_sampled.shape

	elif(bal_strategy == "ADASYN"  or bal_strategy == "ALL"):
	# Apply the random over-sampling
		ada = ADASYN()
		X_sampled, y_sampled = ada.fit_sample(X, y)

		print 'Shape of X_sampled: ', X_sampled.shape
		print 'Shape of y_sampled: ', y_sampled.shape

	elif(bal_strategy == 'NONE'):
		X_sampled = X
		y_sampled = y

		print 'Shape of X_sampled: ', X_sampled.shape
		print 'Shape of y_sampled: ', y_sampled.shape

	else:
		print 'bal_stragegy not in SMOTESVN, SMOTE, ADASYN, ALL, NONE'
		sys.exit(1)


	return (X_sampled, y_sampled)
