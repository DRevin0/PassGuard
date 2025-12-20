import re
from collections import Counter

def check_password_strength(password):
    #Анализирует сложность пароля и возвращает оценку от 0 до 10

    score = 0 # оценка пароля
    checks = []
    tips = [] # рекомендации

    # 1. Длина пароля
    length = len(password)
    if length >= 12:
        score += 3
        checks.append({
            'name': 'Длина пароля (≥12 символов)',
            'passed': True,
            'details': f'Длина: {length} символов'
        })
    elif length >= 8:
        score += 2
        checks.append({
            'name': 'Длина пароля (≥8 символов)',
            'passed': True,
            'details': f'Длина: {length} символов'
        })
    elif length >= 6:
        score += 1
        checks.append({
            'name': 'Длина пароля (≥6 символов)',
            'passed': True,
            'details': f'Длина: {length} символов (рекомендуется ≥12)'
        })
    else:
        checks.append({
            'name': 'Длина пароля (≥6 символов)',
            'passed': False,
            'details': f'Слишком короткий: {length} символов'
        })
        tips.append('Используйте пароль длиной не менее 12 символов')

    # 2. Наличие цифр
    if re.search(r'\d', password):
        score += 1
        checks.append({
            'name': 'Содержит цифры',
            'passed': True,
            'details': None
        })
    else:
        checks.append({
            'name': 'Содержит цифры',
            'passed': False,
            'details': None
        })
        tips.append('Добавьте цифры (0-9) в пароль')

    # 3. Наличие строчных букв
    if re.search(r'[a-z]', password):
        score += 1
        checks.append({
            'name': 'Содержит строчные буквы',
            'passed': True,
            'details': None
        })
    else:
        checks.append({
            'name': 'Содержит строчные буквы',
            'passed': False,
            'details': None
        })
        tips.append('Добавьте строчные буквы')

    # 4. Наличие заглавных букв
    if re.search(r'[A-Z]', password):
        score += 1
        checks.append({
            'name': 'Содержит заглавные буквы',
            'passed': True,
            'details': None
        })
    else:
        checks.append({
            'name': 'Содержит заглавные буквы',
            'passed': False,
            'details': None
        })
        tips.append('Добавьте заглавные буквы')

    # 5. Наличие спец символов
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>/?]', password):
        score += 2
        checks.append({
            'name': 'Содержит специальные символы',
            'passed': True,
            'details': None
        })
    else:
        checks.append({
            'name': 'Содержит специальные символы',
            'passed': False,
            'details': None
        })
        tips.append('Добавьте специальные символы (!@#$%^&* и т.д.)')

    # 6. Проверка на повторяющиеся символы
    char_counts = Counter(password)
    repeated_chars = sum(1 for count in char_counts.values() if count > 1)
    if repeated_chars <= len(password) * 0.3:  # не более 30% повторений
        score += 1
        checks.append({
            'name': 'Минимальное количество повторяющихся символов',
            'passed': True,
            'details': None
        })
    else:
        checks.append({
            'name': 'Минимальное количество повторяющихся символов',
            'passed': False,
            'details': 'Слишком много повторяющихся символов'
        })
        tips.append('Избегайте повторяющихся символов')

    # 7. Проверка на последовательности (123, abc и т.д.)
    sequences = ['123', '234', '345', '456', '567', '678', '789', '890',
                 'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij',
                 'qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop']
    has_sequence = any(seq in password.lower() for seq in sequences)
    if not has_sequence:
        score += 1
        checks.append({
            'name': 'Отсутствуют простые последовательности',
            'passed': True,
            'details': None
        })
    else:
        checks.append({
            'name': 'Отсутствуют простые последовательности',
            'passed': False,
            'details': 'Обнаружены простые последовательности'
        })
        tips.append('Избегайте простых последовательностей (123, abc и т.д.)')

    # Ограничиваем оценку 10 баллами
    score = min(score, 10)

    # Определяем уровень сложности
    if score <= 3:
        message = "Очень слабый пароль"
        alert_class = "danger"
        badge_class = "danger"
    elif score <= 5:
        message = "Слабый пароль"
        alert_class = "warning"
        badge_class = "warning"
    elif score <= 7:
        message = "Средний пароль"
        alert_class = "info"
        badge_class = "info"
    elif score <= 9:
        message = "Сильный пароль"
        alert_class = "success"
        badge_class = "success"
    else:
        message = "Очень сильный пароль"
        alert_class = "primary"
        badge_class = "primary"

    return {
        'score': score,
        'score_percentage': score * 10,
        'message': message,
        'alert_class': alert_class,
        'badge_class': badge_class,
        'checks': checks,
        'tips': tips[:3],
    }