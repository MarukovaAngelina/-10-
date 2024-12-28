# Задача 1
# x = [28, 12, 52]
# y = [32, 90, 71]
# def pointer(x, y):
#     coord = []
#     for i in range(len(x)):
#         coord.append((x[i], y[i]))
#     return coord
# print(pointer(x, y))


# Задача 2
# guest = ['Nicola' , 'Nina', 'Natasha']
# def privet (guest):
#     for i in guest:
#         print(f'hello, {i}')
# privet(guest)


# Задача 3
# a = 'abbabbbbbbbbaaaaaaaaaaa'
# b = 'abba'
# def two (n):
#     for i in range(len(n)-1):
#         if n[i] == n[i+1]:
#             return True
#     return False
# print(two(a))
# print(two(b))


# Задача 4
# spaces = 'курочка         окрошка'
# def spacer(s):
#     res = ""
#     extra = False
#     for i in s:
#         if i != ' ':
#             res += i
#             ettra = False
#         else:
#             if not extra:
#                 res += i
#                 extra = True
#     return res.strip()
# print(spacer(spaces))

# Задача 5
# import math
# r = 33
# h = 28

# def mass(rad, hei):
#     v = math.pi * r**2 * h
#     p = 1000
#     m = v * p
#     return round(m, 2)

# m = mass(r, h)
# print(f"Масса воды: {m} кг")

# Задача 6
# def multiply_numbers(input_string):
#     numbers = [float(num.strip()) for num in input_string.split(',')]
#     product = 1
#     for number in numbers:
#         product *= number
#     return product
    
# input_string = "2.5, 3.0, 4.0"
# result = multiply_numbers(input_string)
# print(f"Произведение чисел: {result}")


# Задача 7 
# def all (box):
#     all = 0
#     for i in box:
#         a, b, h = i
#         volume = a * b * h
#         all += volume
#     return all

# sizes = [(3323, 323, 43), (37864, 566, 13), (456362, 5457, 45)]

# sum = all(sizes)
# print(sum)


# Задача 8
# import math
# Xa = 24
# Ya = 52
# Xb = 34
# Yb = 45
# def lengther():
#     Xx = (Xb - Xa)**2
#     Yy = (Yb - Ya)**2
#     leng = (Xx + Yy) ** 0.5
#     print("{:.3f}".format(leng))
# lengther()


# Задача 9
# a = 'я говорю на языке хакера '
# x = a.replace('а', '4')
# y = x.replace('е', '3')
# print(y)


# Задача 10
# def sum(number):
#     summ = []
#     res = 0
#     for i in numbers:
#         res += i
#         summ.append(res)
#     return summ
# numbers = [11, 22, 33]
# result = sum(numbers)
# print(result)

# Задача 11
# num1 = [121,31,423,23,56]
# num2 = [2341,4222,13,223]
# def up(n):
#     for i in range(1, len(n)):
#         if n[i] <= n[i-1]:
#             return 'Не возрастает'
#     return 'Возрастает'
# print(up(num1))
# print(up(num2))


# Задача 14
# a = [21, 344, 623, 12, 70, 34, 94]

# def med (n):
#     for i in range(0, len(n)):
#         for k in range(0, len(n)-1):
#             if n[k] > n[k+1]:
#                 n[k],n[k+1] = n[k+1],n[k]

#     return n[len(n)//2]
# print(med(a))



# Задача 13
# def letter(n):
#     a = 'abcdefghiklmnopqrstuvwxyz'
#     cou = 0
#     for let in n:
#         for i in range (len(a)):
#             if let == a[i]:
#                 cou += i+1
#     return cou
# print(letter('dfhhs'))


# Задача 14
# a = 'Первернул он ее перевернул'
# def swapper(st):
#     swapped = st[::-1]
#     res = swapped.swapcase()
#     return res
# print(swapper(a))


# Задача 15
# friends = ['Миша', 'Гриша', 'Паша', 'Филипп']
# enemies = ['Никита', 'Аня']

# def truefriends (friends, enemies):
#     return [friend for friend in friends if friend not in enemies]

# print(truefriends(friends, enemies))