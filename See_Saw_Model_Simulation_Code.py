#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
See Saw Model Simulation Code


@author: Paarth Rathore
"""
# import python libraries for math/plotting
import numpy as np
import matplotlib.pyplot as plt

# define parameters
m = 0.65 # mass in kg
r = 4.2 # radius in m
p = -5 # proportional gain
d = -2      # derivative gain

A = np.array([[0,1],[(3/(m*r))*p,(3/(m*r))*d]]) # system matrix

# define initial condition
o0 = 45 # angle in degrees
w0 = 1 # angular velocity

x0 = np.array([[o0],[w0]]) # initial state vector

# define the time vector
t0 = 0 # initial time (seconds)
tf = 40 # final time
dt = 0.01 # time step
N = int(tf/dt) # number of time steps

# create a time vector
time_vector = np.linspace(t0,tf,num=N)

# numerical integration with Newton's Method
x_k = x0 # set the initial condition as the current state
x_save = np.zeros((x0.shape[0],int(tf/dt))).astype(float) #state history
x_save[:,0] = x_k.transpose() # transpose flips the vector/matrix

# fill in x_save at each step using a for loop
for i in range(time_vector.shape[0]-1):

    x_k_dot = np.dot(A,x_k)
    
    x_kk = x_k_dot*dt + x_k # update step
    
    x_save[:,i+1] = x_kk.transpose()
    x_k = x_kk
    #print(x_save)
    
### Plotting
plt.plot(time_vector,x_save[0,:]) # plot position
plt.plot(time_vector,x_save[1,:]) # plot velocity

plt.title("See Saw Control Algorithm")
plt.xlabel("time (sec.)")
plt.ylabel("system states")
plt.legend(['Position (m.)','Velocity (m./sec.)'])
plt.minorticks_on()
plt.grid(which='minor', color='#DDDDDD', linestyle=':', linewidth=0.5)