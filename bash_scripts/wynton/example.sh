#### My job
module load Sali anaconda
module load cuda
source activate gtvdn_nn

python tmp.py

#### End-of-job summary, if running as a job
[[ -n "$JOB_ID" ]] && qstat -j "$JOB_ID"
