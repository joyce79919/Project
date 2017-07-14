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

def get_increment(cube_length, laser_diameter):
	increment = cube_length / (laser_diameter *1.2)
	return increment

def x_path(cube_length, laser_speed, x, y, z, t):
	x_inc = get_increment()
	x_path = []
	while x < = cube_length:
		x = x + x_inc
		y = y
		z = z
		t = t + x_inc / laser_speed
		x_path.append([t,x,y,z])
	return x_path

def y_path(laser_speed, x, y, z, t):
	y_inc = get_increment()
	y_path = []
	x = x
	y = y + y_inc
	t = t + y_inc / laser_speed
	z = z
	y_inc = (-1) * y_inc
	y_path.append([t,x,y,z])
	return y_path

def z_path(laser_speed, x, y, z, t):
	z_inc = get_increment()
	z_path = []
	x = x 
	y = y	
	z = z + z_inc
	return z_path

def get_path(laser_diameter, cube_length, laser_speed,t,x,y,z):
	path = []
	a = get_increment()
	layer = cube_length/a # number of times laser needs to go upwards

	for i in range(layer):
		inc = get_increment()
		while (y + inc) < = cube_length:
			path = np.concatenate((path,x_path()))
			path = np.concatenate((path,y_path()))
		z_path()
		#path.append([t,x,y.z])

#print(np.shape(path))
np.savetxt('path.txt',path)
