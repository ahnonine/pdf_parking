import qrcode

# URL 설정
url = 'https://27de-125-137-234-75.ngrok-free.app'

# QR 코드 생성
qr = qrcode.QRCode(
    version=1,  # QR 코드 버전
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 오류 수정 레벨
    box_size=10,  # 박스 크기
    border=4,  # 테두리 크기
)
qr.add_data(url)  # URL 데이터를 QR 코드에 추가
qr.make(fit=True)  # 최적화

# 이미지로 변환하여 파일로 저장
img = qr.make_image(fill='black', back_color='white')
img.save('qr_code_localhost.png')  # qr_code_localhost.png로 저장

# 이미지를 화면에 출력하고 싶으면 다음을 사용
img.show()
