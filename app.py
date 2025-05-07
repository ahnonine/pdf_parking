from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('data.csv', encoding='utf-8')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    car_number = request.form['car_number'].strip()

    # ✅ 특정 차량번호 입력 시 별도 페이지로 이동
    if car_number == '05저7845':
        return render_template('special.html', car_number=05저784)

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
