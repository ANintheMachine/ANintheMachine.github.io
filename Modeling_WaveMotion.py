
"""
Created on Wed Nov  8 12:40:14 2017

@author: Arun-SP
"""
import matplotlib.pyplot as plt
import numpy as np


#%%###### 2 FIXED ENDS ######
c = 300    # wave speed in m/s
dx = 0.01  # grid spacing on the string in meters
dt = dx/c  # time in seconds
l = 1      # string length in meters
t = 1000    # max time in seconds
r = c*dt/dx
 
n = int(l/dx) # number of grid points on the string - 1

# Initialize Arrays
Y = np.zeros([n+1,3])

#Boundary Condition
Y[0,0]= 0
Y[n,0]= 0

Y[0,1]= 0
Y[n,1]= 0

Y[0,2]= 0
Y[n,2]= 0

# Initial Condition (excluding the end points)
for i in range(n):
    Y[i,0]=np.exp(-1000*(i*dx - 0.3)**2)
    Y[i,1]=np.exp(-1000*(i*dx - 0.3)**2)
    
Y[0,0]= 0
Y[n,0]= 0

Y[0,1]= 0
Y[n,1]= 0
    

# Update V1 

# PLOTTING FIGURE 1-1
for j in range(2000):
    for i in range(n-1):
        temp_element2 = 2*(1-r**2)*Y[i+1,1]-Y[i+1,0]+r**2*(Y[i+2,1]+Y[i,1])
        Y[i+1,2] = temp_element2
        
        Temp1 = Y[1, 2]
        Y[0, 2] = Temp1
        
        Temp2 = Y[n-1, 2]
        Y[n, 2] = Y[n, 2]
        
    
    for i in range(n-2):
        Y0 = Y[i+1,1]
        Y1 = Y[i+1,2]
        Y[i+1,0]= Y0
        Y[i+1,1]= Y1
    if (j%100 ==0):
        plt.figure(1)
        plt.plot(Y[:,2])
        plt.xlabel('Gridpoints')
        plt.ylabel('Vertical Displacement (meters)')
        plt.title('Figure 1-1: Wave with Two Fixed Ends')    
        
# PLOTTING FIGURE 1-2
# SUBPLOTS FOR 2 FIXED POINTS
for j in range(200):
    for i in range(n-1):
        temp_element2 = 2*(1-r**2)*Y[i+1,1]-Y[i+1,0]+r**2*(Y[i+2,1]+Y[i,1])
        Y[i+1,2] = temp_element2
        Temp1 = Y[1, 2]
        Y[0, 2] = Temp1
        
        Temp2 = Y[n-1, 2]
        Y[n, 2] = Y[n, 2]
        
    
    for i in range(n-2):
        Y0 = Y[i+1,1]
        Y1 = Y[i+1,2]
        Y[i+1,0]= Y0
        Y[i+1,1]= Y1
    if (j%200 ==0):
        plt.figure(2)
        plt.subplot(221)
        plt.title('Figure 1-2:timestep 200',fontsize=8)
        plt.plot(Y[:,1])
        plt.ylabel('Vertical Disp. (meters)',fontsize=8)
        plt.xlabel('Gridpoints',fontsize=8)
        

for j in range(500):
    for i in range(n-1):
        temp_element2 = 2*(1-r**2)*Y[i+1,1]-Y[i+1,0]+r**2*(Y[i+2,1]+Y[i,1])
        Y[i+1,2] = temp_element2
        Temp1 = Y[1, 2]
        Y[0, 2] = Temp1
        
        Temp2 = Y[n-1, 2]
        Y[n, 2] = Y[n, 2]
        
    
    for i in range(n-2):
        Y0 = Y[i+1,1]
        Y1 = Y[i+1,2]
        Y[i+1,0]= Y0
        Y[i+1,1]= Y1
    if (j%500 ==0):
        plt.figure(2)
        plt.subplot(222)
        plt.title('Figure1-2:timestep 500',fontsize=8)
        plt.plot(Y[:,1])
        plt.ylabel('Vertical Disp. (meters)',fontsize=8)
        plt.xlabel('Gridpoints',fontsize=8)
        
