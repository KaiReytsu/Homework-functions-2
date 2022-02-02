# Напишите функцию, определяющую 
# количество простых чисел в списке целых. 
# Список передаётся в качестве параметра. 
# Полученный результат возвращается из функции.
from random import randint
from re import X

def rand_number(list_len = 20, min_num = 1, max_num = 50):
    '''Return random list with numbers'''
    list_num = []
    step = 0
    while step < list_len:
        rand_num = randint(min_num, max_num)
        list_num.append(rand_num)
        step += 1
    return list_num

def prime_numbers(list_num):
    '''Return prime numbers of the list'''
    prime_list = []
    start_seq = 2
    for num in list_num:
        if all(num % seq != 0 for seq in range(start_seq, num)):
            prime_list.append(num)
    return prime_list

list_of_numbers = rand_number()
print('Prime numbers in list:', *list_of_numbers)
print('is', *prime_numbers(list_of_numbers))