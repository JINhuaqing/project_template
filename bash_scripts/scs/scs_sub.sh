#!/bin/bash
#### sbatch scs_sub.sh to submit the job

#### Job memory request
#SBATCH --mem=200gb                  
#SBATCH --nodes=1
#### Num of cores required, I think I should use --cpus-per-task other than --ntasks
#SBATCH --cpus-per-task=30
#####SBATCH --ntasks=30
#### Run on partition "dgx" (e.g. not the default partition called "long")
### long for CPU, gpu/dgx for CPU, dgx is slow
#SBATCH --partition=gpu                    
#### Allocate 1 GPU resource for this job. 
#SBATCH --gres=gpu:teslav100:1   
#SBATCH --output=scs/logs/prefix-%x-%j.out
#SBATCH -J (job_name)
#SBATCH --chdir=/you path/bash_scripts/

(some job)

#### You job
echo "Running prime number generator program on $SLURM_CPUS_ON_NODE CPU cores"


