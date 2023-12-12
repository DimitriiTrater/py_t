import random
print('ПРАВИЛА ИГРЫ\nПеред вами лежит куча камней (от 1 до 100). С помощью рандомайзера вы можете выбрать: увеличить количество камней в куче, уменьшить или оставить прежним\nВам необходимо убрать все камни из кучи (довести до нуля).')
print()
pile = random.randint(1, 100)
cnt = 0
while True:
    if pile == 0:
        print(f'Игра окончена. Вы выиграли! Количество затраченных ходов: {cnt}.')
        break
    plus = random.randint(1, 50)
    minus = random.randint(1, 50)
    print(f"Сейчас в куче {pile} камней.\nВыберите свой ход: 1. Прибавить {plus}; 2. Отнять {minus}; 3. Оставить как есть; 4. Сдаться.")
    choice = int(input())
    print()
    if choice == 1:
        pile += plus
    elif choice == 2:
        pile -= minus
    elif choice == 3:
        continue
    elif choice == 4:
        print(f'Игра окончена. Вы сдались. Количество камней в куче {pile}.')
        break
    else:
        print('Ошибка! Начните сначала.')
        break
    cnt += 1
