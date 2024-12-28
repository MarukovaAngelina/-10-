# задача 1
# a = input('Игрок 1, Камень, Ножницы или Бумага?')
# b = input('Игрок 2, Камень, Ножницы или Бумага?')

# def game(a,b):
#     if (a == 'Ножницы' and b == 'Бумага') or (a == 'Бумага' and b == 'Камень') or (a == 'Камень' and b == 'Ножницы'):
#         print('Игрок 1 выиграл!')
#     elif (b == 'Ножницы' and a == 'Бумага') or (b == 'Бумага' and a == 'Камень') or (b == 'Камень' and a == 'Ножницы'):
#         print('Игрок 2 выиграл!')
#     elif a == b:
#         print('Ничья!')
#     else:
#         print('Введите корректный знак')

# print(game(a,b))



# Задача 2
# money = [23, 44, 13, 53, 15]

# def cou(money):
#     summa = sum(money)
#     return summa % 3 == 0
# res = cou(money)
# if res:
#     print('Можно')
# else:
#     print('Нельзя')


# Задача 3
# def correct(s):
#     word = ''
#     pun = ''
#     punfind = False
#     for i in range(len(s) - 1, -1, -1):
#         if s[i] == '!' and not punfind:
#             pun = '!'
#             punfind = True

#         elif s[i] == '?' and not punfind:
#             pun = '?'
#             punfind = True

#         elif s[i] != '!' and s[i] != '?':
#             word += s[i]

#     word = word[::-1] + pun
#     return word

# print(correct("Не кричи!"))


# Задача 4
# cards = [4, 3, 0, 9, 8]

# def carder(cards):
#     summ = sum(cards)
#     return summ > 21

# print(carder(cards))


# Задача 5
# str = 'вбполцыол'

# def summa(s):
#     tot = 0
#     num = ''
#     for i in s:
#         if i.isdigit():
#             num += i
#         else:
#             if num:
#                 tot += int(num)
#                 num = ''
#     if num:
#         tot += int(num)
#     return tot
# print(summa(str))


# Задача 6
# def pluss(st):
#     for i in range(1,len(st)-1):
#         if st[i] != '+' and st[i+1] == '+' and st[i+1] == '+':
#             return True
#         else:
#             return False


# print(pluss('+2+2333+445+5786+438+ 390+'))


# Задача 7
# def convert_time(time_str):
#     if 'AM' in time_str or 'PM' in time_str:
#         time_parts = time_str[:-2].strip().split(':')
#         hours = int(time_parts[0])
#         minutes = int(time_parts[1])

#         if 'PM' in time_str and hours != 12:
#             hours += 12
#         elif 'AM' in time_str and hours == 12:
#             hours = 0

#         return f"{hours:02}:{minutes:02}"
#     else:
#         time_parts = time_str.split(':')
#         hours = int(time_parts[0])
#         minutes = int(time_parts[1])

#         period = 'AM'
#         if hours >= 12:
#             period = 'PM'
#             if hours > 12:
#                 hours -= 12

#         if hours == 0:
#             hours = 12

#         return f"{hours}:{minutes:02} {period}"

# print(convert_time("08:30 PM"))
# print(convert_time("20:30"))


# Задача 8
# def difficulter(password):
#     res = 0
#     leng = 0
#     special = 0
#     capital = 0
#     dig = 0
#     low = 0

#     for i in password:
#         if not i.isalpha() and not i.isdigit():
#             special = 1
#         if i.isupper():
#             capital = 1
#         if i.islower():
#             low = 1
#         if i.isdigit():
#             dig = 1
#     if len(password) >= 7:
#         leng = 1
#     summ = special + capital + dig + low + leng
#     return summ
# print(difficulter('3463fhgsah?><fj!@'))


# Задача 9
# def speaker(n):
#     if n < 0 or n > 999:
#         raise

#     units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
#     teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать",
#              "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
#     tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят",
#             "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
#     hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот",
#                 "шестьсот", "семьсот", "восемьсот", "девятьсот"]

#     if n == 0:
#         return "ноль"

#     result = []

#     h = n // 100
#     if h > 0:
#         result.append(hundreds[h])

#     t = (n % 100) // 10
#     u = n % 10
#     if t == 1 and u > 0:
#         result.append(teens[u])
#     else:
#         if t > 0:
#             result.append(tens[t])
#         if u > 0:
#             result.append(units[u])

#     return ' '.join(result).strip()


# print(speaker(28))
# print(speaker(99))
# print(speaker(1000))


# Задача 10
# def lucker(n):
#     n = n/2
#     n = int(n)
#     sum1 = 0
#     sum2 = 0
#     sum3 = 0
#     for i in range (0,10**n):
#         for k in range (0,10**n):
#             i = str (i)
#             k = str (k)
#             for num in i:
#                 sum2 += int(num)
#             for num in k:
#                 sum3 += int(num)
#             if sum3 == sum3:
#                 sum1 += 1
#             sum2 = 0
#             sum3 = 0

#     return sum1

# print(lucker(1))