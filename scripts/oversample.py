from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import ADASYN
import sys
import numpy as np


def oversample(X_train, y_train, bal_strategy):

	if(bal_strategy == "SMOTESVN"  or bal_strategy == "ALL"):
		# Apply SMOTE SVM
		sm = SMOTE(kind='svm')
		X_resampled, y_resampled = sm.fit_sample(X_train, y_train)

		print 'Shape of X_resampled: ', X_resampled.shape
		print 'Shape of y_resampled: ', y_resampled.shape

	elif(bal_strategy == "SMOTE"  or bal_strategy == "ALL"):
		# Apply regular SMOTE
		sm = SMOTE(kind='regular')
		X_resampled, y_resampled = sm.fit_sample(X_train, y_train)

		print 'Shape of X_resampled: ', X_resampled.shape
		print 'Shape of y_resampled: ', y_resampled.shape

	elif(bal_strategy == "ADASYN"  or bal_strategy == "ALL"):
	# Apply the random over-sampling
		ada = ADASYN()
		X_resampled, y_resampled = ada.fit_sample(X_train, y_train)

		print 'Shape of X_resampled: ', X_resampled.shape
		print 'Shape of y_resampled: ', y_resampled.shape

	elif(bal_strategy == 'NONE'):
		X_resampled = X_train
		y_resampled = y_train

		print 'Shape of X_resampled: ', X_resampled.shape
		print 'Shape of y_resampled: ', y_resampled.shape

	else:
		print 'bal_stragegy not in SMOTESVN, SMOTE, ADASYN, ALL, NONE'
		sys.exit(1)


	return (X_resampled, y_resampled)
