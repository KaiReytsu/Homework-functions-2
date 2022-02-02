# Напишите функцию, высчитывающую 
# степень каждого элемента списка целых. 
# Значение для степени передаётся в качестве параметра, 
# список тоже передаётся в качестве параметра. 
# Функция возвращает новый список, содержащий полученные результаты.
from myrandom import rand_number

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


