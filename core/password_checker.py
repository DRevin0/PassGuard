def check_password_leak(password: str) -> dict:
    is_leaked = len(password) < 8  # Пример логики
    leak_count = 0 if not is_leaked else 1
    
    return {
        'is_leaked': is_leaked,
        'leak_count': leak_count,
        'message': 'Пароль найден в утечках' if is_leaked else 'Пароль безопасен',
    }


def hash_password(password: str, algorithm: str = 'sha1') -> str:
    import hashlib
    
    if algorithm == 'sha1':
        hashed = hashlib.sha1(password.encode('utf-8')).hexdigest()
    elif algorithm == 'sha256':
        hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")
    
    return hashed.upper()

# def check_hibp_api(password_hash: str) -> bool:
#     """Проверка через HaveIBeenPwned API"""
#     pass
# 
# def load_local_database() -> set:
#     """Загрузка локальной базы утечек"""
#     pass
# 
# def check_local_database(password_hash: str, database: set) -> bool:
#     """Проверка по локальной базе"""
#     pass