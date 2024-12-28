# Задача 1
# def to_dict(lst):
#     dictionary = {}
#     for name in lst:
#         dictionary[name] = name
#     return dictionary

# print(to_dict(['age','name']))

# Задача 2
# def biggest_dict(*args):
#     my_dict = {"first_one": "we can do it"}
#     for i in range(0, len(args), 2):
#         if i + 1 < len(args):
#             key = args[i]
#             value = args[i + 1]
#             my_dict[key] = value
    
#     return my_dict
# result = biggest_dict("second_one", "hello", "third_one", "world")
# print(result)

# Задача 3
# from typing import Any

# def count_it(numbers):
#     counter = {}
#     for i in range (10):
#         counter[i] = 0

#     for number in numbers:
#         counter[int(number)] += 1
#     biggest = {}
#     for i in range(3):
#         max_num = -1
#         big_key = None

#         for number in counter:
#             if int(counter[number]) > int(max_num):
#                 max_num = counter[number]
#                 big_key = number

#         biggest[big_key] = max_num
#         counter[big_key] = 0
#     return biggest

# print(count_it("1234567890"))

# Задача 4
# my_dict = {
#     'first_key': 'first_value',
#     'second_key': 'second_value',
#     'third_key': 'third_value',
#     'fourth_key': 'fourth_value',
#     'fifth_key': 'fifth_value'
# }

# print("Исходный словарь:", my_dict)

# keys = list(my_dict.keys())
# my_dict[keys[0]], my_dict[keys[-1]] = my_dict[keys[-1]], my_dict[keys[0]]
# del my_dict[keys[1]]
# my_dict['new_key'] = 'new_value'


# print("Итоговый словарь:", my_dict)