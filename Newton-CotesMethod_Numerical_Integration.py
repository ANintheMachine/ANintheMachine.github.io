# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:56:43 2017

@author: Arun-SP
"""

import numpy as np
import matplotlib.pyplot as plt

# DEFINING PARAMETERS
l=9.8
g=9.8
d_theta=0.001
theta_m=(np.pi)/6
d_T=0
T2=0
# CALCULATING NUMBER OF GRID POINTS
nGP=int(theta_m/d_theta)

# "FOR" LOOP TO CALCULATE THE PERIOD OF THETA_M= PI/6
for i in range(nGP):
    bvalue=(np.cos(i*d_theta)-np.cos(theta_m))
    d_T=d_theta/np.sqrt(bvalue)
    T2=T2+d_T    
T=np.sqrt(8*T2)

#%%

# DEFINING PARAMETERS AND ARRAYS
l=9.8
g=9.8
d_theta=0.001
theta_m=np.linspace((np.pi)/30,(np.pi),10)
T2=np.zeros(theta_m.size)
T=np.zeros(theta_m.size)

# "FOR" LOOP TO CALCULATE THE PERIOD FOR MANY ANGLES
for i in range(theta_m.size):
    nGP0=theta_m[i]/d_theta
    nGP=int(nGP0)
    d_T=0
    for j in range(nGP):
        bvalue=(np.cos(j*d_theta)-np.cos(theta_m[i]))
        d_T=d_theta/np.sqrt(bvalue)
        T2[i]=T2[i]+d_T
    T[i]=np.sqrt(8*T2[i])
    
# PLOTTING FIGURE 1-1
plt.figure()
plt.plot(theta_m,T)
plt.title('Figure 1-1: Period vs Initial Angle')
plt.xlabel('theta_m (radians)')
plt.ylabel('Period (sec)')
