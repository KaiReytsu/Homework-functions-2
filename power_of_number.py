# Напишите функцию, высчитывающую 
# степень каждого элемента списка целых. 
# Значение для степени передаётся в качестве параметра, 
# список тоже передаётся в качестве параметра. 
# Функция возвращает новый список, содержащий полученные результаты.
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

def power_of_number(list_num, power = 2):
    '''Return given power of numbers in a given list'''
    res_list = []
    for elem in list_num:
        res_num = elem ** power
        res_list.append(res_num)
    return res_list

list_of_num = rand_number(list_len = 3, max_num = 5)
print('Power of numbers in list:', *list_of_num)
print('is', *power_of_number(list_of_num, 3))


