import numpy as np
import pandas as pd
import matplotlib as plt

# 10/17/26 Learning libraries
# Using Python REPL to run lines (shift-Enter), main.py will use print statements to show results when running main.py in the terminal.
# Referencing O'Reilly's "Python Data Science Handbook" by Jake VanderPlas

# NumPy
rng = np.random.default_rng(seed=5757) # rng seed
# Arrays
np.zeros(10, dtype=int) # Array of zeroes
np.ones((3,5),dtype=float)
np.full((2,4), 5.7) # Filled Array
np.arange(0,20,3) # Linear sequence, step
np.linspace(0,1,5) # Array of 5 evenly spaced values
np.random.random((3,3)) # 3x3 Array of uniformly distributed randoms
np.random.normal(0,1,(3,3)) # 3x3 of normally distributed randoms, mean 0 stddev 1
np.random.randint(0,10,(3,3)) # 3x3 of randoms in [0,10)
np.eye(3) # Identity matrix
np.empty(3) # Uninitialized array
twodim = rng.integers(10, size=(3,4)) # 2d array
twodim
twodim.ndim # number of dimensions
twodim.shape # size of each dimension
twodim.size # size of array
twodim.dtype # type of each element
# Subarrays
twodim[:2] # show first two lines
twodim[2:] # show lines after first two
twodim[1] # show 1st index (second row)
# Multi-Dimensional Subarrays
twodim[:2, :3] # first two rows, first three cols
twodim[:3, ::2] # first three rows, every other col
subtwodim = twodim[:2, ::2] # saving a subarray copy
# Reshaping Arrays
np.arange(1,10).reshape((3,3)) # Reshaped array
toreshape = np.arange(1,4)
toreshape.reshape((1,3))
toreshape[np.newaxis, :]
toreshape.reshape((3,1))
toreshape[:, np.newaxis]
# Concatenation
x = np.arange(1,3)
y = np.arange(5,9)
np.concatenate([x,y])
np.concatenate([twodim, twodim])
np.concatenate([twodim, twodim], axis=1)
# Splitting
upper, lower = np.vsplit(twodim, [2])
upper
lower
left,right=np.hsplit(twodim,[2])
left
right
## dsplit would split along a third axis.

# Pandas
spectrum = pd.read_csv("spectrum.csv")
"CSV Output:"
spectrum
spectrum.shape

#Matplotlib