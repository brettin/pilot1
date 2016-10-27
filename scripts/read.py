import numpy as np
import sys

if (len(sys.argv) != 3):
	print 'requires arg1=X_fname and arg2=y_fname'
	sys.exit(1)
 
X_fname = sys.argv[1] 
y_fname = sys.argv[2]

X_train = np.loadtxt(open(X_fname, "rb"), dtype=float, delimiter='\t')
y_train = np.loadtxt(open(y_fname, "rb"), dtype=int, delimiter='\t')

print X_train.shape
print y_train.shape

input_dim = X_train.shape[1]
output_dim = np.unique(y_train).shape[0]

print 'input_dim: ', input_dim
print 'output_dim: ', output_dim

# this is not needed
# X = np.array(X_train, dtype=float, copy=False, order='C')
# y = np.array(y_train, dtype=float, copy=False, order='C')
# 
# print X.shape
# print y.shape