for j in range(1000):
    for i in range(n-1):
        temp_element2 = 2*(1-r**2)*Y[i+1,1]-Y[i+1,0]+r**2*(Y[i+2,1]+Y[i,1])
        Y[i+1,2] = temp_element2
        Temp1 = Y[1, 2]
        Y[0, 2] = Temp1
        
        Temp2 = Y[n-1, 2]
        Y[n, 2] = Y[n, 2]
        
    
    for i in range(n-2):
        Y0 = Y[i+1,1]
        Y1 = Y[i+1,2]
        Y[i+1,0]= Y0
        Y[i+1,1]= Y1
    if (j%1000 ==0):
        plt.figure(2)
        plt.subplot(223)
        plt.title('Figure1-2:timestep 1000',fontsize=8)
        plt.plot(Y[:,1])
        plt.xlabel('Gridpoints',fontsize=8)
        plt.ylabel('Vertical Disp. (meters)',fontsize=8)     
    
    
for j in range(2000):
    for i in range(n-1):
        temp_element2 = 2*(1-r**2)*Y[i+1,1]-Y[i+1,0]+r**2*(Y[i+2,1]+Y[i,1])
        Y[i+1,2] = temp_element2
        Temp1 = Y[1, 2]
        Y[0, 2] = Temp1
        
        Temp2 = Y[n-1, 2]
        Y[n, 2] = Y[n, 2]
        
    
    for i in range(n-2):
        Y0 = Y[i+1,1]
        Y1 = Y[i+1,2]
        Y[i+1,0]= Y0
        Y[i+1,1]= Y1
    if (j%2000 ==0):
        plt.figure(2)
        plt.subplot(224)
        plt.title('Figure1-2:timestep 2000',fontsize=8)
        plt.plot(Y[:,1])
        plt.xlabel('Gridpoints',fontsize=8)
        plt.ylabel('Vertical Disp. (meters)',fontsize=8)
        plt.tight_layout()
        
#%%###### 2 FREE ENDS ######

c = 300    # wave speed in m/s
dx = 0.01  # grid spacing on the string in meters
dt = dx/c  # time in seconds
l = 1      # string length in meters
t = 1000    # max time in seconds
r = c*dt/dx
 
n = int(l/dx) # number of grid points on the string - 1

# Initialize Arrays
Y = np.zeros([n+1,3])

# Boundary Condition
Y[0,0]= 0
Y[n,0]= 0

Y[0,1]= 0
Y[n,1]= 0

Y[0,2]= 0
Y[n,2]= 0

# Initial Condition (excluding the end points)
for i in range(n):
    Y[i,0]=np.exp(-1000*(i*dx - 0.3)**2)
    Y[i,1]=np.exp(-1000*(i*dx - 0.3)**2)
    
Y[0,0]= 0
Y[n,0]= 0

Y[0,1]= 0
Y[n,1]= 0
    


for j in range(1200):
    for i in range(n-1):
        temp_element2 = 2*(1-r**2)*Y[i+1,1]-Y[i+1,0]+r**2*(Y[i+2,1] +Y[i,1])
        Y[i+1,2] = temp_element2
         
    Y[0,2] = 2*(1- 0.5*r**2)*Y[0,1] - Y[0,0] + r**2*Y[1,1]
    temp1 = Y[1,2]
    Y[0,2] = temp1
    Y[n,2] = 2*(1- 0.5*r**2)*Y[n,1] - Y[n,0] + r**2*Y[n-1,1]
    temp2 = Y[n-1,2]
    Y[n,2] = temp2
    
    for i in range(n+1):
        Y0 =  Y[i,1]
        Y1 =  Y[i,2]
        Y[i,0] = Y0
        Y[i,1] = Y1
    
    if (j%1200 ==0):
        plt.figure(3)
        plt.subplot(221)
        plt.plot(Y[:,1])
        plt.title('Figure 1-3:Timestep 1200',fontsize=8)
        plt.ylabel('Vertical Disp. (meters)',fontsize=8)
        plt.xlabel('Gridpoints',fontsize=8)
        
for j in range(1600):
    for i in range(n-1):
        temp_element2 = 2*(1-r**2)*Y[i+1,1]-Y[i+1,0]+r**2*(Y[i+2,1] +Y[i,1])
        Y[i+1,2] = temp_element2
         
    Y[0,2] = 2*(1- 0.5*r**2)*Y[0,1] - Y[0,0] + r**2*Y[1,1]
    temp1 = Y[1,2]
    Y[0,2] = temp1
    Y[n,2] = 2*(1- 0.5*r**2)*Y[n,1] - Y[n,0] + r**2*Y[n-1,1]
    temp2 = Y[n-1,2]
    Y[n,2] = temp2
    
    for i in range(n+1):
        Y0 =  Y[i,1]
        Y1 =  Y[i,2]
        Y[i,0] = Y0
        Y[i,1] = Y1
    
    if (j%1600 ==0):
        plt.figure(3)
        plt.subplot(222)
        plt.plot(Y[:,1])
        plt.title('Figure 1-3:Timestep 1600',fontsize=8)
        plt.xlabel('Gridpoints',fontsize=8)
        plt.ylabel('Vertical Disp. (meters)',fontsize=8)        
