# Напишите функцию, удаляющую из списка целых
# некоторое заданное число. 
# Из функции нужно вернуть
# количество удаленных элементов.
from myrandom import rand_number, randint

def delete_elem(list_num, num):
    '''Return delete elements from given list'''
    del_num = 0
    i = 0
    while i < len(list_num):
        if list_num[i] == num:
            del list_num[i]
            del_num += 1
        else:
            i += 1
    return del_num

list_of_num = rand_number(max_num=5, list_len=5)
num_to_del = randint(1, 5)
print('Delete', num_to_del, 'from list', *list_of_num)
print('Number of deleted elements =', delete_elem(list_of_num, num_to_del))
print('New list', *list_of_num)