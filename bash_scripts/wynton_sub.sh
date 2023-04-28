#!/bin/bash
#### The job script, run it as qsub xxx.sh 

#### the shell language when run via the job scheduler [IMPORTANT]
#$ -S /bin/bash
#### job should run in the current working directory
#$ -cwd
#### Specify job name
#$ -N wake_R
#### Output file
#$ -o $JOB_NAME_$JOB_ID.out
#### Error file
#$ -e $JOB_NAME_$JOB_ID.err
#### memory per core
#$ -l mem_free=2G
#### number of cores 
#$ -pe smp 1
#### Maximum run time 
#$ -l h_rt=10:00:00
#### job requires up to 2 GB local space
#$ -l scratch=2G
#### Specify queue
###  gpu.q for using gpu
###  if not gpu.q, do not need to specify it
#$ -q gpu.q 
#### The GPU memory required, in MiB
### #$ -l gpu_mem=12000M


#### My job
module load Sali anaconda
module load cuda
source activate gtvdn_nn

python tmp.py

#### End-of-job summary, if running as a job
[[ -n "$JOB_ID" ]] && qstat -j "$JOB_ID"
