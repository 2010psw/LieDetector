import serial
import re

ser = serial.Serial(
    port='COM3',
    baudrate=9600,
)

findGsr = list()
findHrt = list()

while True:
    if ser.readable():
        res = ser.readline()
        gsrdata = res.decode()[:len(res) - 1]
        print(gsrdata)


        if 'gsr' in gsrdata:
            findGsr.append(gsrdata)
            print(findGsr)
        if 'hrt=' in gsrdata:
            findHrt.append(gsrdata)
            print(findHrt)