for j in range(1800):
    for i in range(n-1):
        temp_element2 = 2*(1-r**2)*Y[i+1,1]-Y[i+1,0]+r**2*(Y[i+2,1] +Y[i,1])
        Y[i+1,2] = temp_element2
         
    Y[0,2] = 2*(1- 0.5*r**2)*Y[0,1] - Y[0,0] + r**2*Y[1,1]
    temp1 = Y[1,2]
    Y[0,2] = temp1
    Y[n,2] = 2*(1- 0.5*r**2)*Y[n,1] - Y[n,0] + r**2*Y[n-1,1]
    temp2 = Y[n-1,2]
    Y[n,2] = temp2
    
    for i in range(n+1):
        Y0 =  Y[i,1]
        Y1 =  Y[i,2]
        Y[i,0] = Y0
        Y[i,1] = Y1
    
    if (j%1800 ==0):
        plt.figure(3)
        plt.subplot(223)
        plt.plot(Y[:,1])
        plt.title('Figure 1-3:Timestep 1800',fontsize=8)
        plt.xlabel('Gridpoints',fontsize=8)
        plt.ylabel('Vertical Disp. (meters)',fontsize=8)        
for j in range(2200):
    for i in range(n-1):
        temp_element2 = 2*(1-r**2)*Y[i+1,1]-Y[i+1,0]+r**2*(Y[i+2,1] +Y[i,1])
        Y[i+1,2] = temp_element2
         
    Y[0,2] = 2*(1- 0.5*r**2)*Y[0,1] - Y[0,0] + r**2*Y[1,1]
    temp1 = Y[1,2]
    Y[0,2] = temp1
    Y[n,2] = 2*(1- 0.5*r**2)*Y[n,1] - Y[n,0] + r**2*Y[n-1,1]
    temp2 = Y[n-1,2]
    Y[n,2] = temp2
    
    for i in range(n+1):
        Y0 =  Y[i,1]
        Y1 =  Y[i,2]
        Y[i,0] = Y0
        Y[i,1] = Y1
    
    if (j%2200 ==0):
        plt.figure(3)
        plt.subplot(224)
        plt.plot(Y[:,1])    
        plt.title('Figure 1-3:Timestep 1800',fontsize=8)
        plt.xlabel('Gridpoints',fontsize=8)
        plt.ylabel('Vertical Disp. (meters)',fontsize=8)        
        plt.tight_layout()
#%%###### 1 FREE 1 FIXED END ######
c = 300   # wave speed in m/s
dx = 0.01  # grid spacing on the string in meters
dt = dx/c  # time in seconds
l = 1      # string length in meters
t = 1000    # max time in seconds
r = c*dt/dx
omega = 1884.96
A = 1

n = int(l/dx) # number of grid points on the string - 1

# Initialize Arrays
Y = np.zeros([n+1,3])

# Boundary Condition
Y[0,0]= 0
Y[n,0]= 0

Y[0,1]= 0
Y[n,1]= A* np.sin(omega*dt)


# PLOTTING FIGURE 1-4

for j in range(1000):
    for i in range(n-1):
        temp_element2 = 2*(1-r**2)*Y[i+1,1]-Y[i+1,0]+r**2*(Y[i+2,1]+Y[i,1])
        Y[i+1,2] = temp_element2
    Y[0, 2] = 0
    Y[n, 2] = A * np.sin(omega*(j+2)*dt)
        
    
    for i in range(n+1):
        Y0 = Y[i,1]
        Y1 = Y[i,2]
        Y[i,0]= Y0
        Y[i,1]= Y1
    if (j%100 ==0):
        plt.figure(4)
        plt.plot(Y[:,2])
        plt.xlabel('Gridpoints')
        plt.ylabel('Vertical Displacementn (meters)')
        plt.title('Figure 1-4: Wave with One Free and One Fixed End')
   
    
