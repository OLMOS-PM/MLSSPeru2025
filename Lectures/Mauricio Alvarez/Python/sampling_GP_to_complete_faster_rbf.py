import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

# Fix the seed
seedn = 10**4
np.random.seed(seedn)

Nx = 100
x = np.linspace(0, 1, num=Nx)[:, np.newaxis]
Nxp = 100              
xp = np.linspace(0, 1, num=Nxp)[:, np.newaxis]


# Faster version for computing the RBF kernel
def rbfKernel(x, xp, l, sf):
    # Write your code here
    
    return K


# Compute the covariance matrix
l = 0.1*np.sqrt(3)
sf = 1
K = rbfKernel(x, xp, l, sf)

# Plot the covariance function
fig, ax = plt.subplots()
plt.imshow(K, extent=[0, 1, 1, 0])
plt.colorbar()
ax.set_title('Covariance matrix')

# We now sample from the GP with mean zero and matrix K
nsamples = 5
mean_GP = np.zeros(Nx)
samples = multivariate_normal.rvs(mean_GP, K, nsamples)

fig, ax = plt.subplots()  
plt.plot(x, samples.T, linewidth=2)



    

