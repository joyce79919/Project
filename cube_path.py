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

x = substrate_length/2 - cube_length/2
y = substrate_length/2 - cube_length/2
z = 0
t = 0


def get_path(laser_diameter, cube_length, laser_speed,t,x,y,z):
	path = []
	x_increment = cube_length/(laser_diameter*1.2)
	y_increment = cube_length/(laser_diameter*1.2)
	layer = cube_length/x_increment # number of times laser needs to go upwards

	for i in range(total_number_steps):
		t = t + increment/laser_speed # unit: second
		while x < = cube_length:
			x = x + x_increment
			y = y
			z = z
			t = t + increment/laser_speed # unit: second	
		y = y + y_increment
		t = t + increment/laser_speed # unit: second		
		y_increment = (-1) * y_increment
		path.append([t,x,y.z])

#print(np.shape(path))
np.savetxt('path.txt',path)
