#
# Some global settings
import os
import ctypes
import numpy
from mpi4py import MPI

pth = os.path.dirname(os.path.abspath(__file__))
pth = os.path.split(pth)[0]
pth = os.path.join(pth,'standalone/libs/libqsym.so')
libqsym = ctypes.CDLL(pth)

dmrg_type = 'real'
if dmrg_type == 'real':
   # Real case
   dmrg_dtype =numpy.float_
   dmrg_mtype =MPI.DOUBLE
   #pth = os.path.join(pth,'libs/libextract_real.so')
   #ll = ctypes.CDLL(pth)
elif dmrg_type == 'complex': 
   # Complex case
   dmrg_dtype = numpy.complex_
   dmrg_mtype = MPI.DOUBLE_COMPLEX
   #pth = os.path.join(pth,'libs/libextract_complex.so')
   #ll = ctypes.CDLL(pth)
