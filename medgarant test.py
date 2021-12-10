"""
import numpy as np

numbers = list(np.random.randint(low = 1, high = 10, size = 100000))
for i, number in enumerate(numbers):
    number_is_in_tail = number in numbers[i+1:]

Надо придумать быстрый способ и проверить, что он действительно лучше.
"""


import timeit


"""
Исходный алгоритм
"""

code_to_test_1 = """
import numpy as np
numbers = list(np.random.randint(low = 1, high = 10, size = 10000))
for i, number in enumerate(numbers):
    number_is_in_tail = number in numbers[i+1:]
"""

elapsed_time_1 = timeit.timeit(code_to_test_1, number=100)/100
print(elapsed_time_1)


"""
Алгоритм со словарём, два прохода списка.
"""

code_to_test_2 = """
import numpy as np
numbers = list(np.random.randint(low = 1, high = 10, size = 10000))
dict_numbers = {}
for number in range(1, 11):
    dict_numbers[number] = 0
for i, number in enumerate(numbers):
    dict_numbers[number] += 1
for i, number in enumerate(numbers):
    dict_numbers[number] -= 1
    if dict_numbers[number] > 0:
        number_is_in_tail = True
    else:
        number_is_in_tail = False
"""
elapsed_time_2 = timeit.timeit(code_to_test_2, number=100)/100
print(elapsed_time_2, 'Faster then first in - ', elapsed_time_1 / elapsed_time_2)


"""
Алгоритм со словарём, с одним проходом списка, стеком со значениями.
"""

code_to_test_3 = """
import numpy as np
numbers = list(np.random.randint(low = 1, high = 10, size = 10000))

dict_numbers = {}

for number in range(1, 11):
    dict_numbers[number] = 0

stek_number_is_in_tail = [[] for i in range(len(numbers))]

for i, number in enumerate(numbers[::-1]):
    if dict_numbers[number] == True:
        stek_number_is_in_tail[len(numbers)-1 - i] = True
    else:
        stek_number_is_in_tail[len(numbers)-1 - i] = False
        dict_numbers[number] = True
"""

elapsed_time_3 = timeit.timeit(code_to_test_3, number=100)/100
print(elapsed_time_3, 'Faster then first in - ', elapsed_time_1 / elapsed_time_3)