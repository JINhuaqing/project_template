import numpy as np


# eig decomp with sorted results by the mode of eigvals
def eig_sorted(mat):
    eigVals, eigVecs = np.linalg.eig(mat)
        # sort the eigvs and eigvecs
    sidx = np.argsort(-np.abs(eigVals))
    eigVals = eigVals[sidx]
    eigVecs = eigVecs[:, sidx]
    return eigVals, eigVecs
