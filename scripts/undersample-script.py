import sys
import numpy as np
import undersample as us

if (len(sys.argv) != 4):
	print 'requires arg1=X_fname and arg2=Y_fname and bal_strategy'
	sys.exit(1)

X_fname      = sys.argv[1]
y_fname      = sys.argv[2]
bal_strategy = sys.argv[3]


X_train = np.loadtxt(open(X_fname, "rb"), dtype=float, delimiter='\t')
y_train = np.loadtxt(open(y_fname, "rb"), dtype=int, delimiter='\t')

print 'Shape of X_train: ', X_train.shape
print 'Shape of y_Train: ', y_train.shape

X_balanced, y_balanced = us.undersample(X_train, y_train, bal_strategy)

X_balfname = X_fname + "_bal"
y_balfname = y_fname + "_bal"

np.savetxt( X_balfname, X_balanced, delimiter='\t')
np.savetxt( y_balfname, y_balanced, delimiter='\t')
