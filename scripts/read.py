import numpy as np

X_fname = "GDC_downloads/data/ByType.2/X"
y_fname = "GDC_downloads/data/ByType.2/y"
 
X_train = np.loadtxt(open(X_fname, "rb"), dtype=float, delimiter='\t')
y_train = np.loadtxt(open(y_fname, "rb"), dtype=int, delimiter='\t')

print X_train.shape
print y_train.shape

# this is not needed
# X = np.array(X_train, dtype=float, copy=False, order='C')
# y = np.array(y_train, dtype=float, copy=False, order='C')
# 
# print X.shape
# print y.shape
