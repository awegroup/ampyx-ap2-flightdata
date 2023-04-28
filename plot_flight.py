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

plt.close('all')
mpl.rcParams['figure.figsize'] = 10, 8

import scipy.io

def read_variables_from_matlab_file(filename, locations):
    # Load the MATLAB file
    mat = scipy.io.loadmat(filename)
    
    mat = mat['logData_FCC114_1']
    # Initialize a dictionary to hold the variable values
    variable_values = {}
    
    # Loop over the specified locations
    for location_name, location_vars in locations.items():
        # Get the data from the current location
        location_data = mat[location_name][0,0]['packetData'][0,0]
        
        # Initialize a dictionary to hold the variable values for this location
        location_variable_values = {}
        
        # Extract the time variable
        location_variable_values['time'] = mat[location_name][0,0]['time'][0,0]
        
        # Loop over the variable names for this location and extract the corresponding data
        for variable_name in location_vars:
            variable_data = location_data[variable_name][0,0]
            location_variable_values[variable_name] = variable_data
        
        # Add the location variable values to the overall dictionary
        variable_values[location_name] = location_variable_values
    
    return variable_values



#%% Read Variables

# Example usage
filename = 'logData_FCC114_1.mat'
locations = {
    'NavigationData': ['positionNED', 'velocityNED'],
    'ProcessedSensorData': ['trueAirspeed', 'angleOfAttack', 'sideSlip','angleOfAttackValid'],
    'WinchData': ['length_total', 'length_on_drum', 'tether_speed', 'tether_tension','state']
    
    
}

data = read_variables_from_matlab_file(filename, locations)
positionNED= data['NavigationData']['positionNED']
velocityNED = data['NavigationData']['velocityNED']
time_nav = data['NavigationData']['time']-data['NavigationData']['time'][0]
aoa = data['ProcessedSensorData']['angleOfAttack']
aoaValid = data['ProcessedSensorData']['angleOfAttackValid']
time_winch = data['WinchData']['time']-data['WinchData']['time'][0]
tether_speed = data['WinchData']['tether_speed']
tether_tension = data['WinchData']['tether_tension']
length_total = data['WinchData']['length_total']



#%%
valid = aoaValid.astype(bool).flatten()




plt.figure()
plt.plot(time_nav[valid], positionNED[valid,0])
plt.xlabel('Time [s]')
plt.ylabel('x [m]')


plt.figure()
plt.plot(time_nav[valid], aoa[valid]*180/np.pi)
plt.xlabel('Time [s]')
plt.ylabel('Angle of Attack [deg]')


start = 30000
plt.figure()
plt.plot(time_winch[start:], tether_tension[start:])
plt.xlabel('Time [s]')
plt.ylabel('Tether Tension [N]')



fig = plt.figure()
ax  = fig.gca(projection='3d')

ax.plot(-positionNED[valid,0], -positionNED[valid,1], -positionNED[valid,2])

