import math

import numpy
import numpy as np



th,d,L,a=0,0,0,0
th1,d1,L1,a1=0,0,0,0
th2,d2,L2,a2=0,0,0,0
#베이스 모터1->모터2 사이 거리(l1)
l1=11.9
#모터1->모터2 사이 거리(l2)
l2=25
#모터2->앤드이펙터 사이 거리(l3)
l3=37

def HTM(th,d,L,a):
    th=math.radians(th)
    a=math.radians(a)
    T=np.array([[math.cos(th),-(math.sin(th)*math.cos(a)),math.sin(th)*math.sin(a),L*math.cos(th)],
       [math.sin(th),math.cos(th)*math.cos(a),-(math.cos(th)*math.sin(a)),L*math.sin(th)],
       [0,math.sin(a),math.cos(a),d],
       [0,0,0,1]])
    T=np.round(T,4)

    return T
"""
def inverse(Px,Py,Pz):


    r=math.sqrt(Px**2+Py**2)

    Inv_th1=math.atan2(Py,Px)
    Inv_th1=numpy.degrees(Inv_th1)

    k=math.sqrt(r**2+((Pz-l1)**2))

    Inv_th3=math.acos((k**2-l2**2-l3**2)/(2*l2*l3))
    Inv_th3=-numpy.degrees((Inv_th3))


    beta=numpy.degrees(math.atan2(Pz-l1,r))
    alpha=numpy.degrees(math.atan2(l3*math.sin(math.radians(Inv_th3)),(l2+l3*math.cos(math.radians(Inv_th3)))))

    Inv_th2=beta-alpha
    r_Inv_th1 = Inv_th1 + 90
    r_Inv_th3=Inv_th3-Inv_th2
    r_Inv_th2=Inv_th2
    print(r_Inv_th1,r_Inv_th2,r_Inv_th3)

    theta=np.array((Inv_th1,Inv_th2,Inv_th3),dtype=int)

    return theta

"""

def inverse2(Px,Py,Pz):


    r=math.sqrt(Px**2+Py**2)

    Inv_th1=math.atan2(Py,Px)
    Inv_th1=numpy.degrees(Inv_th1)


    k=math.sqrt(r**2+((Pz-l1)**2))
    print(k)
    Inv_th3_cos=(k**2-l2**2-l3**2)/(2*l2*l3)
    Inv_th3_sin=-math.sqrt((1-(Inv_th3_cos**2)))
    print(Inv_th3_sin,Inv_th3_cos)
    Inv_th3=math.atan2(Inv_th3_sin,Inv_th3_cos)
    Inv_th3=numpy.degrees((Inv_th3))


    beta=numpy.degrees(math.atan2(Pz-l1,r))
    print(beta)
    alpha=numpy.degrees(math.atan2(l3*math.sin(math.radians(Inv_th3)),(l2+l3*math.cos(math.radians(Inv_th3)))))
    print(alpha)
    Inv_th2=beta-alpha

    print(Inv_th1,Inv_th2,Inv_th3)

    r_Inv_th1 = 90-Inv_th1
    r_Inv_th3=150-abs(Inv_th3+Inv_th2)
    r_Inv_th2=180-Inv_th2
    print(r_Inv_th1,r_Inv_th2,r_Inv_th3)

    """
    r_theta=[]
    
    r_Inv_th2_fake=r_Inv_th2/3
    r_Inv_th3_fake=r_Inv_th3/3
    r_Inv_th2=r_Inv_th2_fake
    r_Inv_th3=r_Inv_th3_fake
    print(r_Inv_th2,r_Inv_th3)
    r_theta.append(r_Inv_th1)
    for i in range(3):
        r_theta.append(r_Inv_th2)
        r_theta.append(r_Inv_th3)

        r_Inv_th2=r_Inv_th2+r_Inv_th2_fake
        r_Inv_th3=r_Inv_th3+r_Inv_th3_fake
    print(r_theta)
    """

    r_theta = np.array((r_Inv_th1,r_Inv_th2,r_Inv_th3), dtype=float)
    #theta = np.array((Inv_th1, Inv_th2, Inv_th3), dtype=float)
    r_theta=np.round(r_theta,2)
    r_theta=numpy.array(r_theta,dtype=str)
    #print(r_theta)

    return r_theta


"""
r_theta,theta=inverse2(30,0,0)
print(theta)



th,th1,th2=theta[0],theta[1],theta[2]
T_01=HTM(th,l1,0,90)
T_12=HTM(th1,0,l2,0)
T_23=HTM(th2,0,l3,0)

T_02=np.matmul(T_01,T_12)

T_03=np.matmul(T_02,T_23)
T_03=np.round(T_03,4)
print(T_03)

Px,Py,Pz=T_03[0][3],T_03[1][3],T_03[2][3]
"""
