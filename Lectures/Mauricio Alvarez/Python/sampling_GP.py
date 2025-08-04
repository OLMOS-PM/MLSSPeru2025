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


# Slow version for computing the kernel
def rbfKernel_loop(x, xp, l, sf):
    Nx = np.shape(x)[0]
    Nxp = np.shape(xp)[0]
    K = np.zeros((Nx, Nxp))
    for i in range(Nx):
        for j in range(Nxp):
            K[i,j] = sf*np.exp(-(x[i]-xp[j])**2/(2*l**2))
    
    return K

# Faster version for computing the kernel
def rbfKernel(x, xp, l, sf):
    aux = x**2 - 2*x@xp.T + (xp.T**2)
    K = sf*np.exp(-aux/(2*l**2))
    return K

# Faster version for computing the kernel
def matern32Kernel(x, xp, l, sf):
    aux = np.abs(x-xp.T) 
    K = sf*(1 + np.sqrt(3)*aux/l)*np.exp(-np.sqrt(3)*aux/l)
    return K

# Compute the covariance matrix
l = 0.1*np.sqrt(3)
sf = 1

#K = rbfKernel_loop(x, xp, l, sf) # RBF with loops
#K = matern32Kernel(x, xp, l, sf) # Matern 3/2
K = rbfKernel_loop(x, xp, l, sf) # RBF without loops

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



    

