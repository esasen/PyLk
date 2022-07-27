import numpy as np
import pylk
import time
import iopolymc

implementation='python'
implementation='numba'
implementation='cython'

# compile
R = np.zeros([100,3])
R[:,0] = 1
wm = pylk.writhemap(R,implementation=implementation)

N = 2
if implementation=='numba':
    N = 100
if implementation=='cython':
    N = 100

state = iopolymc.load_state('test.state')
configs = state['pos']

print(f'running {N} calculations')
t1 = time.time()
for i in range(N):
    wm = pylk.writhemap(configs[-1],implementation=implementation)
t2 = time.time()
print(f'Wr = {np.sum(wm)}')
print('done')
print(f'elapsed time: {(t2-t1)/N}')
