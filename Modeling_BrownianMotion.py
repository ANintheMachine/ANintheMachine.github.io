# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:18:54 2019

@author: Arun-SP
"""
#Import needed python libraries and packages for calculations
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import math 

df = pd.read_fwf('brownpy_testwo.txt')

#Saved text file of data as .csv
#Used a panda attribute to read .csv, and labeled DataFrame as "df"
#df = pd.read_csv('brownpanda.csv')
#df = pd.read_csv('data_table_out.csv')

#Used panda attribute DataFrame.diff() to calculate dt,dx,dy
df=df.diff(axis = 0, periods = 1) 
#Used DataFrame.drop() to delete headers, and DataFrame.rename() to rename
#them as the correct headers dt,dx,dy
df=df.drop(df.index[0])
#df=df.drop(df.columns[0], axis=1)
print(list(df.columns.values))
df= df.rename(columns={'0.0000000e+00': 'dt', '3.7642640e+01': 'dx','3.0815820e+01':'dy'})
#Squared both dx and dy
df['dx'] = df['dx'].apply(np.square)
df['dy'] = df['dy'].apply(np.square)
#Added dx^2 and dy^2 to get dr^2
df['dr']=df['dx']+df['dy']

#Used panda attribute .mean() to find the average of the dr^2 column
dr2=df['dr'].mean()
#Converted dr^2 column values from um^2 to m^2
dr2=dr2*(10**-12)
#Used panda attribute .describe() to give more statistical data
print(df['dr'].describe())
#Defined function to calcualte Boltzmann Constant
# t=combination time, n=dynamic viscosity, T=temperature, a=particle radius
def boltz(t,n,a,T):
   return (6*(math.pi)*n*a*(dr2))/(4*t*T)

print(boltz(0.04,0.00089,0.4e-06,298))

