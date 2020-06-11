import serial
import re
import time

def ser_data():
    ser = serial.Serial(
        port='COM3',
        baudrate=9600,
    )


    try:
        dic = {}
        while True:
            if ser.readable():
                res = ser.readline()
                data = res.decode()

                if 'gsr' in data:
                    gsr_1 = data.replace('gsr=', '')
                    gsr_1 = gsr_1.replace('\r', '')
                    gsr_1 = gsr_1.replace('\n', '')
                    dic['gsr'] = gsr_1



                if 'hrt' in data:
                    hrt_1 = data.replace('hrt=', '')
                    hrt_1 = hrt_1.replace('\r', '')
                    hrt_1 = hrt_1.replace('\n', '')
                    if '141' not in data:
                        dic['hrt'] = hrt_1


                if 'gsr' in dic.keys() and 'hrt' in dic.keys() and dic is not None:
                    return(dic)
    except Exception as msg:
        print('err')
        print(msg)
        ser_data()
print(ser_data())

print('======================')
    # return dic


# def tttt():
#     print('asdfasdf')
#     dic = {}
#     while True:
#         if ser.readable():
#             res = ser.readline()
#             read_data = res.decode()[:len(res) - 2]
#
#             if 'gsr=' in read_data:
#                 gsr_1 = read_data.replace('gsr=', '')
#                 gsr_1 = gsr_1.replace('\r', '')
#                 gsr_1 = gsr_1.replace('\n', '')
#                 gsr_1 = int(gsr_1)
#                 if gsr_1 < 600:
#                     dic['gsr'] = gsr_1
#
#             if 'hrt=' in read_data:
#                 hrt_1 = read_data.replace('hrt=', '')
#                 hrt_1 = hrt_1.replace('\r', '')
#                 hrt_1 = hrt_1.replace('\n', '')
#                 hrt_1 = int(hrt_1)
#                 dic['hrt'] = hrt_1
#
#             if 'gsr' in dic.keys() and 'hrt' in dic.keys():
#                 return dic
#             else:
#                 time.sleep(10)


# print(tttt())