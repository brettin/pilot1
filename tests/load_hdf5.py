import h5py
import numpy as np
import sys
import os
import h5loader

# We assume the problem directory specification.
# We further assume that the basename of the HDF5
# file is the same as the name of the problem dir.
# Finally, we assume that the HDF5 file has an
# extension identifying it as a HDF5 file. Recommended
# extensions include .h5 and .hdf5.

hdf_fname = sys.argv[1]
X, y = h5loader.h5load(hdf_fname)

print 'loaded h5 file  : ', hdf_fname
print 'Done reading X with shape: ', X.shape
print 'Done reading y with shape: ', y.shape
