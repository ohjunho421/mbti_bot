import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(dotenv_path='main/.env')
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

print("안녕하세요! 저는 MBTI별 특성과 남녀 궁합을 알려드릴 수 있는 전문가입니다.")

with open("conversation_log.txt", "a", encoding="utf-8") as log_file:
    while True:
        user_input = input("사용자: ")
        if user_input.lower() == "exit":
            print("대화를 종료합니다.")
            break

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "안녕하세요! 저는 MBTI별 특성을 알려드릴 수 있는 전문가입니다."},
                {"role": "user", "content": user_input}
            ]
        )

        ai_response = response.choices[0].message.content
        print("AI: " + ai_response)
        log_file.write(f"사용자: {user_input}\n")
        log_file.write(f"AI: {ai_response}\n")