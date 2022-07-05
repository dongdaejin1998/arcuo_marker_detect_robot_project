import serial
import time


arduino = serial.Serial('COM3',9600)


def send_data(data):
    #for i in range(len(data)):
    c=" ".join(data)
    print(c)
    c=c.encode('utf-8')
    arduino.write(c)
    time.sleep(10)

