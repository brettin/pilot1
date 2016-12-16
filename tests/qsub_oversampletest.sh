#!/bin/bash

#PBS -N pilot1
#PBS -q batch
#PBS -l advres=brettin.3672
#PBS -l walltime=12:00:00

export HOME=/lustre/beagle/$(whoami)
cd $PBS_O_WORKDIR


# Initialize the module script
. /opt/modules/default/init/bash
module list 2>&1

module swap PrgEnv-cray PrgEnv-gnu

# Change environmental variables
export TMP=/tmp
export pyvers=2.7.12
export myCC=gcc
export myCXX=g++
export sqlitedir=/soft/CANDLE/lib/sqlite3
export pyInst=/lustre/beagle2/lpBuild/CANDLE/python/Python-2.7.12-inst
export LD_LIBRARY_PATH=$pyInst/lib:$LD_LIBRARY_PATH
export INSTALLDIR=$pyInst

echo "calling /opt/cray/alps/5.2.1-2.0502.9072.13.1.gem/bin/aprun -d 32 /lustre/beagle2/brettin/KERAS/pilot1/run_oversampletest.sh"
/opt/cray/alps/5.2.1-2.0502.9072.13.1.gem/bin/aprun -d 32 /lustre/beagle2/brettin/KERAS/test-scripts/run_oversampletest.sh

