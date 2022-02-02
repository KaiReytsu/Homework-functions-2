#Функция для создания рандомных чисел,
#возвращающая список чисел.
#Создана для решения задач, в которых 
# в функции поступают случайные списки с целыми числами
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