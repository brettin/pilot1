from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import ADASYN
import sys
import numpy as np

if (len(sys.argv) != 4):
	print 'requires arg1=X_fname and arg2=Y_fname and bal_strategy'
	sys.exit(1)

X_fname = sys.argv[1]
y_fname = sys.argv[2]
bal_strategy = sys.argv[3]


X_train = np.loadtxt(open(X_fname, "rb"), dtype=float, delimiter='\t')
y_train = np.loadtxt(open(y_fname, "rb"), dtype=int, delimiter='\t')

print 'Shape of X_train: ', X_train.shape
print 'Shape of y_Train: ', y_train.shape




if(bal_strategy == "SMOTESVN"):
	# Apply SMOTE SVM
	sm = SMOTE(kind='svm')
	X_resampled, y_resampled = sm.fit_sample(X_train, y_train)

	print 'Shape of X_resampled: ', X_resampled.shape
	print 'Shape of y_resampled: ', y_resampled.shape

elif(bal_strategy == "SMOTE"):
	# Apply regular SMOTE
	sm = SMOTE(kind='regular')
	X_resampled, y_resampled = sm.fit_sample(X_train, y_train)

	print 'Shape of X_resampled: ', X_resampled.shape
	print 'Shape of y_resampled: ', y_resampled.shape

elif(bal_strategy == "ADASYN"):
	# Apply the random over-sampling
	ada = ADASYN()
	X_resampled, y_resampled = ada.fit_sample(X_train, y_train)

	print 'Shape of X_resampled: ', X_resampled.shape
	print 'Shape of y_resampled: ', y_resampled.shape

else:
	print 'bal_stragegy not in SMOTESVN, SMOTE, ADASYN'
	sys.exit(1)

