import serial
import re
import numpy as np
import random
import time
from matplotlib import pyplot as plt
from matplotlib import animation

ser = serial.Serial(
    port='COM3',
    baudrate=9600,
)

S = list()
findGsr = list()
findHrt = list()




while True:
    if ser.readable():
        res = ser.readline()
        gsrdata = res.decode()[:len(res) - 2]
        print(gsrdata)


        if 'gsr' in gsrdata:
            findGsr.append(re.findall("\d+",gsrdata))
            print(findGsr)
        if 'hrt=' in gsrdata:
            findHrt.append(re.findall("\d+",gsrdata))
            print(findHrt)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split('m')
            xs.append(findGsr)
            ys.append()
