
import time
import cv2
import numpy as np
import aruco_detect,base_cam,kenematics,arduino





# loop over the frames from the video stream



transf=aruco_detect.aruco()


transf[0][3]=transf[0][3]-0.97
transf[1][3]=transf[1][3]+0.58
#transf[2][3]=transf[2][3]
print(transf)


#transf 카메라와 aruco 간의 동차 변환 행렬  x축 8도
base_cam=base_cam.base_cam_matrix(36.5,0,40.5,y_angle=180,z_angle=90)
print(base_cam)
#r_base_cam=base_cam.base_cam_matrix(32.5,5.5,52,y_angle=180,z_angle=90)
targetf=np.identity(n=4,dtype=np.float32)
k= cv2.waitKey()
while True:

    num_list = list(map(float, input().split()))
    targetf[0][3]=num_list[0]
    targetf[1][3]=num_list[1]
    targetf[2][3]=num_list[2]
    print(targetf)
    real_target = np.dot(base_cam, transf)
    real_target = np.dot(real_target, targetf)
    real_target=np.round(real_target,3)
    print(real_target)
    if real_target[2][3]<2:
        real_target[2][3]=0
    elif real_target[2][3]>3:
        real_target[0][3]=real_target[0][3]+3
    x, y, z = real_target[0][3], real_target[1][3], real_target[2][3]
    #round(real_target[2][3]+10.65,2)s
    #초기자세 고려
    #y theta 모터각도 , 계산식 동일
    print(x, y, z)

    theta = kenematics.inverse2(x, y, z)
    print(theta)
    #theta=np.array(["-1 " +theta[0],"-2 "+theta[1],"-3 "+theta[2],"-2 "
    # +theta[3],"-3 "+theta[4],"-2 "+theta[5],"-3 "+theta[6]],dtype=str)
    #theta = np.array(["-1 " + theta[0], "-2 " + theta[1], "-3 " + theta[2]],dtype=str)
    #print(theta)
    theta = np.array([theta[0],  theta[1], theta[2]], dtype=str)
    print(theta)
    arduino.send_data(theta)

    #theta[0]="0"
    #theta[1] = "90"
    #theta[2] = "160"

    #arduino.send_data(theta)





