from flask import Flask, render_template, request
import random
import json
import hashlib
from datetime import datetime
from DB import conn

app = Flask(__name__)


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
    dic = {}
    dic["gsr"] = random.randint(1, 100)
    dic["hrt"] = random.randint(1, 100)
    data = json.dumps(dic)
    return data

@app.route('/sil')
def sil_page():
    return render_template('silhum.html')


@app.route('/savedata', methods=['POST'])
def save_data():
    now = datetime.now()
    nowtime = str("%s%s%s%s%s%s" % (now.year, now.month, now.day, now.hour, now.minute, now.microsecond))
    encoded_data = nowtime.encode()
    before = hashlib.sha256(encoded_data).hexdigest()
    if len(before) > 65 :
        id = before[0:65]
    else :
        id = before


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













if __name__ == '__main__':
    app.run(debug=True)


