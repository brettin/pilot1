#!/bin/bash

export HOME=/lustre/beagle2/brettin 

export PATH=/lustre/beagle2/lpBuild/CANDLE/python/Python-2.7.12-inst/bin:/soft/torque/2.5.7/sbin:/soft/torque/2.5.7/bin:/soft/moab/6.1.1/bin:/soft/moab/6.1.1/sbin:/soft/ci/sbin:/soft/ci/bin:/opt/cray/rca/1.0.0-2.0502.53711.3.125.gem/bin:/opt/cray/pmi/5.0.7-1.0000.10678.155.29.gem/bin:/opt/toolworks/totalview.8.14.1-8/bin:/opt/totalview-support/1.2.0.3/bin:/opt/cray/pe/cce/8.5.4/cray-binutils/x86_64-pc-linux-gnu/bin:/opt/cray/pe/cce/8.5.4/craylibs/x86-64/bin:/opt/cray/pe/cce/8.5.4/cftn/bin:/opt/cray/pe/cce/8.5.4/CC/bin:/opt/cray/craype/2.4.2/bin:/opt/cray/llm/default/bin:/opt/cray/llm/default/etc:/opt/cray/xpmem/0.1-2.0502.55507.3.2.gem/bin:/opt/cray/dmapp/7.0.1-1.0502.9501.5.211.gem/bin:/opt/cray/ugni/5.0-1.0502.9685.4.24.gem/bin:/opt/cray/udreg/2.3.2-1.0502.9275.1.25.gem/bin:/opt/cray/lustre-cray_gem_s/2.5_3.0.101_0.31.1_1.0502.8394.15.1-1.0502.19897.18.2/sbin:/opt/cray/lustre-cray_gem_s/2.5_3.0.101_0.31.1_1.0502.8394.15.1-1.0502.19897.18.2/bin:/opt/cray/alps/5.2.1-2.0502.9072.13.1.gem/sbin:/opt/cray/alps/5.2.1-2.0502.9072.13.1.gem/bin:/opt/cray/sdb/1.0-1.0502.55976.5.27.gem/bin:/opt/cray/nodestat/2.2-1.0502.53712.3.109.gem/bin:/opt/modules/3.2.10.3/bin:/usr/local/bin:/usr/bin:/bin:/usr/bin/X11:/usr/X11R6/bin:/usr/games:/opt/kde3/bin:/usr/lib/mit/bin:/usr/lib/mit/sbin:.:/usr/lib/qt3/bin:/opt/cray/bin:/home/brettin/bin 

python --version 

export PYTHONPATH=/lustre/beagle2/lpBuild/CANDLE/python/Python-2.7.12-inst/lib/python2.7:/lustre/beagle2/lpBuild/CANDLE/python/Python-2.7.12-inst/lib/python2.7/site-packages

echo PYTHONPATH:$PYTHONPATH

function_to_fork() {
  top -b -n 60 -d 60  >> $PBS_JOBID.top
}
function_to_fork &

python -u ./oversampletest.py SMOTE .01 > run_oversampletest.$PBS_JOBID.result 2>&1
