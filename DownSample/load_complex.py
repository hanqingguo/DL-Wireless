import scipy
import numpy as np
import os

filename = "original"
dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, filename)

print(file_path)
f = scipy.fromfile(open(file_path),dtype=scipy.complex64)

dest_path = os.path.join(dir_path, filename+"_out"+".txt")
np.savetxt(dest_path, f, fmt='%.8f')
