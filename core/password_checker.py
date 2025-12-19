import hashlib
import requests
from typing import Optional
def check_password_hibp(password: str) -> dict:
    #Проверка утечки через HIBP API, возрвратит количество утечек или None при ошибке
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]

    try:
        response = requests.get(
            f"https://api.pwnedpasswords.com/range/{prefix}",
            headers={'User-Agent': 'PassGuard-Django-App'},
            timeout=10,
            stream=True  
        )
        
        if response.status_code == 200:
            found_count = 0
            for line in response.iter_lines(decode_unicode=True):
                if line:
                    hash_suffix, count = line.split(':')
                    if hash_suffix == suffix:
                        return int(count)
            return 0
        else:
            response.raise_for_status()

        lines = response.text.splitlines()

        for line in lines:
            hash_suffix, count = line.split(':')
            if hash_suffix == suffix:
                return int(count)
        return 0
    except requests.RequestException:
        return None
    
def check_password_leak(password: str) -> dict:
    result = check_password_hibp(password)
    
    if result is None:
        return {
            'is_leaked': False,
            'leak_count': 0,
            'message': 'Сервис проверки временно недоступен. Попробуйте позже.',
        }
    elif result > 0:
        return {
            'is_leaked': True,
            'leak_count': result,
            'message': f'Пароль найден в {result} утечках! Срочно замените его.',
        }
    else:
        return {
            'is_leaked': False,
            'leak_count': 0,
            'message':'Пароль не найден в известных утечках.',
        }

