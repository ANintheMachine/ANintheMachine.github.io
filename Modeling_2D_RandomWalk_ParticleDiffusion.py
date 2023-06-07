# random_walk.py
#%%
import numpy as np
from numpy.random import random as rng
import matplotlib.pyplot as plt

num_steps = 500
num_walkers = 1000


plt.figure()
plt.title("Figure 1-1: Random Walk (Diamond Lattice)")
r2ave=np.zeros(num_steps)
for j in range(num_walkers):
    x_step=rng(num_steps)
    y_step=rng(num_steps)
    x_step=2*(x_step > 0.5)-1
    y_step=2*(y_step > 0.5)-1
    x=np.cumsum(x_step)
    y=np.cumsum(y_step)
    temp=x**2+y**2
    r2ave=r2ave+temp
    plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.figure()

plt.plot(r2ave/num_walkers)
plt.figure()
plt.title("Figure 1-3: Avg. Displacement from Origin (Diamond Lattice)")
plt.xlabel("step number")
plt.ylabel("Displacement")

plt.figure(3)
for i in range(num_walkers):
    theta_step=np.random.randint(0,6,500)*60
    theta_step=np.radians(theta_step)
    
    x_step=rng(num_steps)
    x_step=2*(x_step>0.5)-1
    x_step=x_step*np.cos(theta_step)

    y_step=rng(num_steps)
    y_step=2*(y_step>0.5)-1
    y_step=y_step*np.sin(theta_step)
    
    x=np.cumsum(x_step)
    y=np.cumsum(y_step)
    temp=x**2+y**2
    r2ave=r2ave+temp
    plt.plot(x,y)
plt.figure(4)
plt.plot(r2ave/num_walkers)

plt.title("Figure 1-6: Displacement from Origin (Triangular Lattice)")
plt.xlabel("step number")
plt.ylabel("Displacement")