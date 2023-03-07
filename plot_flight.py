#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 08:13:07 2020

@author: rschmehl
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.io import loadmat

mpl.rcParams['figure.figsize'] = 10, 8

mat = loadmat('logData_FCC114_1.mat')
#print(mat.keys())
#print(mat)

#print(mat['__header__'])

data        = mat['logData_FCC114_1']
time        = data['NavigationData'][0,0]['time'][0,0]
positionNED = data['NavigationData'][0,0]['packetData'][0,0]['positionNED'][0,0]

print(time.shape)
print(positionNED.shape)

plt.plot(time[62775:], positionNED[62775:,0])
plt.xlabel('Time [s]')
plt.ylabel('x [m]')

fig = plt.figure()
ax  = fig.gca(projection='3d')

ax.plot(-positionNED[62775:,0], -positionNED[62775:,1], -positionNED[62775:,2])


#plot(logData_FCC114_1.NavigationData.time(62775:end), logData_FCC114_1.NavigationData.packetData.positionNED(62775:end, 3))
#hold on
#plot(validationData.times(2:end), validationData.response.p(3,:))

#Starttime = datetime(logData_FCC114_1.NavigationData.packetData.UTC_Time(62775),'ConvertFrom','epochtime’)
#Starttime = 03-Oct-2017 11:23:27.