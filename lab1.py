## Task 1##

# count = int(input("Введите количество отображаемых элементов: "))
# counter = 0
# value_print = 1
# flag = True
# while flag:
#     for x in range(value_print):
#         print(value_print, end=" ")
#         counter += 1
#         if counter == count:
#             flag = False;
#             break;
#     value_print += 1

## Task 2##

# lst = list(map(int, input().split()))
# x = int(input())
# ln = len(lst)
# count = 0
# for i in range(ln):
#     if lst[i] == x:
#         print(i, end=" ")
#         count += 1
# if(count == 0):
#     print("Отсутствует")

## Task 3 ##
# mas = []
# main_len = -1   #переменная для проверки длины каждой строки
# first = True    #флаг для запоминания длины первой строки
# while True:
#     c = list(input().split())
#     if first:
#         first = False
#         main_len = len(c)
#     if (c[0] == "end"):
#         print("Ввод матрицы окончен")
#         break
#     if len(c) != main_len and main_len != -1:
#         print("Разные длины строк. Введите ещё раз")
#     else:
#         mas.append(c)
#
# len_i = len(mas)
# len_j = len(mas[0])
#
# arr_sum = [0] * len_i
# for i in range(len_i):
#     arr_sum[i] = [0] * len_j
#
# for i in range(len_i):
#     for j in range(len_j):
#         if i - 1 == -1:
#             gran_i1 = len_i - 1
#         else:
#             gran_i1 = i - 1
#         if i + 1 == len_i:
#             gran_i2 = 0
#         else:
#             gran_i2 = i + 1
#         if j - 1 == -1:
#             gran_j1 = len_j - 1
#         else:
#             gran_j1 = j - 1
#         if j + 1 == len_j:
#             gran_j2 = 0
#         else:
#             gran_j2 = j + 1
#
#         arr_sum[i][j] = int(mas[gran_i1][j]) + int(mas[gran_i2][j]) + int(mas[i][gran_j1]) + int(mas[i][gran_j2])
#
# for row in arr_sum:
#     print()
#     for elem in row:
#         print(elem, end=' ')

## Task 4##

# count = int(input())
# list = [0] * count
# for i in range(count):
#    list[i] = [0] * count
#
# numb = 0
# k = -1
# n =- 1
# check = count
# while True:
#     n += 1
#     k += 1
#     check = check - 1
#     start = k
#     while k <= check:
#        numb += 1
#        list[n][k] = numb
#        k += 1
#     k -= 1
#     n = start + 1
#     while n <= k:
#         numb += 1
#         list[n][k] = numb
#         n = n + 1
#     n = n - 1
#     k = k - 1
#     while k >= start:
#        numb += 1
#        list[n][k] = numb
#        k -= 1
#     n = n - 1
#     k = k + 1
#     while n > start:
#         numb += 1
#         list[n][k] = numb
#         n -= 1
#     if numb == count ** 2:
#         break
#
# for i in list:
#     print()
#     for y in i:
#         print(y, end=" ")
# count = int(input())