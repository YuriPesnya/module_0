# Доработанный алгоритм с бинариным поиском

import numpy as np


def game_core_v3(number):
    '''Сначала устанавливаем любое random число, а потом пролводим бинарный поиск '''
    count = 0
    predict = 50 #начинаем всегда с середины диапазона
    min_number = 0
    max_number  = 101 #чтобы угадывать 100 и 0 - берем диапазон 0-101
    while number != predict:
        count+=1
        if number > predict:
            min_number = predict # устванавлмваем новую нижнюю границу поиска
            predict = ( max_number - predict ) // 2 + predict # следуююее предположение  - середина нового диапазона
        elif number < predict:
            max_number = predict # устванавлмваем новую верхнюю границу поиска
            predict = ( predict -  min_number) // 2 + min_number # следуююее предположение  - середина нового диапазона
    return(count) # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))

    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
score_game(game_core_v3)

