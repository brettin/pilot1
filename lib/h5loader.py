import h5py
import numpy as np
import sys
import os

# We assume the problem directory specification.
# We further assume that the basename of the HDF5
# file is the same as the name of the problem dir.
# Finally, we assume that the HDF5 file has an
# extension identifying it as a HDF5 file. Recommended
# extensions include .h5 and .hdf5.

def h5load(hdf_fname):

	prob_dir, ext = os.path.splitext(os.path.basename(hdf_fname))

	X_fname = '/' + prob_dir + '/X'
	y_fname = '/' + prob_dir + '/y'

	# Read data back from hdf5 file on disk
	f = h5py.File(hdf_fname, "r")
	X = f[X_fname]
	y = f[y_fname]

	return X, y
