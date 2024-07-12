import numpy as np
from typing import Tuple
from .eval_link import eval_link

def triads2link(pos: np.ndarray, triads: np.ndarray, radius: float = 1) -> float:
    chain1,chain2 = triads2chain(pos,triads,radius)
    return eval_link(chain1,chain2)

def triads2chain(pos: np.ndarray, triads: np.ndarray, radius: float = 1) -> Tuple[np.ndarray,np.ndarray]:
    chain1 = np.zeros((len(pos),3))
    chain2 = np.zeros((len(pos),3))
    for i in range(len(pos)):
        chain1[i] = pos[i] - triads[i,:,0]*radius
        chain2[i] = pos[i] + triads[i,:,0]*radius
    return chain1,chain2
    
if __name__ == '__main__':
    
    taus = np.load('test/taus.npy')
    triads = taus[:,:3,:3]
    pos = taus[:,3,:3]  

    chain1,chain2 = triads2chain(pos,triads,1)
    
    from .linkingnumber_python import _eval_lk_python
    from .linkingnumber_numba import _eval_lk_numba
    from .linkingnumber_cython import _eval_lk_cython
    
    import time 
    t1 = time.time()
    num = 1
    for i in range(num):
        lk = _eval_lk_python(chain1,chain2)
    t2 = time.time()
    print(f'python dt = {np.round(t2-t1,decimals=3)} ({(t2-t1)/num} s)')
    num = 65
    for i in range(num):
        lk = _eval_lk_numba(chain1,chain2)
    t3 = time.time()
    print(f'numba dt = {np.round(t3-t2,decimals=3)} ({(t3-t2)/num} s)')
    num = 65
    for i in range(num):
        lk = _eval_lk_cython(chain1,chain2)
    t4 = time.time()
    print(f'cython dt = {np.round(t4-t3,decimals=3)} ({(t4-t3)/num} s)')
    print(f'lk = {lk}')
    
    