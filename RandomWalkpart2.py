# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 11:02:07 2017

@author: Arun-SP
"""
#%%%
import numpy as np
from numpy.random import random as rng
import matplotlib.pyplot as plt

#%% DEFINING PARAMETERS AND INITAL CONDITIONS
num_steps = 500
num_walkers = 1000

#%% PLOTTING FIGURE 1-1

# NON-CONFINED TRIAL

x_coor = np.zeros([num_walkers,num_steps])
y_coor = np.zeros([num_walkers,num_steps])

for j in range(num_walkers):
    x_step = rng(num_steps)
    x_step = 2 * (x_step >= 0.5) - 1
    x = np.cumsum(x_step) 
    x_coor[j,:] = x

    y_step = rng(num_steps)
    y_step = 2 * (y_step >= 0.5) - 1
    y = np.cumsum(y_step)
    y_coor[j,:] = y

plt.figure()
plt.title("Figure 1-1: Non-Confined Random walk in two dimension")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x_coor[:,num_steps-1],y_coor[:,num_steps-1],'o')

#%%PLOTTING FIGURE 1-2

# CALCULATING ENTROPY 
nbin= 64
xedges=np.linspace(-1*num_steps,num_steps,nbin+1)
yedges=np.linspace(-1*num_steps,num_steps,nbin+1)

Entropy=np.zeros(num_steps)

for s in range(num_steps):
    h=np.histogram2d(x_coor[:,s],y_coor[:,s],bins=(xedges,yedges))
    p=h[0]/sum(sum(h[0]))
    v=0
    for i in range (nbin):
        for j in range(nbin):
            if (p[i,j]>0):
                v+=-p[i,j]*np.log(p[i,j])
    Entropy[s]=v
    
plt.figure()
plt.title("Figure 1-2: Non-Confined Random walk in two dimension")
plt.xlabel("num_step")
plt.ylabel("Entropy")
plt.plot(Entropy)


#%% PLOTTING FIGURE 1-3

# CONFINIED TRIAL 

#Subplot num_step=500
num_steps=500
x_coor = np.zeros([num_walkers,num_steps])
y_coor = np.zeros([num_walkers,num_steps])

for j in range(num_walkers):
    x_step = rng(num_steps)
    x_step = 2 * (x_step >= 0.5) - 1    
    y_step = rng(num_steps)
    y_step = 2 * (y_step >= 0.5) - 1
    x = np.cumsum(x_step)
    y = np.cumsum(y_step)
    
    for i in range(num_steps):
        if x[i]>100:
            x[i]=100
        else:
            x[i]=x[i]        
        if x[i]<-100:
            x[i]=-100
        else:
            x[i]=x[i]
        
        if y[i]>100:
            y[i]=100
        else:
            y[i]=y[i]
        if y[i]<-100:
            y[i]=-100
        else:
            y[i]=y[i]
            
    x_coor[j,:] = x
    y_coor[j,:] = y


plt.figure(3)
plt.subplot(221)
plt.plot(x_coor[:,num_steps-1],y_coor[:,num_steps-1],'o')
plt.title('Figure 1-3: Confined Diffusion, num_step=500',fontsize=8)
plt.ylabel('x',fontsize=8)
plt.xlabel('y',fontsize=8)
plt.tight_layout()

#Subplot num_step= 1000
num_steps=1000
x_coor = np.zeros([num_walkers,num_steps])
y_coor = np.zeros([num_walkers,num_steps])

for j in range(num_walkers):
    x_step = rng(num_steps)
    x_step = 2 * (x_step >= 0.5) - 1    
    y_step = rng(num_steps)
    y_step = 2 * (y_step >= 0.5) - 1
    x = np.cumsum(x_step)
    y = np.cumsum(y_step)
    
    for i in range(num_steps):
        if x[i]>100:
            x[i]=100
        else:
            x[i]=x[i]        
        if x[i]<-100:
            x[i]=-100
        else:
            x[i]=x[i]
        
        if y[i]>100:
            y[i]=100
        else:
            y[i]=y[i]
        if y[i]<-100:
            y[i]=-100
        else:
            y[i]=y[i]
            
    x_coor[j,:] = x
    y_coor[j,:] = y


plt.figure(3)
plt.subplot(222)
plt.plot(x_coor[:,num_steps-1],y_coor[:,num_steps-1],'o')
plt.title('Figure 1-3: Confined Diffusion, num_step=1000',fontsize=8)
plt.ylabel('x',fontsize=8)
plt.xlabel('y',fontsize=8)
plt.tight_layout()
#Subplot num_step=1500
num_steps=1500
x_coor = np.zeros([num_walkers,num_steps])
y_coor = np.zeros([num_walkers,num_steps])

for j in range(num_walkers):
    x_step = rng(num_steps)
    x_step = 2 * (x_step >= 0.5) - 1    
    y_step = rng(num_steps)
    y_step = 2 * (y_step >= 0.5) - 1
    x = np.cumsum(x_step)
    y = np.cumsum(y_step)
    
    for i in range(num_steps):
        if x[i]>100:
            x[i]=100
        else:
            x[i]=x[i]        
        if x[i]<-100:
            x[i]=-100
        else:
            x[i]=x[i]
        
        if y[i]>100:
            y[i]=100
        else:
            y[i]=y[i]
        if y[i]<-100:
            y[i]=-100
        else:
            y[i]=y[i]
            
    x_coor[j,:] = x
    y_coor[j,:] = y


plt.figure(3)
plt.subplot(223)
plt.plot(x_coor[:,num_steps-1],y_coor[:,num_steps-1],'o')
plt.title('Figure 1-3: Confined Diffusion, num_step=1500',fontsize=8)
plt.ylabel('x',fontsize=8)
plt.xlabel('y',fontsize=8)
plt.tight_layout()

#Subplot num_step=3000
num_steps=3000
x_coor = np.zeros([num_walkers,num_steps])
y_coor = np.zeros([num_walkers,num_steps])

for j in range(num_walkers):
    x_step = rng(num_steps)
    x_step = 2 * (x_step >= 0.5) - 1    
    y_step = rng(num_steps)
    y_step = 2 * (y_step >= 0.5) - 1
    x = np.cumsum(x_step)
    y = np.cumsum(y_step)
    
    for i in range(num_steps):
        if x[i]>100:
            x[i]=100
        else:
            x[i]=x[i]        
        if x[i]<-100:
            x[i]=-100
        else:
            x[i]=x[i]
        
        if y[i]>100:
            y[i]=100
        else:
            y[i]=y[i]
        if y[i]<-100:
            y[i]=-100
        else:
            y[i]=y[i]
            
    x_coor[j,:] = x
    y_coor[j,:] = y


plt.figure(3)
plt.subplot(224)
plt.plot(x_coor[:,num_steps-1],y_coor[:,num_steps-1],'o')
plt.title('Figure 1-3: Confined Diffusion, num_step=3000',fontsize=8)
plt.ylabel('x',fontsize=8)
plt.xlabel('y',fontsize=8)
plt.tight_layout()

#%% PLOTTING FIGURE 1-4


#Comparison of Non-Confined vs Confined at num_step=2000

#Confined 2D and Entopy plots
num_steps=2000
x_coor = np.zeros([num_walkers,num_steps])
y_coor = np.zeros([num_walkers,num_steps])

for j in range(num_walkers):
    x_step = rng(num_steps)
    x_step = 2 * (x_step >= 0.5) - 1    
    y_step = rng(num_steps)
    y_step = 2 * (y_step >= 0.5) - 1
    x = np.cumsum(x_step)
    y = np.cumsum(y_step)
    
    for i in range(num_steps):
        if x[i]>100:
            x[i]=100
        else:
            x[i]=x[i]        
        if x[i]<-100:
            x[i]=-100
        else:
            x[i]=x[i]
        
        if y[i]>100:
            y[i]=100
        else:
            y[i]=y[i]
        if y[i]<-100:
            y[i]=-100
        else:
            y[i]=y[i]
            
    x_coor[j,:] = x
    y_coor[j,:] = y
plt.figure(4)
plt.subplot(221)
plt.plot(x_coor[:,num_steps-1],y_coor[:,num_steps-1],'o')
plt.title('Figure 1-4: Confined Diffusion 2D, num_step=2000',fontsize=8)
plt.ylabel('x',fontsize=8)
plt.xlabel('y',fontsize=8)
plt.tight_layout()


# CALCULATING ENTROPY 
nbin= 64
xedges=np.linspace(-1*num_steps,num_steps,nbin+1)
yedges=np.linspace(-1*num_steps,num_steps,nbin+1)

Entropy=np.zeros(num_steps)

for s in range(num_steps):
    h=np.histogram2d(x_coor[:,s],y_coor[:,s],bins=(xedges,yedges))
    p=h[0]/sum(sum(h[0]))
    v=0
    for i in range (nbin):
        for j in range(nbin):
            if (p[i,j]>0):
                v+=-p[i,j]*np.log(p[i,j])
    Entropy[s]=v

plt.figure(4)
plt.subplot(223)
plt.plot(Entropy)
plt.title("Figure 1-4: Change in Entropy for Confined Diffusion",fontsize=8)
plt.xlabel("num_step",fontsize=8)
plt.ylabel("Entropy",fontsize=8)
plt.tight_layout()

# Non-Confined 2D and Entropy plots at num_step=2000

num_steps=2000
x_coor = np.zeros([num_walkers,num_steps])
y_coor = np.zeros([num_walkers,num_steps])

for j in range(num_walkers):
    x_step = rng(num_steps)
    x_step = 2 * (x_step >= 0.5) - 1
    x = np.cumsum(x_step) 
    x_coor[j,:] = x

    y_step = rng(num_steps)
    y_step = 2 * (y_step >= 0.5) - 1
    y = np.cumsum(y_step)
    y_coor[j,:] = y
plt.figure(4)
plt.subplot(222)
plt.plot(x_coor[:,num_steps-1],y_coor[:,num_steps-1],'o')
plt.title('Figure 1-4: Non-Confined Diffusion 2D, num_step=2000',fontsize=8)
plt.ylabel('x',fontsize=8)
plt.xlabel('y',fontsize=8)
plt.tight_layout()


# CALCULATING ENTROPY 
nbin= 64
xedges=np.linspace(-1*num_steps,num_steps,nbin+1)
yedges=np.linspace(-1*num_steps,num_steps,nbin+1)

Entropy=np.zeros(num_steps)

for s in range(num_steps):
    h=np.histogram2d(x_coor[:,s],y_coor[:,s],bins=(xedges,yedges))
    p=h[0]/sum(sum(h[0]))
    v=0
    for i in range (nbin):
        for j in range(nbin):
            if (p[i,j]>0):
                v+=-p[i,j]*np.log(p[i,j])
    Entropy[s]=v
    
plt.figure(4)
plt.subplot(224)
plt.plot(Entropy)
plt.title("Figure 1-4: Change in Entropy for Non-Confined Diffusion",fontsize=8)
plt.xlabel("num_step",fontsize=8)
plt.ylabel("Entropy",fontsize=8)
plt.tight_layout()

#%% PLOTTING FIGURE 1-5