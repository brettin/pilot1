import numpy as np
import sys

if (len(sys.argv) != 3):
	print 'requires arg1=X_fname and arg2=y_fname'
	sys.exit(1)
 
X_fname = sys.argv[1] 
y_fname = sys.argv[2]

X = np.loadtxt(open(X_fname, "rb"), dtype=float, delimiter='\t')
y = np.loadtxt(open(y_fname, "rb"), dtype=int, delimiter='\t')

print X.shape
print y.shape

input_dim = X.shape[1]
output_dim = np.unique(y).shape[0]

print 'input_dim: ', input_dim
print 'output_dim: ', output_dim

np.savetxt('X.save', X, delimiter="\t", fmt='%s')
np.savetxt('y.save', y, delimiter="\t", fmt='%s')
