# generate a raster path to build the cube button
# diameter of laser and speed of its are user inputs 

from math import *
import numpy as np


#################
## User Inputs ##
#################

laser_diameter = 2.5e-3 # unit: m
laser_speed = 0.01 # unit: m/s

##################
### Fixed Data ###
##################

substrate_length = 0.2 # unit: m
cube_length = 0.06985 # unit: m

###############
#### Codes ####
###############

x_0 = substrate_length/2 - cube_length/2
y_0 = substrate_length/2 - cube_length/2
z_0 = 0
t = 0


def get_path(laser_diameter, cube_length, laser_speed,t):
	path = []
	increment = cube_length/(laser_diameter*1.2)
	layer = cube_length/increment

	for z in range(layer):
		t = t + increment/laser_speed # unit: second
		path.append([t,x,y.z])

#print(np.shape(path))
np.savetxt('path.txt',path)
