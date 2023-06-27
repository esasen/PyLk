from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import numpy

compile_args = ['-g', '-std=c++17', '-stdlib=libc++']
cmdclass = {}
ext_modules = []

cmdclass.update({'build_ext': build_ext})
ext_modules+=cythonize([Extension("pylk._writhemap_cython", ["pylk/_writhemap_cython.pyx"], include_dirs=[numpy.get_include()])])

# ~ ext_modules+=cythonize("pylk/cythonWM.pyx"),include_dirs=[numpy.get_include()]
# ~ compile_args = ['-g', '-std=c++17', '-stdlib=libc++']

setup(name='PyLk',
      version='0.0.1',
      description='A package to calculate linking properties of polymer configurations',
      url='https://github.com/esasen/IOPolyMC',
      author='Enrico Skoruppa',
      author_email='enrico.skoruppa@gmail.com',
      license='MIT',
      packages=['pylk'],
      install_requires=[
          'numpy',
          'numba',
          'cython',
          'scipy'
      ],
      zip_safe=False,
      ext_modules=ext_modules,
      cmdclass=cmdclass,
      compile_args=compile_args
      )

