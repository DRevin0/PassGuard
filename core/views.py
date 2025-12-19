from django.shortcuts import render
from .password_checker import check_password_leak

def home(request):
    return render(request, 'core/home.html')

def check_leak(request):
    #Страница проверки утечки паролей
    result = None
    if request.method == 'POST':
        password = request.POST.get('password', '')
        check_result = check_password_leak(password)

        result = {
            'password':password[:2]+'*******'+password[-2:] if password else '',
            'is_leaked':check_result['is_leaked'],
            'leak_count':check_result['leak_count'],
            'message': check_result['message'],

        }
    return render(request, 'core/check_leak.html', {'result':result})