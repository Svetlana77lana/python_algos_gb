"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

import time


def create_list(elem_number):
    start_val = time.time()
    my_list = [i for i in range(elem_number)]
    end_val = time.time()
    return my_list, end_val - start_val


def create_dict(elem_number):
    start_val = time.time()
    my_dict = {i:i for i in range(elem_number)}
    end_val = time.time()
    return my_dict, end_val - start_val


# elem_number = 19000
elem_number = 98000

print(f'Операция по заполнению 	СПИСКА длиной {elem_number} заняла {create_list(elem_number)[1]} сек')
print(f'Операция по заполнению СЛОВАРЯ длиной {elem_number} заняла {create_dict(elem_number)[1]} сек\n')
elem_number = 200100
print(f'Операция по заполнению 	СПИСКА длиной {elem_number} заняла {create_list(elem_number)[1]} сек')
print(f'Операция по заполнению СЛОВАРЯ длиной {elem_number} заняла {create_dict(elem_number)[1]} сек\n')
elem_number = 2100100

print(f'Операция по заполнению 	СПИСКА длиной {elem_number} заняла {create_list(elem_number)[1]} сек')
print(f'Операция по заполнению СЛОВАРЯ длиной {elem_number} заняла {create_dict(elem_number)[1]} сек\n')

'''
при колличестве элементов в 98000, elem_number=98000
Операция по заполнению списка длиной 98000 заняла 0.005000114440917969 сек
Операция по заполнению словаря длиной 98000 заняла 0.010000228881835938 сек

Вывод: словарь генерируется дальше, примерно в два раза, посколько длина списки и словаря одинкаовая, но у 
словаря один элемент содержит и ключ и значение - те два элемента
'''
