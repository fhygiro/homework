while True:
    try:
        a = float(input('Введите первое число: '))
        break
    except:
        print('Введите число!!!')

while True:
    try:
        b = float(input('Введите первое число: '))
        break
    except:
        print('Введите число!!!')

while True:
    sign = input('Введите знак: ')

    if sign == '+': r = a + b; break
    elif sign == '-': r = a - b; break
    elif sign == '*': r = a * b; break
    elif sign == '/': r = a / b; break
    else: print('Введите знак (+, -, *, /)!!!')

print(f'Результат: {r}')