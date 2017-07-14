# generate a raster path to build the cube button
# diameter of laser and speed of its are user inputs 

from math import *
import numpy as np


#################
## User Inputs ##
#################

laser_diameter = e-3 # unit: m
laser_speed = 0.01 # unit : m/s

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

def get_increment(laser_diameter, cube_length):
	increment=0
	if (cube_length/laser_diameter <= 0.9 * laser_diameter):
	
	return increment

def get_path(laser_diameter, cube_length, increment, layer, laser_speed):
	path = []
	for z in range(layer):
		t = t + increment/laserr_speed #second
		path.append([t,x,y.z])




print(np.shape(path))
np.savetxt('path.txt',path)
