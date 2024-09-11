def power_and_multiply(num):
    # Преобразуем число в строку, чтобы легко извлечь цифры
    num_str = str(num)
    
    # Извлекаем последние три цифры
    единицы = int(num_str[-1])
    десятки = int(num_str[-2]) if len(num_str) > 1 else 0
    сотни = int(num_str[-3]) if len(num_str) > 2 else 0
    
    # Рассчитываем результат
    if десятки * 10 - единицы == 0:
        raise ValueError("Деление на ноль невозможно.")
    
    результат = (десятки ** единицы) * сотни
    результат /= (десятки * 10 - единицы)
    
    return результат

# Пример использования
num = 46275
print(power_and_multiply(num))  # Примерный вывод, зависит от значения num


# https://github.com/DrowASD/St4p2
