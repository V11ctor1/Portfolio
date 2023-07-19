from flask import Flask, redirect
from flask import render_template, request
import requests
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Портфолио')


@app.errorhandler(404)
def http_404_error(error):
    return redirect('/error404')


@app.route('/error404')
def well():  # колодец
    return render_template('well.html', title='Вот это поворот 404', year_app='Никогда')


@app.route('/works')
def works():
    return render_template('works.html', title='Прогноз погоды', year_app='июль 2023')


@app.route('/weather_form', methods=['GET', 'POST'])
def weather_form():
    if request.method == 'GET':
            return render_template('weather_form.html', title="Погода", year_app='июль 2023')
    elif request.method == 'POST':
        town = request.form.get('town')
        key = '6d1cbcd7f1f15faea7b3accc84da2c51'
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': key, 'q': town, 'units': 'metric'}
        result = requests.get(url, params=params)
        weather = result.json()  # превратить ответ в формат json
        code = weather['cod']  # если города нет, поймать ошибку
        icon = weather['weather'][0]['icon']
        temp = int(weather['main']['temp'])
        vlag = weather['main']['humidity']
        text = weather['weather'][0]['description']
        return render_template('weather.html', title='Погода', year_app='июль 2023',
                               town=town, data=weather, icon=icon, temp=temp, vlag=vlag, text=text)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
