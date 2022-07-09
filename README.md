### arcuo_marker_detect_robot_project

## 목적
본 프로젝트는 AI로봇디자인이라는 수업을 통해서 진행되었다. 로봇아르테에서 의뢰를 받아서 만든 로봇이며 목적은 카메라를 통해서 엔드이펙터가 원하는 위치로 이동하고자 했다.

## 1.기구부 제작
기구부는 솔리드웍스를 하는 팀원들을 통해서 진행되었으며 간단하게 설명하고자 한다. 로봇은 4절링크가 포함되어있는 3자유도를 가진 로봇팔을 제작하였다.

## 2.카메라 보정 및 마커감지
카메라 보정은 chessboard와 charucoboard 두개로 진행하였으며 chessboard 이미지는 images파일에 있으며 charucoboard이미지는 chruco_images 파일에 저장되어있다. chessboard는 calibration.py 파일을 실행하게 되면 보정에 필요한 5개의 파라미터를 numpy파일로 저장하게 설계했다. 그리고 charuco image는 charuco_calibration.py 파일을 실행하게 되면 5개의 파라미터를 numpy파일로 저장하게 설계했다. 두개의 numpy파일로 marker을 감지하였을 경우 chessboard의 파라미터가 좀더 정확한 동차변환 행렬을 추출하는것을 확인하였기에 본 프로젝트에서는 chessboard의 파라미터를 사용하였다. 그래픽 마커는 aruco 마커를 사용하여 감지하였다.

## 3.역기구학 및 행렬변환식 계산
base_cam.py파일은 로봇베이스에서 캠까지의 동차변환행렬을 만들어주는 파일이다. 그리고 카메라에서 마커까지의 동차변환 행렬은 2번 목차에서 다루었다. 그리고 kenematics.py에서 inverse2는 우리 3자유도 로봇의 역기구학을 계산해주는 함수이다. 계산된 theta값을 계산했다.

## 4.아두이노로 값 전달
arduino.py는 시리얼 통신을 통해서 파이썬에서 아두이노로 값을 보내는 파일이며 보내는 값은 모터 세개의 값을 string형태로 아두이노로 보내주었다.



https://user-images.githubusercontent.com/35069745/178119528-90d6636e-a23b-46f1-b741-16b91d077d10.mp4



# 자세한 내용은 pdf파일을 참고하시면 자세하게 나와있습니다.
