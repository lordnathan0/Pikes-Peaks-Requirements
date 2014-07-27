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

file_dir = 'C:/Users/Nathan/Desktop/Git/Pikes Peak Requirements/PPIHC torque-rpm mapping data - 2014-07-27.json'

json_data=open(file_dir).read()

data = json.loads(json_data)

passlower = 9*60 + 44
passhigher = 9*60 + 46

rpm_list = list()
torque_list = list()
time_list = list()
average_power_list = list()

pass_list = list()

index = 0

for r in data.keys():
    for t in data[r].keys():
        rpm_list.append(float(r))
        torque_list.append(float(t))
        time_list.append(data[r][t]['Finish time'])
        average_power_list.append(data[r][t]['Average power'])
        
        if (data[r][t]['Finish time'] >= passlower) and (data[r][t]['Finish time'] <= passhigher):
            pass_list.append(index)
        
        index = index + 1

rpm = np.array(rpm_list)
torque = np.array(torque_list)
time = np.array(time_list)
average_power = np.array(average_power_list)


figure('average power')
scatter(rpm,torque, c = average_power, edgecolors = 'none', vmin = min(average_power), vmax = max(average_power))
colorbar()
scatter(rpm[pass_list],torque[pass_list], c = average_power[pass_list], marker = 's', s = 50, vmin = min(average_power), vmax = max(average_power))

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