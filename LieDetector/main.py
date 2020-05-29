from flask import Flask, render_template

app = Flask(__name__)

############페이지############
@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/main')
def main_page():
    return render_template('main.html')

#############################













if __name__ == '__main__':
    app.run()


