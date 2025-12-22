from django.shortcuts import render
from .password_checker import check_password_leak
from .password_analyser import check_password_strength
from .password_generator import generate_password

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

def generate_password_view(request):
    """
    Страница генерации паролей
    """
    generated_password = ""
    length = 12
    use_digits = True
    use_special = True
    use_uppercase = True
    use_lowercase = True
    
    if request.method == 'POST':
        try:
            length = int(request.POST.get('length', 12))

            use_digits = 'use_digits' in request.POST
            use_special = 'use_special' in request.POST
            use_uppercase = 'use_uppercase' in request.POST
            use_lowercase = 'use_lowercase' in request.POST
            
            # Генерируем пароль
            generated_password = generate_password(
                length=length,
                use_digits=use_digits,
                use_special=use_special,
                use_uppercase=use_uppercase,
                use_lowercase=use_lowercase
            )
        except ValueError as e:
            generated_password = f"Ошибка: {e}"
        except Exception as e:
            generated_password = f"Ошибка при генерации: {str(e)}"
    
    # Контекст для передачи в шаблон
    context = {
        'generated_password': generated_password,
        'default_length': length,
        'use_digits': use_digits,
        'use_special': use_special,
        'use_uppercase': use_uppercase,
        'use_lowercase': use_lowercase,
    }
    
    return render (request, 'core/password_generator.html', context)
