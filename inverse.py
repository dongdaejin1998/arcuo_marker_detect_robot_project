import math
import numpy
#import arduino

th,d,L,a=0,0,0,0
th1,d1,L1,a1=0,0,0,0
th2,d2,L2,a2=0,0,0,0
#베이스 모터1->모터2 사이 거리(l1)
l1=11.5
#모터1->모터2 사이 거리(l2)
l2=25
#모터2->앤드이펙터 사이 거리(l3)
l3=37



def inverse(Px,Py,Pz):


    r=math.sqrt(Px**2+Py**2)


    Inv_th1=math.atan2(Py,Px)
    Inv_th1=numpy.degrees(Inv_th1)
    print(Inv_th1)
    Inv_th1=abs(Inv_th1-90)

    k = math.sqrt(r ** 2 + ((Pz - l1) ** 2))

    Inv_th3 = math.acos((k ** 2 - l2 ** 2 - l3 ** 2) / (2 * l2 * l3))
    Inv_th3 = numpy.degrees((Inv_th3))
    print(Inv_th3)


    beta=numpy.degrees(math.atan2(Pz-l1,r))
    alpha = numpy.degrees(math.atan2(l3 * math.sin(math.radians(Inv_th3)), (l2 + l3 * math.cos(math.radians(Inv_th3)))))

    Inv_th2=beta-alpha
    print(Inv_th2)
    Inv_th2=Inv_th2



    #theta=np.array((Inv_th1,Inv_th2,Inv_th3),dtype=int)
    #theta = np.array(theta,dtype=str)

    theta = numpy.array((Inv_th1, Inv_th2, Inv_th3), dtype=float)
    theta = numpy.rint(theta)
    theta = theta.astype(int)
    #theta[1] = abs(theta[1]) + 10
    #theta[2] = 360 - theta[1] - abs(theta[2])
    theta=numpy.array(theta,dtype=str)
    return theta

while True:
    num_list = list(map(int, input().split()))
    Px = num_list[0]
    Py = num_list[1]
    Pz = num_list[2]
    theta=inverse(Px, Py, Pz)

    print(theta)
    theta = numpy.array(["-1 " + theta[0], "-2 " + theta[1], "-3 " + theta[2]], dtype=str)

    print(theta)
    #arduino.send_data(theta)

    #theta[0] = "-3 160"
    #theta[1] = "-2 90"
    #theta[2] = "-1 0"
    #arduino.send_data(theta)