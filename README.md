# MBTI 챗봇 프로젝트

AI 기반 MBTI 성격유형 상담 챗봇 서비스입니다. GPT를 활용하여 MBTI 관련 질문에 답변하고, 성격 유형 분석과 궁합을 제공합니다.

## 주요 기능
- OpenAI API 기반 MBTI 전문 챗봇
- 사용자 인증 (로그인/회원가입)
- 상담 내역 저장 및 조회
- 프로필 관리

## 기술 스택
- Django
- OpenAI API
- SQLite
- jQuery

## 설치 및 실행
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

API 키는 .env 파일에 OPENAI_API_KEY로 설정해야 합니다.

## 프로젝트 구조
```
mbti_project/
├── mbti_chat/
│   ├── models.py  # 대화 기록 모델
│   ├── views.py   # 챗봇 및 인증 로직
│   └── templates/ # 프론트엔드 템플릿
└── static/        # CSS, JavaScript
```
