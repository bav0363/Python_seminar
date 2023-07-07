# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.


import random
from random import  randint

print(list_1 := [random.randint(0, 10) for _ in range(int(input("Введите размер первого списка: ")))])
print(list_2 := [random.randint(0, 10) for _ in range(int(input("Введите размер второго списка: ")))])

set_list_1 = set(list_1)
set_list_2 = set(list_2)
result_set = set_list_1.intersection(set_list_2)
result_list = list(result_set)
result_list.sort()
print(f"Пересекающиеся числа без повторений в порядке возрастания: {result_list}")
