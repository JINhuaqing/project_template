#!/bin/bash
#### The job script, run it as qsub wynton_sub.sh

#### the shell language when run via the job scheduler [IMPORTANT]
#$ -S /bin/bash
#### job should run in the current working directory
####$ -cwd
##### set job working directory
#$ -wd  /path/to/bash_scripts/
#### Output file
#$ -o wynton/logs/Realdata_$JOB_NAME_$JOB_ID.out
#### Error file
#$ -e wynton/logs/Realdata_$JOB_NAME_$JOB_ID.err
#### memory per core
#$ -l mem_free=2G
#### number of cores 
#$ -pe smp 1
#### Maximum run time 
#$ -l h_rt=10:00:00
#### job requires up to 2 GB local space
#$ -l scratch=2G
#### Specify queue
###  gpu.q for using gpu, sometimes, long.q can run GPU
###  if not gpu.q, do not need to specify it
#$ -q gpu.q 
#### The GPU memory required, in MiB
### #$ -l gpu_mem=12000M
#### Specify job name
#$ -N wake_R

#Your script

#### End-of-job summary, if running as a job
[[ -n "$JOB_ID" ]] && qstat -j "$JOB_ID"
