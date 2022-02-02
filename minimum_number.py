# Напишите функцию для нахождения 
# минимума в списке целых. 
# Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.
from myrandom import rand_number

def minimum_number(num_list):
    '''Return minimum number of list'''
    min_num = 0
    min_num = num_list[0]
    for elem in num_list:
        if elem < min_num:
            min_num = elem
    return min_num


list_of_num = rand_number(min_num = 15, max_num = 100)
print('Minimum number in list:', *list_of_num, '\nis', minimum_number(list_of_num))