while True:
    n = input('Введите число:')
    if n.isdigit():
        print(f'Введено целое число {n}')
        break
    print('Ошибка. Попробуйте еще раз')