import serial
import re

ser = serial.Serial(
    port='COM3',
    baudrate=9600,
)


while True:
    if ser.readable():
        res = ser.readline()
        gsrdata = res.decode()[:len(res) - 1]
        print(gsrdata)

        findGsr = []
        findHrt = []
        for s in gsrdata:
         if "gsr" in s:
            findGsr.append(s)
            print(findGsr)
         if "hrt" in s:
            findHrt.append(s)
            print(findHrt)