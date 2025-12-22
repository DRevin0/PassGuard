import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    """
    Генератор случайных паролей
    
    Параметры:
    - length: длина пароля (по умолчанию 12)
    - use_digits: включать цифры (по умолчанию True)
    - use_special_chars: включать специальные символы (по умолчанию True)
    
    Возвращает:
    - Сгенерированный пароль
    """
    
    # Базовый набор символов (буквы)
    characters = string.ascii_letters
    
    # Добавляем цифры если нужно
    if use_digits:
        characters += string.digits
    
    # Добавляем специальные символы если нужно
    if use_special_chars:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Проверяем, что есть хотя бы один набор символов
    if not characters:
        raise ValueError("Должен быть выбран хотя бы один тип символов")
    
    # Генерируем пароль
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Дополнительная проверка для гарантии сложности
    if use_digits and not any(char.isdigit() for char in password):
        # Если нужны цифры, но их нет - добавляем одну
        password_list = list(password)
        password_list[random.randint(0, length-1)] = random.choice(string.digits)
        password = ''.join(password_list)
    
    if use_special_chars and not any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in password):
        # Если нужны спецсимволы, но их нет - добавляем один
        password_list = list(password)
        password_list[random.randint(0, length-1)] = random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?")
        password = ''.join(password_list)
    
    return password

def generate_multiple_passwords(count=5, length=12, use_digits=True, use_special_chars=True):
    """
    Генерация нескольких паролей
    """
    return [generate_password(length, use_digits, use_special_chars) for _ in range(count)]

# Пример использования:
if __name__ == "__main__":
    print("Примеры паролей:")
    print("-" * 30)
    
    # Простой пароль (только буквы)
    print("1. Только буквы:", generate_password(10, use_digits=False, use_special_chars=False))
    
    # Пароль средней сложности (буквы + цифры)
    print("2. Буквы + цифры:", generate_password(12, use_digits=True, use_special_chars=False))
    
    # Сложный пароль (все символы)
    print("3. Все символы:", generate_password(14, use_digits=True, use_special_chars=True))
    
    print("\nНесколько паролей:")
    for i, pwd in enumerate(generate_multiple_passwords(3), 1):
        print(f"{i}. {pwd}")
