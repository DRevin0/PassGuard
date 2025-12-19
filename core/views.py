from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def check_leak(request):
    #Страница проверки утечки паролей
    result = None
    if request.method == 'POST':
        password = request.POST.get('password', '')
        #ЛОГИКА 
        is_leaked = len(password)<6
        leak_count = 0 if not is_leaked else 1

        result = {
            'password':password,
            'is_leaked':is_leaked,
            'leak_count':leak_count,
            'message': 'Пароль найден в учетчке' if is_leaked else 'Пароль безопасен',

        }
    return render(request, 'core/check_leak.html', {'result':result})