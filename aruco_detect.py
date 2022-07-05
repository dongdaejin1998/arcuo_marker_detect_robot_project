import cv2
import numpy as np
import base_cam

arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
arucoParams = cv2.aruco.DetectorParameters_create()

# initialize the video stream and allow the camera sensor to warm up

np.set_printoptions(suppress=True)

a = np.load("camera_calibration.npz")
mtx = a['mtx']
dist = a['dist']
capture=cv2.VideoCapture(0)

#calibration_vector=base_cam.base_cam_matrix(0,0,0,x_angle=-9,z_angle=3)
#print(calibration_vector)
k=cv2.waitKey(0)
#data=[]
def aruco():
    while True:
        ret, frame = capture.read()
        #frame=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
        # frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # detect ArUco markers in the input frame
        #ret, frame = cv2.threshold(frame, 0, 255, cv2.THRESH_OTSU)
        h, w = frame.shape[:2]
        newcameraMtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
        cam_mid_h=h//2
        cam_mid_w=w//2

        frame = cv2.undistort(frame, mtx, dist, None, newcameraMtx)

        x, y, w, h = roi

        frame = frame[y:y + h, x:x + w]

        (corners, ids, rejected) = cv2.aruco.detectMarkers(frame,
                                                           arucoDict, parameters=arucoParams)
        #cv2.line(frame,(cam_mid_w,50),(cam_mid_w,h-50),(255,0,0),2)
        #cv2.line(frame, (50, cam_mid_h), (w-50, cam_mid_h), (0, 255, 0), 2)
        """
        # Aruco Perimeter
        aruco_perimeter = cv2.arcLength(corners[0], True)

        # Pixel to cm ratio
        pixel_cm_ratio = int(aruco_perimeter // 18)
        print(pixel_cm_ratio)
        
        """
        # verify *at least* one ArUco marker was detected
        if len(corners) > 0:
            # flatten the ArUco IDs list
            ids = ids.flatten()
            #print(ids)
            for i in range(0, len(ids)):
                rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corners[i], 5, mtx, dist)  # For a single marker
                cv2.aruco.drawAxis(frame, mtx, dist, rvec[i], tvec[i],
                            10)  # axis length 100 can be changed according to your requirement
                
                #cv2.circle(frame, (cam_mid_w, cam_mid_h), 4, (0, 0, 255), -1)
                rmat, _ = cv2.Rodrigues(rvec)
                tvec = tvec.reshape(3, 1)
                #angle_fix=base_cam.angle_rotation(x_angle=0,y_angle=0,z_angle=-2.5)

                #print(rmat)
                #data.append(tvec)
                transf = np.concatenate((rmat, tvec), axis=1)

                a = np.array([0, 0, 0, 1])
                transf = np.vstack([transf, a])
                transf = transf.astype(np.float32)
                transf=np.round(transf,3)
                #transf=np.dot(transf,calibration_vector)
                #rmat = np.dot(transf, angle_fix)
                #필요없으면 삭제
                print(transf)
            # loop over the detected ArUCo corners
            for (markerCorner, markerID) in zip(corners, ids):
                # extract the marker corners (which are always returned
                # in top-left, top-right, bottom-right, and bottom-left
                # order)
                corners = markerCorner.reshape((4, 2))
                (topLeft, topRight, bottomRight, bottomLeft) = corners

                # convert each of the (x, y)-coordinate pairs to integers
                topRight = (int(topRight[0]), int(topRight[1]))
                bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
                bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
                topLeft = (int(topLeft[0]), int(topLeft[1]))




                # draw the bounding box of the ArUCo detection
                cv2.line(frame, topLeft, topRight, (0, 255, 0), 2)
                cv2.line(frame, topRight, bottomRight, (0, 255, 0), 2)
                cv2.line(frame, bottomRight, bottomLeft, (0, 255, 0), 2)
                cv2.line(frame, bottomLeft, topLeft, (0, 255, 0), 2)

                # compute and draw the center (x, y)-coordinates of the
                # ArUco marker
                cX = int((topLeft[0] + bottomRight[0]) / 2.0)
                cY = int((topLeft[1] + bottomRight[1]) / 2.0)
                cv2.circle(frame, (cX, cY), 4, (0, 0, 255), -1)
                """
                cv2.circle(frame, (cam_mid_w, cam_mid_h), 2, (255, 0, 0), -1)
                cv2.circle(frame, (cam_mid_w  , cam_mid_h + pixel_cm_ratio), 2, (0, 255, 0), -1)
                cv2.circle(frame, (cam_mid_w  + pixel_cm_ratio,cam_mid_h), 2, (0, 0, 255), -1)
                cv2.circle(frame, (cam_mid_w, cam_mid_h + pixel_cm_ratio*3), 2, (255, 255, 0), -1)
                cv2.circle(frame, (cam_mid_w + pixel_cm_ratio*3, cam_mid_h), 2, (0, 255, 255), -1)
                cv2.circle(frame, (cam_mid_w, cam_mid_h - pixel_cm_ratio * 3), 2, (125, 255, 0), -1)
                cv2.circle(frame, (cam_mid_w - pixel_cm_ratio * 3, cam_mid_h), 2, (0, 125, 255), -1)
                """
                # draw the ArUco marker ID on the frame
                cv2.putText(frame, str(markerID),
                            (topLeft[0], topLeft[1] - 15),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (0, 255, 0), 2)
        # show the output frame
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

        #data=np.array(data)
        #print(data.shape)
    cv2.destroyAllWindows()
    return transf#,data
transf=aruco()