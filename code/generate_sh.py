# python generate_header_sh.py --gpu 4 --ram 16 --time 24:00:00 --output job.sh
# generate header
import os
import sys
import argparse
import subprocess

# init the parser
parse = argparse.ArgumentParser(description='Generate the header for the bash script.')
parse.add_argument('--gpu', type=int, help='number of gpu', default=4)
parse.add_argument('--ram', type=int, help='number of ram', default=16)
parse.add_argument('--time', type=str, help='time limit', default="24:00:00")
parse.add_argument('--output', type=str, help='output file name', default="job.sh")
args = parse.parse_args()

# variables
gpu = args.gpu
ram = args.ram
time = args.time

# generate the header
header = '''#!/bin/bash
# Grid Engine options (lines prefixed with #$)
# Runtime limit of 24 hour:
#$ -l h_rt=%s
#
# Set working directory to the directory where the job is submitted from:
#$ -cwd
#
# Request one GPU:
#$ -pe gpu-titanx %d
#
# Request 4 GB system RAM
# the total system RAM available to the job is the value specified here multiplied by
# the number of requested GPUs (above)
#$ -l h_vmem=%dG
# Initialise the environment modules and load CUDA version 8.0.61
./etc/profile.d/modules.sh
module load anaconda/5.3.1
source activate python310
module load phys/compilers/gcc/10.1.0
module load cuda/11.0.2
''' % (time, gpu, ram)

# output
with open(args.output, 'w') as f:
    f.write(header)
