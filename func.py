import numpy as np
def score_align(p):
    odd=(1-p)/p
    dff_score=20*(np.log(odd)-np.log(15))/np.log(2)
    return int(np.round(660+dff_score))
