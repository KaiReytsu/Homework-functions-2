# Напишите функцию для нахождения 
# минимума в списке целых. 
# Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.
from random import randint

def minimum_number(num_list):
    '''Return minimum number of list'''
    min_num = []
    min_num.append(num_list[0])
    for elem in num_list:
        if elem < min_num[0]:
            min_num.clear()
            min_num.append(elem)
    return min_num

def rand_number(list_len = 10, min_num = 1, max_num = 50):
    '''Return random list with numbers'''
    list_num = []
    step = 0
    while step < list_len:
        rand_num = randint(min_num, max_num)
        list_num.append(rand_num)
        step += 1
    return list_num


list_of_num = rand_number(min_num = 15, max_num = 100)
print('Minimum number in list:', *list_of_num, '\nis', *minimum_number(list_of_num))