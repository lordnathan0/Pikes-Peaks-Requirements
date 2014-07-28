# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 17:39:32 2014

@author: Nathan
"""

import json
import pickle
import numpy
import os.path

from scipy.interpolate import griddata,interp1d

passlower = 9*60 + 44
passhigher = 9*60 + 46

file_dir_list = ['data/11_7.json', 'data/11_10.json',  'data/12_11.json', 'data/12_7.json', 'data/13_12.json', 'data/10_9.json', 'data/10_7.json', 'data/9_9.json', 'data/9_7.json', 'data/13_7.json']

f = list()

for d in file_dir_list:
    json_data=open(d).read()
    
    data = json.loads(json_data)
    

    
    rpm_list = list()
    torque_list = list()
    time_list = list()
    average_power_list = list()
    peak_power_list = list()
    energy_list = list()
    
    pass_list = list()
    
    index = 0
    
    for r in data.keys():
        for t in data[r].keys():
            rpm_list.append(float(r))
            torque_list.append(float(t))
            time_list.append(data[r][t]['Finish time'])
            average_power_list.append(data[r][t]['Average power'])
            peak_power_list.append(data[r][t]['Maximum power'])
            energy_list.append(data[r][t]['Energy used'])
            
            if (data[r][t]['Finish time'] >= passlower) and (data[r][t]['Finish time'] <= passhigher):
                pass_list.append(index)
                print d + ',' + repr(float(r)) + ',' + repr(float(t)) + ',' + repr(data[r][t]['Average power']) + ',' + repr(data[r][t]['Maximum power']) + ',' + repr(data[r][t]['Energy used']) + ',' + repr(data[r][t]['Finish time']) 
            
            index = index + 1
            
        
    
    rpm = np.array(rpm_list) #0
    torque = np.array(torque_list)
    time = np.array(time_list)
    average_power = np.array(average_power_list)
    peak_power = np.array(peak_power_list)
    energy = np.array(energy_list)
    pass_array = np.array(pass_list)
    
    data = list()
    
    data.append(rpm.copy())
    data.append(torque.copy())
    data.append(time.copy())
    data.append(average_power.copy())
    data.append(peak_power.copy()) 
    data.append(energy.copy())
    data.append(pass_array.copy())
    
    f.append(data)
    
    figure(d + ' average power')
    scatter(rpm,torque, c = average_power, edgecolors = 'none', vmin = min(average_power), vmax = max(average_power))
    colorbar()
    scatter(rpm[pass_list],torque[pass_list], c = average_power[pass_list], marker = 's', s = 50, vmin = min(average_power), vmax = max(average_power))

    figure(d + ' peak power')
    scatter(rpm,torque, c = peak_power, edgecolors = 'none', vmin = min(peak_power), vmax = max(peak_power))
    colorbar()
    scatter(rpm[pass_list],torque[pass_list], c = peak_power[pass_list], marker = 's', s = 50, vmin = min(peak_power), vmax = max(peak_power))

    figure(d + ' energy')
    scatter(rpm,torque, c = energy, edgecolors = 'none', vmin = min(energy), vmax = max(energy))
    colorbar()
    scatter(rpm[pass_list],torque[pass_list], c = energy[pass_list], marker = 's', s = 50, vmin = min(energy), vmax = max(energy))

#x = rpm
#y = torque
#z = average_power

#points = np.transpose(np.array([y,x]))
#values = np.array(z)
#
#grid_x, grid_y = np.mgrid[np.min(y):np.max(y)+1, np.min(x):np.max(x)+1]
#show_grid = griddata(points, values, (grid_x, grid_y), method='linear')

#
#figure('heat map')
#imshow(show_grid, aspect = 'auto', origin = 'lower')
##scatter(rpm[pass_list], torque[pass_list], c = average_power[pass_list], marker = 's', s = 50, vmin = min(average_power), vmax = max(average_power))
#colorbar()