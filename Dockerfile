# 1. 파이썬 3.10 이미지 기반으로 시작
FROM python:3.10-slim

# 2. 작업 디렉토리 설정 (컨테이너 내부)
WORKDIR /app

# 3. 로컬의 requirements.txt 파일을 컨테이너로 복사
COPY requirements.txt .

# 4. 필요한 파이썬 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 5. 모든 프로젝트 파일을 컨테이너에 복사
COPY . .

# 6. 포트 열기 (Django는 8000 포트를 사용)
EXPOSE 8000

# 7. 서버 실행 명령
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]