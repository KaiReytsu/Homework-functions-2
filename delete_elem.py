# Напишите функцию, удаляющую из списка целых
# некоторое заданное число. 
# Из функции нужно вернуть
# количество удаленных элементов.
from myrandom import rand_number, randint

def delete_elem(list_num, num):
    '''Return delete elements from given list'''
    del_num = 0
    for index, elem in enumerate(list_num):
        if elem == num:
            del list_num[index]
            del_num += 1
    return del_num

list_of_num = rand_number(max_num=10, list_len=10)
num_to_del = randint(1, 10)
print('Delete', num_to_del, 'from list', *list_of_num)
print('Number of deleted elements =', delete_elem(list_of_num, num_to_del))
print('New list', *list_of_num)