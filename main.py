from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Портфолио')

@app.route('/works')
def works():
    return render_template('works.html', title='Прогноз погоды', year_app='июль 2023')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
