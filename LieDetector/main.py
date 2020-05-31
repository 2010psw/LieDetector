from flask import Flask, render_template
import random
import json




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

@app.route('/result')
def result_page():
    return render_template('result.html')

@app.route('/request_data', methods=['POST'])
def send_data():
    dic = {}
    dic["gsr"] = random.randint(1, 10)
    dic["hrt"] = random.randint(1, 10)
    data = json.dumps(dic)
    return data

#############################













if __name__ == '__main__':
    app.run(debug=True)


