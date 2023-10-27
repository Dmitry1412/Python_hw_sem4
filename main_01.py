# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

# На входе:
# var1 = '5 4' # количество элементов первого и второго множества
# var2 = '1 3 5 7 9' # элементы первого множества через пробел
# var3 = '2 3 4 5' # элементы второго множества через пробел
# На выходе:
# 3 5


### Блок создания случайных чисел ###
# import random

# def create_list(len_list):
#     result_list = list()
#     for i in range(0, len_list):
#         result_list.append(random.randint(0, 10))
#     return result_list
### Блок создания случайных чисел ### 

# list1 = create_list(list_len[0]) - создание тестового списка 1
# list2 = create_list(list_len[1]) - создание тестового списка 2

#list_len = list(map(int, input("Введите 2 числа через пробел: ").split())) #Преобразование строки в список чисел
var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5'


nums1 = list(map(int, var2.split()))
nums2 = list(map(int, var3.split()))    

def sort_nums(nums1, nums2):
    result_list = list()
    for i in range(0, len(nums1)):
        for j in range(0, len(nums2)):
            if nums1[i] == nums2[j]:
                result_list.append(nums1[i])
    result_list = list(set(result_list))
    result_list.sort()
    return result_list

user_list = (sort_nums(nums1,nums2))
print(*user_list)