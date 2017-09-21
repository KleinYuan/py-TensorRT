import subprocess
import shlex
import os


root_dir = os.getcwd() + '/jetson-inference'
model_fp = '%s/build/aarch64/bin/networks/ped-100/snapshot_iter_70800.caffemodel' % root_dir
prototxt_fp = '%s/build/aarch64/bin/networks/ped-100/deploy.prototxt' % root_dir
flags = ' -- model %s -- prototxt %s' % (model_fp, prototxt_fp)
command = '%s/build/aarch64/bin/detectnet-camera %s' % (root_dir, flags)
args = shlex.split(command)

popen = subprocess.Popen(args, stdout=subprocess.PIPE)

while True:
    output = popen.stdout.readline()
    if output == '' or output is None:
        break
    print '[Info] ', output
