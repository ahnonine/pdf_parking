from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# 예시 데이터 (CSV 대신 사용할 수 있음)
data = [
    {"차량번호": "1234", "이름": "홍길동", "팀명": "팀 A"},
    {"차량번호": "5678", "이름": "김철수", "팀명": "팀 B"}
]
df = pd.read_csv("data.csv", encoding="euc-kr") 

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/check", methods=["POST"])
def check():
    car_number = request.form['car_number']
    
    # 차량번호를 기준으로 데이터 검색
    match = df[df['차량번호'] == car_number]
    
    if not match.empty:
        user_name = match.iloc[0]['이름']
        team_name = match.iloc[0]['팀명']
        return render_template('result.html', user_name=user_name, team_name=team_name, car_number=car_number)
    else:
        return "등록된 차량번호가 없습니다. 다시 시도해주세요."

if __name__ == '__main__':
    app.run(debug=True, port=5050)