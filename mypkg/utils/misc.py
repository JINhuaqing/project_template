import numpy as np
import pickle
from easydict import EasyDict as edict
import logging

def _set_verbose_level(verbose, logger):
    """Set the verbose level of logger
    """
    if verbose == 0:
        verbose_lv = logging.ERROR
    elif verbose == 1:
        verbose_lv = logging.WARNING
    elif verbose == 2:
        verbose_lv = logging.INFO
    elif verbose == 3:
        verbose_lv = logging.DEBUG
    if len(logger.handlers)>0:
        logger.handlers[0].setLevel(verbose_lv)
    else:
        logger.setLevel(verbose_lv)

def _update_params(input_params, def_params, logger):
    """Update the default parameters with input parameters
    args: 
        - input_params (dict): the input parameters
        - def_params (dict): the default parameters
        - logger (logging.Logger): the logger
    """
    for ky, v in input_params.items():
        if ky not in def_params.keys():
            logger.warning(f"Check your input, {ky} is not used.")
        else:
            if v is not None:
                def_params[ky] = v
    return edict(def_params)


def load_pkl_folder2dict(folder, excluding=[], including=["*"], verbose=True):
    """The function is to load pkl file in folder as an edict
        args:
            folder: the target folder
            excluding: The files excluded from loading
            including: The files included for loading
            Note that excluding override including
    """
    if not isinstance(including, list):
        including = [including]
    if not isinstance(excluding, list):
        excluding = [excluding]
        
    if len(including) == 0:
        inc_fs = []
    else:
        inc_fs = list(set(np.concatenate([list(folder.glob(nam+".pkl")) for nam in including])))
    if len(excluding) == 0:
        exc_fs = []
    else:
        exc_fs = list(set(np.concatenate([list(folder.glob(nam+".pkl")) for nam in excluding])))
    load_fs = np.setdiff1d(inc_fs, exc_fs)
    res = edict()
    for fil in load_fs:
        res[fil.stem] = load_pkl(fil, verbose)                                                                                                                                  
    return res

# save a dict into a folder
def save_pkl_dict2folder(folder, res, is_force=False, verbose=True):
    assert isinstance(res, dict)
    for ky, v in res.items():
        save_pkl(folder/f"{ky}.pkl", v, is_force=is_force, verbose=verbose)

# load file from pkl
def load_pkl(fil, verbose=True):
    if verbose:
        print(f"Load file {fil}")
    with open(fil, "rb") as f:
        result = pickle.load(f)
    return result

# save file to pkl
def save_pkl(fil, result, is_force=False, verbose=True):
    if not fil.parent.exists():
        fil.parent.mkdir()
        if verbose:
            print(fil.parent)
            print(f"Create a folder {fil.parent}")
    if is_force or (not fil.exists()):
        if verbose:
            print(f"Save to {fil}")
        with open(fil, "wb") as f:
            pickle.dump(result, f)
    else:
        if verbose:
            print(f"{fil} exists! Use is_force=True to save it anyway")
        else:
            pass
