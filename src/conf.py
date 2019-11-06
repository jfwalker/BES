from distutils.core import setup
from Cython.Build import cythonize

#To use change use cython run this: python conf.py build_ext --inplace

setup(
	ext_modules = cythonize("cquartets.pyx")
)
setup(

	ext_modules = cythonize("cbeset.pyx")

)
setup(

	ext_modules = cythonize("cnode.pyx")

)
setup(


	ext_modules = cythonize("cstats.pyx")

)
setup(


	ext_modules = cythonize("ctree.pyx")


)
