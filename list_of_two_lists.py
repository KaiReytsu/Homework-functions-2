# Напишите функцию, которая получает два списка в
# качестве параметра и 
# возвращает список, содержащий
# элементы обоих списков.
from myrandom import rand_number

def two_lists(list_one, list_two):
    '''Return list of two lists'''
    return list(set(list_one + list_two))

list_one = rand_number(list_len = 5, max_num=10)
list_two = rand_number(list_len = 5, max_num=10)

print('List one =', *list_one)
print('List two =', *list_two)
print('List of two lists =', *two_lists(list_one, list_two))
