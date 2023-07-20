from flask import Flask, redirect
from flask import render_template, request
import requests
from docxtpl import DocxTemplate

app = Flask(__name__)
posit = 'Python Developer'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Портфолио', posit=posit, about=about)

#
# @app.errorhandler(404)
# def http_404_error(error):
#     return redirect('/error404')
#
#
# @app.route('/error404')
# def well():  # колодец
#     return render_template('well.html', title='Вот это поворот 404', year_app='Никогда', b='/index')
#

@app.route('/works')
def works():
    return render_template('works.html', title='Работа', year_app='июль 2023', b='/index')


@app.route('/weather_form', methods=['GET', 'POST'])
def weather_form():
    message = ''
    if request.method == 'GET':
        return render_template('weather_form.html', title="Погода", year_app='июль 2023', b='/index')
    elif request.method == 'POST':
        town = request.form.get('town')
        if town == '':
            town = 'Санкт-Петербург'
            message = "Вы не ввели город!"
        key = '6d1cbcd7f1f15faea7b3accc84da2c51'
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': key, 'q': town, 'units': 'metric'}
        result = requests.get(url, params=params)
        weather = result.json()  # превратить ответ в формат json
        code = weather['cod']  # если города нет, поймать ошибку
        if code != '401':
            if code != '404':
                icon = weather['weather'][0]['icon']
                temp = int(weather['main']['temp'])
                vlag = weather['main']['humidity']
                text = weather['weather'][0]['description']
                return render_template('weather.html', title=f'Погода в городе {town}', year_app='июль 2023',
                                       town=town, icon=icon, temp=temp, vlag=vlag, text=text,
                                       message=message, b='/weather_form')

            else:
                return redirect('/error404')


if __name__ == '__main__':
    posit = 'Python Developer'
    about = ''' 
    Умею гуглить и разбираться в сути вещей. 
    Наше время ограничено, я хочу провести его с максимальной пользой.
    Беспощадно расставляю приоритеты.
    Умею работать в команде и быстро адаптироваться к меняющейся обстановке.
    Суть бизнеса — это построение классных продуктов, за которые пользователи готовы платить.
    Суть жизни — это жизнь, которой можно гордиться, рядом с любимыми людьми, занимаясь любимым делом.
    '''
    doc = DocxTemplate("static/doc/resume.docx")
    context = {'position': posit, 'experience_list': "t", 'skills_list': "t", 'about': about}
    doc.render(context)
    doc.save("static/doc/resume-r.docx")
    app.run(host='127.0.0.1', port=5000, debug=True)
