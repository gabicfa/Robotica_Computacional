#!/usr/bin/env python

#!/usr/bin/env python

# Execute sudo pkill -HUP -f tcp_serial_redirect0.py antes de executar este programa
# Para desbloquear a serial



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

    ser.write("TestMode on\n")
    time.sleep(2)
    data = read()
    print(data)
    ser.write("GetAnalogSensors brief\n")

    time.sleep(1)
    data = read()
    lista = data.split(",")
    print(lista[1])
    print(lista[5])
    print(lista[6])

    while int(lista[1]) <= 100 and int(lista[5])<=50 and int(lista[6])<=50:
        if int(lista[1])<=45 :
            ser.write("SetMotor 100 100 120\n")
            time.sleep(0.1)
            ser.write("TestMode on\n")
            time.sleep(0.1)
            data = read()
            print(data)
            ser.write("GetAnalogSensors brief\n")
            time.sleep(1)
            data = read()
            lista = (data.split(","))
            print(lista[1])
        elif int(lista[1])>45:
            ser.write("SetMotor 100 -100 30\n")
            time.sleep(0.1)
            ser.write("SetMotor 100 100 120\n")
            time.sleep(0.1)
            ser.write("SetMotor -100 100 30\n")
            time.sleep(0.1)
            ser.write("TestMode on\n")
            time.sleep(0.1)
            data = read()
            print(data)
            ser.write("GetAnalogSensors brief\n")
            time.sleep(1)
            data = read()
            lista = (data.split(","))
        else:
            ser.write("SetMotor -100 100 30\n")
            time.sleep(0.1)
            ser.write("SetMotor 100 100 70\n")
            time.sleep(0.1)
            ser.write("SetMotor 100 -100 30\n")
            time.sleep(0.1)
            ser.write("TestMode on\n")
            time.sleep(0.1)
            data = read()
            print(data)
            ser.write("GetAnalogSensors brief\n")
            time.sleep(1)
            data = read()
            lista = (data.split(","))

    ser.close()


if __name__ == "__main__":
    main()
