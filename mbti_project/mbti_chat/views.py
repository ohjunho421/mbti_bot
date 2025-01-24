from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
import os
from json import JSONDecodeError

def chat_view(request):
    initial_message = "안녕하세요! 저는 MBTI별 특성과 남녀 궁합을 알려드릴 수 있는 전문가입니다. 궁금한 점이 있으면 언제든지 물어보세요."
    
    if request.method == 'POST':
        user_input = request.POST.get('message')
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "MBTI 전문가"},
                    {"role": "user", "content": user_input}
                ]
            )
            ai_response = response.choices[0].message.content
            return JsonResponse({'message': ai_response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return render(request, 'chat.html', {'initial_message': initial_message})