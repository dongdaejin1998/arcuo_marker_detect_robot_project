import time
import cv2
import numpy as np
import aruco_detect
import matplotlib.pyplot as plt

transf,data=aruco_detect.aruco()
Px_Pz=[[]]
Py_Pz=[[]]
for i in range(len(data)):

    Px_Pz[i]=np.array((data[i][0],data[i][2]))
    Px_Pz.append([])
    Py_Pz[i]=np.array((data[i][1],data[i][2]))
    Py_Pz.append([])




