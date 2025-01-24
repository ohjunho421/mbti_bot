import os
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from json import JSONDecodeError
from openai import OpenAI
from .models import ChatHistory
from .forms import UserRegistrationForm

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('chat')  # chat view로 리다이렉트
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    chat_history = ChatHistory.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'profile.html', {'history': chat_history})

@login_required
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

            ChatHistory.objects.create(
                user=request.user,
                question=user_input,
                answer=ai_response
            )


            return JsonResponse({'message': ai_response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return render(request, 'chat.html', {'initial_message': initial_message})