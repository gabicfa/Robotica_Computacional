
import sys
import os
import time
import signal
import threading
import socket
import codecs
import serial
from os import system

ser  = None

def connect_to_serial():
    global ser
    # connect to serial port
    possible_ports = ['/dev/ttyUSB0','/dev/ttyUSB1']
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.parity   = 'N'
    ser.rtscts   = False
    #ser.xonxoff  = options.xonxoff
    ser.timeout  = 1     # required so that the reader thread can exit
    for p in possible_ports:
        ser.port = p
        try:
            ser.open()
            print "Connected on port: " + p
            return ser
        except:
            time.sleep(1)

def read():
    n = ser.inWaiting()
    data = ser.read(n)
    return data



def main():

    print("Starting connection to Neato on ports")

    ser = connect_to_serial()

    while True: 
        ser.write("TestMode on\n")
        time.sleep(2)
        data = read()
        print(data)

        ser.write("SetLDSRotation On\n")
        time.sleep(5)
        data = read()
        #print(data)

        ser.write("GetLDSScan\n")
        time.sleep(5)
        data = read()
        time.sleep(5)
        d2 = read()
        data = data + d2
        data = data.split("\n")
        cortado = [linha.strip().split(",") for linha in data]
        perto= 1400
        print(cortado)
       
        dic_dis={}

        for lista in range(3,361):
            angulo=int(cortado[lista][0])
            distancia=int(cortado[lista][1])
            #print("dist ", distancia)
            dic_dis[distancia]=angulo
            if int(cortado[lista][3])==0:
                if distancia>600 and distancia<1400:
                    if distancia<perto:
                        perto=distancia
            print(perto)

        ang =dic_dis[perto]
        dis = perto-600

        if ang==0:

            if dis<=300:

                ser.write("SetMotor 300 300 {0} \n".format(dis))
                time.sleep(1)
            
            if dis<=600 and dis>300:

                dis=dis-300
                ser.write("SetMotor 300 300 300 \n")
                time.sleep(1)
                ser.write("SetMotor 300 300 {0} \n".format(dis))
                time.sleep(1)

            else:
                dis=dis-600
                ser.write("SetMotor 300 300 300")
                time.sleep(1)
                ser.write("SetMotor 300 300 300")
                time.sleep(1)
                ser.write("SetMotor 300 300 {0} \n".format(dis))
                time.sleep(1)

        else:
            if ang <180:
                if ang<90:

                    v_motor1= -(185*ang)/90
                    v_motor2= (185*ang)/90

                    ser.write("SetMotor {0} {1} 200 \n".format(v_motor1, v_motor2))
                    time.sleep(1)

                    if dis<=300:

                        ser.write("SetMotor 300 300 {0} \n".format(dis))
                        time.sleep(1)
                    
                    if dis<=600 and dis>300:

                        dis=dis-300
                        ser.write("SetMotor 300 300 300 \n")
                        time.sleep(1)
                        ser.write("SetMotor 300 300 {0} \n".format(dis))
                        time.sleep(1)

                    else:
                        dis=dis-600
                        ser.write("SetMotor 300 300 300")
                        time.sleep(1)
                        ser.write("SetMotor 300 300 300")
                        time.sleep(1)
                        ser.write("SetMotor 300 300 {0} \n".format(dis))
                        time.sleep(1)




                else:
                    ang=ang-90


                    v_motor1= -(185*ang)/90
                    v_motor2= (185*ang)/90

                    ser.write("SetMotor -185 185 200 \n")
                    time.sleep(1)
                    ser.write("SetMotor {0} {1} 300 \n".format(v_motor1, v_motor2))
                    time.sleep(1)


                    if dis<=300:

                        ser.write("SetMotor 300 300 {0} \n".format(dis))
                        time.sleep(1)
                    
                    if dis<=600 and dis>300:

                        dis=dis-300
                        ser.write("SetMotor 300 300 300 \n")
                        time.sleep(1)
                        ser.write("SetMotor 300 300 {0} \n".format(dis))
                        time.sleep(1)

                    else:
                        dis=dis-600
                        ser.write("SetMotor 300 300 300")
                        time.sleep(1)
                        ser.write("SetMotor 300 300 300")
                        time.sleep(1)
                        ser.write("SetMotor 300 300 {0} \n".format(dis))
                        time.sleep(1)
            else:
                if ang<270:

                    ang=270-ang

                    v_motor1= (185*ang)/90
                    v_motor2= -(185*ang)/90

                    ser.write("SetMotor 185 -185 200 \n")
                    time.sleep(1)

                    ser.write("SetMotor {0} {1} 200 \n".format(v_motor1, v_motor2))
                    time.sleep(1)

                    if dis<=300:

                        ser.write("SetMotor 300 300 {0} \n".format(dis))
                        time.sleep(1)
                    
                    if dis<=600 and dis>300:

                        dis=dis-300
                        ser.write("SetMotor 300 300 300 \n")
                        time.sleep(1)
                        ser.write("SetMotor 300 300 {0} \n".format(dis))
                        time.sleep(1)

                    else:
                        dis=dis-600
                        ser.write("SetMotor 300 300 300")
                        time.sleep(1)
                        ser.write("SetMotor 300 300 300")
                        time.sleep(1)
                        ser.write("SetMotor 300 300 {0} \n".format(dis))
                        time.sleep(1)
                else:
                    ang=360-ang
                    v_motor1= (185*ang)/90
                    v_motor2= -(185*ang)/90
                    ser.write("SetMotor {0} {1} 200 \n".format(v_motor1, v_motor2))
                    time.sleep(1)

                    if dis<=300:

                        ser.write("SetMotor 300 300 {0} \n".format(dis))
                        time.sleep(1)
                    
                    if dis<=600 and dis>300:

                        dis=dis-300
                        ser.write("SetMotor 300 300 300 \n")
                        time.sleep(1)
                        ser.write("SetMotor 300 300 {0} \n".format(dis))
                        time.sleep(1)

                    else:
                        dis=dis-600
                        ser.write("SetMotor 300 300 300")
                        time.sleep(1)
                        ser.write("SetMotor 300 300 300")
                        time.sleep(1)
                        ser.write("SetMotor 300 300 {0} \n".format(dis))
                        time.sleep(1)

    ser.write("SetLDSRotation Off\n")
    time.sleep(1)
    data = read()
    #print(data)

    ser.close()


if __name__ == "__main__":
    main()
