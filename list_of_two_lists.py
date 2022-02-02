# Напишите функцию, которая получает два списка в
# качестве параметра и 
# возвращает список, содержащий
# элементы обоих списков.
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

def two_lists(list_one, list_two):
    '''Return list of two lists'''
    return list_one + list_two

list_one = rand_number(list_len = 5)
list_two = rand_number(list_len = 5)

print('List one =', *list_one)
print('List two =', *list_two)
print('List of two lists =', *two_lists(list_one, list_two))
