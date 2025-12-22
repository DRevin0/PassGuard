import random
import string

def generate_password(length=12, use_digits=True, use_special=True, 
                     use_uppercase=True, use_lowercase=True):
    """
    Генерирует безопасный пароль на основе выбранных критериев.
    Гарантирует наличие как минимум одного символа из каждого выбранного набора.
    
    Параметры:
    - length: длина пароля (по умолчанию 12)
    - use_digits: включать цифры (по умолчанию True)
    - use_special: включать специальные символы (по умолчанию True)
    - use_uppercase: включать заглавные буквы (по умолчанию True)
    - use_lowercase: включать строчные буквы (по умолчанию True)
    
    Возвращает:
    - Сгенерированный пароль (str)
    """
    # 1. Создаем пулы символов
    lowercase = string.ascii_lowercase if use_lowercase else ''
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?" if use_special else ''
    
    # Объединяем все выбранные пулы
    all_chars = lowercase + uppercase + digits + special
    
    # Проверка, что выбран хотя бы один тип символов
    if not all_chars:
        raise ValueError("Необходимо выбрать хотя бы один тип символов.")
    
    # 2. Гарантируем присутствие выбранных типов
    password_parts = []
    if use_lowercase:
        password_parts.append(random.choice(lowercase))
    if use_uppercase:
        password_parts.append(random.choice(uppercase))
    if use_digits:
        password_parts.append(random.choice(digits))
    if use_special:
        password_parts.append(random.choice(special))
    
    # 3. Добиваем пароль до нужной длины случайными символами из всех пулов
    while len(password_parts) < length:
        password_parts.append(random.choice(all_chars))
    
    # 4. Перемешиваем символы, чтобы гарантированные не стояли в начале
    random.shuffle(password_parts)
    
    # 5. Возвращаем итоговый пароль
    return ''.join(password_parts)


# Дополнительная функция для генерации нескольких паролей
def generate_multiple_passwords(count=5, **kwargs):
    """
    Генерирует несколько паролей с одинаковыми настройками.
    
    Параметры:
    - count: количество паролей для генерации
    - **kwargs: параметры для generate_password()
    
    Возвращает:
    - Список сгенерированных паролей
    """
    return [generate_password(**kwargs) for _ in range(count)]
