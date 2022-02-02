# Напишите функцию, вычисляющую 
# произведение элементов списка целых чисел. 
# Список передаётся в качестве параметра. 
# Полученный результат возвращается из функции.
from myrandom import rand_number

def product_of_numbers(list_num):
    '''Returns product of the numbers in a given list '''
    mult = 1
    for num in list_num:
        mult = mult * num
    return mult

list_of_num = rand_number(5, 1, 15)
print('List of numbers:', *list_of_num)
print('Product of numbers in list =', product_of_numbers(list_of_num))