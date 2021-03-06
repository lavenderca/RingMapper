
#########################################################
# Code to compile readMutStrings.pyx
# Anthony Mustoe
# 2018
#
# This file is licensed under the terms of the MIT license  
#
#########################################################


from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
    name = "readMutStrings",
    ext_modules = cythonize("readMutStrings.pyx"),
    include_dirs = [numpy.get_include()]
)