#%%###### 1 FREE 1 FIXED END ######
c = 300   # wave speed in m/s
dx = 0.01  # grid spacing on the string in meters
dt = dx/c  # time in seconds
l = 1      # string length in meters
t = 1000    # max time in seconds
r = c*dt/dx
omega =1884.95559215
A = 1
 
n = int(l/dx) # number of grid points on the string - 1

# Initialize Arrays
Y = np.zeros([n+1,3])

# Boundary Condition
Y[0,0]= 0
Y[n,0]= 0

Y[0,1]= 0
Y[n,1]= A* np.sin(omega*dt)


# PLOTTING FIGURE 1-5

plt.figure(5)
plt.title('Figure 1-5: Wave Amplitudes for Different "t" values; at Omega=1884.95559215 rad/s')
plt.show(5)
# t=1000*dt
for j in range(1000):
    for i in range(n-1):
        temp_element2 = 2*(1-r**2)*Y[i+1,1]-Y[i+1,0]+r**2*(Y[i+2,1]+Y[i,1])
        Y[i+1,2] = temp_element2
    Y[0, 2] = 0
    Y[n, 2] = A * np.sin(omega*(j+2)*dt)
        
    
    for i in range(n+1):
        Y0 = Y[i,1]
        Y1 = Y[i,2]
        Y[i,0]= Y0
        Y[i,1]= Y1
    if (j%100 ==0):
        plt.figure(5)
        plt.subplot(221)
        plt.plot(Y[:,1])
        plt.title('t=1000*dt',fontsize=8)
        plt.ylabel('Vertical Disp. (meters)',fontsize=8)    
# t=2000*dt

n = int(l/dx) # number of grid points on the string - 1
Y = np.zeros([n+1,3])
# Boundary Condition
Y[0,0]= 0
Y[n,0]= 0
Y[0,1]= 0
Y[n,1]= A* np.sin(omega*dt)
for j in range(2000):
    for i in range(n-1):
        temp_element2 = 2*(1-r**2)*Y[i+1,1]-Y[i+1,0]+r**2*(Y[i+2,1]+Y[i,1])
        Y[i+1,2] = temp_element2
    Y[0, 2] = 0
    Y[n, 2] = A * np.sin(omega*(j+2)*dt)
        
    
    for i in range(n+1):
        Y0 = Y[i,1]
        Y1 = Y[i,2]
        Y[i,0]= Y0
        Y[i,1]= Y1
    if (j%200 ==0):
        plt.figure(5)
        plt.subplot(222)
        plt.plot(Y[:,1])
        plt.title('t=2000*dt',fontsize=8)
        plt.ylabel('Vertical Disp. (meters)',fontsize=8)
        plt.xlabel('Gridpoints',fontsize=8)         
# t=3000*dt

n = int(l/dx) # number of grid points on the string - 1
Y = np.zeros([n+1,3])
# Boundary Condition
Y[0,0]= 0
Y[n,0]= 0
Y[0,1]= 0
Y[n,1]= A* np.sin(omega*dt)
for j in range(3000):
    for i in range(n-1):
        temp_element2 = 2*(1-r**2)*Y[i+1,1]-Y[i+1,0]+r**2*(Y[i+2,1]+Y[i,1])
        Y[i+1,2] = temp_element2
    Y[0, 2] = 0
    Y[n, 2] = A * np.sin(omega*(j+2)*dt)
        
    
    for i in range(n+1):
        Y0 = Y[i,1]
        Y1 = Y[i,2]
        Y[i,0]= Y0
        Y[i,1]= Y1
    if (j%300 ==0):
        plt.figure(5)
        plt.subplot(223)
        plt.plot(Y[:,1])
        plt.title('t=3000*dt',fontsize=8)
        plt.ylabel('Vertical Disp. (meters)',fontsize=8)    
        plt.xlabel('Gridpoints',fontsize=8) 
        plt.tight_layout()

#%% PLOTTING FIGURE 1-       

# SUBPLOTS FOR STANDING WAVES 
c = 300   # wave speed in m/s
dx = 0.01  # grid spacing on the string in meters
dt = dx/c  # time in seconds
l = 1      # string length in meters
t = 1000    # max time in seconds
r = c*dt/dx


omega =942.477796075
A = 1
 
n = int(l/dx) # number of grid points on the string - 1

# Initialize Arrays
Y = np.zeros([n+1,3])

