import numpy as np
from math import *




def base_cam_matrix(x,y,z,x_angle=0,y_angle=0,z_angle=0):
    base_cam_trans=np.identity(n=4,dtype=np.float32)
    base_cam_trans[0][3] = x
    base_cam_trans[1][3] = y
    base_cam_trans[2][3] = z
    R=angle_rotation(x_angle,y_angle,z_angle)
    base_cam=np.dot(base_cam_trans,R)
    base_cam=np.round(base_cam,3)
    return base_cam
def angle_rotation(x_angle,y_angle,z_angle):
    x=x_angle*pi/180
    y = y_angle * pi / 180
    z = z_angle * pi / 180

    R_x=np.array([[1,0,0,0],[0,cos(x),-sin(x),0],[0,sin(x),cos(x),0],[0,0,0,1]])
    R_y=np.array([[cos(y),0,sin(y),0],[0,1,0,0],[-sin(y),0,cos(y),0],[0,0,0,1]])
    R_z=np.array([[cos(z),-sin(z),0,0],[sin(z),cos(z),0,0],[0,0,1,0],[0,0,0,1]])
    R=np.dot(R_x,R_y)
    R=np.dot(R,R_z)
    return R
