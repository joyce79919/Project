# generage a raster path to build the cubit button

from math import *
import numpy as np
import turtle

length_substrate = 2 #unit:m
length_deposition = 0.06985 # unit: m

x_0 = length_substrate/2 - length_deposition/2
y_0 = length_substrate/2 - length_deposition/2

def go(step, heading):
     turtle.setheading(heading)
     turtle.forward(step)
  
def go_down(step):
     go(step, 270)
def go_up(step):
     go(step, 90)
def go_right(step):
     go(step, 0) 
def go_left(step):
     go(step, 180)