# Boundary Condition
Y[0,0]= 0
Y[n,0]= 0

Y[0,1]= 0
Y[n,1]= A* np.sin(omega*dt)

for j in range(2000):
    for i in range(n-1):
        temp_element2 = 2*(1-r**2)*Y[i+1,1]-Y[i+1,0]+r**2*(Y[i+2,1]+Y[i,1])
        Y[i+1,2] = temp_element2
    Y[0, 2] = 0
    Y[n, 2] = A * np.sin(omega*(j+2)*dt)
        
    
    for i in range(n+1):
        Y0 = Y[i,1]
        Y1 = Y[i,2]
        Y[i,0]= Y0
        Y[i,1]= Y1
    if (j%100 ==0):
        plt.figure(6)
        plt.subplot(221)
        plt.title('Figure 1-6: omega =942.477796075rad/s',fontsize=8)
        plt.plot(Y[:,1])
        plt.ylabel('Vertical Disp. (meters)',fontsize=8)    
        plt.xlabel('Gridpoints',fontsize=8)        

omega= 1884.95559215
# Initialize Arrays
Y = np.zeros([n+1,3])
Y[0,0]= 0
Y[n,0]= 0
Y[0,1]= 0
Y[n,1]= A* np.sin(omega*dt)

for j in range(2000):
    for i in range(n-1):
        temp_element2 = 2*(1-r**2)*Y[i+1,1]-Y[i+1,0]+r**2*(Y[i+2,1]+Y[i,1])
        Y[i+1,2] = temp_element2
    Y[0, 2] = 0
    Y[n, 2] = A * np.sin(omega*(j+2)*dt)
        
    
    for i in range(n+1):
        Y0 = Y[i,1]
        Y1 = Y[i,2]
        Y[i,0]= Y0
        Y[i,1]= Y1
    if (j%100 ==0):
        plt.figure(6)
        plt.subplot(222)
        plt.title('Figure 1-6: omega= 1884.95559215rad/s',fontsize=8)
        plt.plot(Y[:,1])
        plt.xlabel('Gridpoints',fontsize=8)        
        plt.ylabel('Vertical Disp. (meters)',fontsize=8)
omega= 2827.43338823
# Initialize Arrays
Y = np.zeros([n+1,3])
Y[0,0]= 0
Y[n,0]= 0
Y[0,1]= 0
Y[n,1]= A* np.sin(omega*dt)

for j in range(2000):
    for i in range(n-1):
        temp_element2 = 2*(1-r**2)*Y[i+1,1]-Y[i+1,0]+r**2*(Y[i+2,1]+Y[i,1])
        Y[i+1,2] = temp_element2
    Y[0, 2] = 0
    Y[n, 2] = A * np.sin(omega*(j+2)*dt)
        
    
    for i in range(n+1):
        Y0 = Y[i,1]
        Y1 = Y[i,2]
        Y[i,0]= Y0
        Y[i,1]= Y1
    if (j%100 ==0):
        plt.figure(6)
        plt.subplot(223)
        plt.title('Figure 1-6: omega= 2827.43338823rad/s',fontsize=8)
        plt.plot(Y[:,1])
        plt.ylabel('Vertical Disp. (meters)',fontsize=8)
        plt.xlabel('Gridpoints',fontsize=8)
omega= 3769.9111843
# Initialize Arrays
Y = np.zeros([n+1,3])
Y[0,0]= 0
Y[n,0]= 0
Y[0,1]= 0
Y[n,1]= A* np.sin(omega*dt)

for j in range(2000):
    for i in range(n-1):
        temp_element2 = 2*(1-r**2)*Y[i+1,1]-Y[i+1,0]+r**2*(Y[i+2,1]+Y[i,1])
        Y[i+1,2] = temp_element2
    Y[0, 2] = 0
    Y[n, 2] = A * np.sin(omega*(j+2)*dt)
        
    
    for i in range(n+1):
        Y0 = Y[i,1]
        Y1 = Y[i,2]
        Y[i,0]= Y0
        Y[i,1]= Y1
    if (j%100 ==0):
        plt.figure(6)
        plt.subplot(224)
        plt.title('Figure 1-6: omega= 3769.9111843rad/s',fontsize=8)
        plt.plot(Y[:,1])
        plt.ylabel('Vertical Disp. (meters)',fontsize=8)
        plt.xlabel('Gridpoints',fontsize=8)        
        plt.tight_layout()