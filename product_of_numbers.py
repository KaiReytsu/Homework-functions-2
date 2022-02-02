# Напишите функцию, вычисляющую 
# произведение элементов списка целых чисел. 
# Список передаётся в качестве параметра. 
# Полученный результат возвращается из функции.
from random import randint

def rand_number(list_len = 10, min_num = 1, max_num = 50):
    '''Return random list with numbers'''
    list_num = []
    step = 0
    while step < list_len:
        rand_num = randint(min_num, max_num)
        list_num.append(rand_num)
        step += 1
    return list_num

def product_of_numbers(list_num):
    '''Returns product of the numbers in a given list '''
    mult = 1
    for num in list_num:
        mult = mult * num
    return mult

list_of_num = rand_number(5, 1, 15)
print('List of numbers:', *list_of_num)
print('Product of numbers in list =', product_of_numbers(list_of_num))