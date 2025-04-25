from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# CSV에서 데이터 읽기
df = pd.read_csv('data.csv', encoding='utf-8')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/check", methods=["POST"])
def check():
    car_number = request.form['car_number']
    
    # 차량번호를 기준으로 데이터 검색
    match = df[df['차량번호'] == car_number]
    
    if not match.empty:
        team_name = match.iloc[0]['팀명']
        participation_date = match.iloc[0]['참가일']  # 참가일 유지
        return render_template(
            'result.html',
            team_name=team_name,
            car_number=car_number,
            participation_date=participation_date
        )
    else:
        return render_template('error.html')  # 일치하는 차량 없을 때

if __name__ == '__main__':
    app.run(debug=True, port=5050)
