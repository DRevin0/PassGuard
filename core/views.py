from django.shortcuts import render
from .password_checker import check_password_leak
from .password_analyser import check_password_strength

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

def check_strength(request):
    #Страница анализа сложности пароля
    context = {}
    if request.method == 'POST':
        password = request.POST.get('password', '')
        if password:
            result = check_password_strength(password)
            context['result'] = result

    return render(request, 'core/check_strength.html', context)