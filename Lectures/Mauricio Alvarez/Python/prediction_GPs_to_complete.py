import numpy as np
import matplotlib.pyplot as plt

# Fix the seed
seedn = 10**4
np.random.seed(seedn)

N_tot = 100
sigma2 = 0.01
beta = 1/sigma2
betaInv = 1/beta
x_tot = np.linspace(0, 1, num=N_tot)[:, np.newaxis] 
y_tot = np.sin(2*np.pi*x_tot)
noise = np.sqrt(betaInv)*np.random.randn(N_tot)[:, np.newaxis]
t_tot = y_tot + noise 

# Choose 60% for traininig 
N = 10
index = np.random.permutation(N_tot)
t = t_tot[index[0:N]]
x = x_tot[index[0:N]]

fig, ax = plt.subplots()

ax.plot(x_tot, y_tot, 'b', x, t, '.r', linewidth=2.0)
plt.show()

def rbfKernel(x, xp, l, sf):
    aux = x**2 - 2*x@xp.T + (xp.T**2)
    K = sf*np.exp(-aux/(2*l**2))
    return K

# Compute the covariance matrix
l = 0.1
sf = 0.5
xp = x
K = rbfKernel(x, xp, l, sf)

# We compute the inverse of K using the Cholesky decomposition
# K = L*L.T then K^{-1} = L^{-T}*L^{-1}
L = np.linalg.cholesky(K + betaInv*np.eye(N))
Linv = np.linalg.solve(L, np.eye(N))
Kinv = Linv.T@Linv

# Compute the covariance between all x_tot and x
Ktest = 
# Compute the covariance between all x_tot and x_tot
Ktest_test = 
# Compute the predictive mean
mpred = 
# Compute the predictive variance
vpred = 

# We plot the predictive distribution
fig, ax = plt.subplots()
ax.plot(x_tot, y_tot, 'b', x_tot, mpred, 'k', linewidth=2.0)
ax.plot(x_tot, mpred+1.96*np.sqrt(vpred[:, np.newaxis]), 'k--', linewidth=2.0)
ax.plot(x_tot, mpred-1.96*np.sqrt(vpred[:, np.newaxis]), 'k--', linewidth=2.0)
ax.plot(x, t, 'or')
plt.show()







