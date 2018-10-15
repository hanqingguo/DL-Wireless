import scipy
import numpy as np
import os

filename = "qpsk_demod.txt"
dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, filename)

print(file_path)
f = scipy.fromfile(open(file_path),dtype=scipy.int8)

dest_path = os.path.join(dir_path, filename[:-4]+"_out"+".txt")
np.savetxt(dest_path, f, fmt='%.8f')
