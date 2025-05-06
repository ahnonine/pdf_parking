from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# CSV에서 데이터 읽기
df = pd.read_csv('data.csv', encoding='utf-8')

# 홈 화면
@app.route('/')
def index():
    return render_template('index.html')

# 차량번호 확인
@app.route("/check", methods=["POST"])
def check():
    car_number = request.form['car_number']
    
    # 차량번호를 기준으로 데이터 검색
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
        return render_template('error.html')  # 일치 차량 없음

# 🔽 추가된 라우트들

# 파워풀퍼레이드 (토)
@app.route('/schedule/sat')
def schedule_sat():
    return render_template('schedule_sat.html')

# 파워풀퍼레이드 (일)
@app.route('/schedule/sun')
def schedule_sun():
    return render_template('schedule_sun.html')

# 원더풀퍼레이드
@app.route('/schedule/wonderful')
def schedule_wonderful():
    return render_template('schedule_wonderful.html')

# 주차 및 하역장소
@app.route('/parking')
def parking():
    return render_template('parking.html')

# 서버 실행
if __name__ == '__main__':
    app.run(debug=True, port=5050)
