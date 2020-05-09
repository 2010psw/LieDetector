import serial

ser = serial.Serial(
    port='COM4',
    baudrate=9600,
)


while True:
    if ser.readable():
        res = ser.readline()
        gsrdata = res.decode()[:len(res) - 1]
        print(gsrdata)