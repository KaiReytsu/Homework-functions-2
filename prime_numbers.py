# Напишите функцию, определяющую 
# количество простых чисел в списке целых. 
# Список передаётся в качестве параметра. 
# Полученный результат возвращается из функции.
from myrandom import rand_number

def prime_numbers(list_num):
    '''Return prime numbers of the list'''
    prime_list = []
    start_seq = 2
    for num in list_num:
        if all(num % seq != 0 for seq in range(start_seq, num)):
            prime_list.append(num)
    return prime_list

list_of_numbers = rand_number(list_len=20)
print('Prime numbers in list:', *list_of_numbers)
print('is', *prime_numbers(list_of_numbers))