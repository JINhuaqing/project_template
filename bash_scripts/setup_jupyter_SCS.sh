# useage: source setup_jupyter_SCS.sh
# this file is to lanuch jupyter notebook on SCS server

# load the anaconda module
module load SCS/anaconda/anaconda3
# activate the conda environment
conda activate xxxx
# launch the jupyter notebook
jupyter notebook --config ~/jupyter_notebook_config_xxxx.py