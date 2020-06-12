from flask import Flask, render_template, request
import random
import json
import hashlib
from datetime import datetime
from DB import conn
''''#from arduino import serialTest as st'''
from multiprocessing import Pool
import time
import threading
import serial
app = Flask(__name__)



#############################################
dic = {'gsr' : 0, 'hrt' : 0}
####5050/
############페이지############
@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/main')
def main_page():
    return render_template('main.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/live')
def live_page():
    return render_template('live.html')

@app.route('/result')
def result_page():
    return render_template('result.html')

@app.route('/request_data', methods=['GET'])
def send_data():
    try:
        data = json.dumps(dic)
        return data
    except Exception as msg:
        print(msg)




@app.route('/sil')
def sil_page():
    return render_template('silhum.html')


@app.route('/savedata', methods=['POST'])
def save_data():
    now = datetime.now()
    nowtime = str("%s_%s_%s_%s_%s_%s_%s" % (now.year, now.month, now.day, now.hour, now.minute, now.second,now.microsecond))
    encoded_data = nowtime.encode()
    before = hashlib.sha256(encoded_data).hexdigest()
    # if len(before) > 65 :
    #     id = before[0:65]
    # else :
    #     id = before
    id = nowtime

    print(before)
    print(id)

    b_data = request.json
    conn.ins_id(id)
    conn.ins_gsr(id, b_data['gsr'])
    conn.ins_hrt(id, b_data['hrt'])
    if b_data['label'] == 't':
        conn.ins_lb(id, 1)
    if b_data['label'] == 'f':
        conn.ins_lb(id, 0)



    #print(type(b_data['gsr']))






    return 'good';



#############################







def thread1():
    ser = serial.Serial(
        port='COM2',
        baudrate=9600,
    )

    global dic
    while True:
        try:
            while True:
                global dic
                if ser.readable():
                    res = ser.readline()
                    data = res.decode()

                    if 'gsr' in data:
                        gsr_1 = data.replace('gsr=', '')
                        gsr_1 = gsr_1.replace('\r', '')
                        gsr_1 = gsr_1.replace('\n', '')
                        gsr_1 = int(gsr_1)
                        dic['gsr'] = gsr_1

                    if 'hrt' in data:
                        hrt_1 = data.replace('hrt=', '')
                        hrt_1 = hrt_1.replace('\r', '')
                        hrt_1 = hrt_1.replace('\n', '')
                        hrt_1 = int(hrt_1)
                        if 100 > hrt_1 > 40:
                            dic['hrt'] = hrt_1

        except Exception as msg:
            print('errrrrrrrrrrrrrrr')
            print(msg)

if __name__ == '__main__':
    threading.Thread(target=thread1).start()
    app.run()

