import numpy as np
from ._writhemap_numba  import wmn_writhemap_klenin1a
from ._writhemap_python import wmp_writhemap_klenin1a
try:
    from ._writhemap_cython import wmc_writhemap_klenin1a
    CYTHON_INCLUDED = True
    DEFAULT_METHOD = 'cython'
except ModuleNotFoundError:
    CYTHON_INCLUDED = False
    DEFAULT_METHOD = 'numba'
    
WM_METHODS = ['klenin1a']

def writhemap(config,method='klenin1a',implementation=DEFAULT_METHOD):
    
    if method not in WM_METHODS:
        raise ValueError(f"Method '{method}' not implemented")
    
    if implementation == 'cython' and not CYTHON_INCLUDED:
        raise ModuleNotFoundError("No module named 'pylk._writhemap_cython'")
    
    if method == 'klenin1a':
        if implementation   == 'cython':
            print('cython')
            return np.asarray(wmc_writhemap_klenin1a(config))
        elif implementation == 'numba':
            print('numba')
            return wmn_writhemap_klenin1a(config)
        elif implementation == 'python':
            return wmp_writhemap_klenin1a(config)
        else:
            raise ValueError(f"Invalid implementation '{implementation}' for method '{method}'")
