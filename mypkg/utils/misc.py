import numpy as np
import pickle
from easydict import EasyDict as edict


# load file from folder and save it to dict
def load_pkl_folder2dict(folder, vars_=None):
    res = edict()
    for fil in folder.glob('*.pkl'):
        if vars_ is None:
            res[fil.stem] = load_pkl(fil)
        else:
            if fil.stem in vars_:
                res[fil.stem] = load_pkl(fil)
    return res

# save a dict into a folder
def save_pkl_dict2folder(folder, res, is_force=False):
    assert isinstance(res, dict)
    for ky, v in res.items():
        save_pkl(folder/f"{ky}.pkl", v, is_force=is_force)


# load file from pkl
def load_pkl(fil):
    print(f"Load file {fil}")
    with open(fil, "rb") as f:
        result = pickle.load(f)
    return result

# save file to pkl
def save_pkl(fil, result, is_force=False):
    if not fil.parent.exists():
        fil.parent.mkdir()
        print(fil.parent)
        print(f"Create a folder {fil.parent}")
    if is_force or (not fil.exists()):
        print(f"Save to {fil}")
        with open(fil, "wb") as f:
            pickle.dump(result, f)
    else:
        print(f"{fil} exists! Use is_force=True to save it anyway")
