from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('data.csv', encoding='utf-8')

@app.route('/parking')
def parking():
    return render_template('parking.html')

@app.route('/schedule/sat')
def schedule_sat():
    return render_template('schedule_sat.html')

@app.route('/schedule/sun')
def schedule_sun():
    return render_template('schedule_sun.html')

@app.route('/schedule/wonderful')
def schedule_wonderful():
    return render_template('schedule_wonderful.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    car_number = request.form['car_number'].strip().replace(' ', '').upper()


    # 특정 차량번호에 대한 처리
    if car_number == '05저7845':
        team_name = '학습능력이 뛰어나고 발표를 잘하나 잘난 척하는 경향이 있는 소년'
        participation_date = '5월 11일(일)'
        return render_template(
            'special.html',
            team_name=team_name,
            car_number=car_number,
            participation_date=participation_date
        )

    match = df[df['차량번호'] == car_number]

    if not match.empty:
        team_name = match.iloc[0]['팀명']
        participation_date = match.iloc[0]['참가일']
        return render_template(
            'result.html',
            team_name=team_name,
            car_number=car_number,
            participation_date=participation_date
        )
    else:
        return render_template('error.html')
