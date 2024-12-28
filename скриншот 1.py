# # Задача 1
# a= [1,2,3,4,5,6,7]
# print(a[::-1])

# Задача 2
# def change(bebe):
#     bebe[0], bebe[-1] = bebe[-1], bebe[0]
#     print(bebe)
# change([3,2,1,2])

# Задача 3
# def to_list(*a):
#     list(a)
#     print (list(a))
# to_list('ghgh',3,4,5,666)

# Задача 4
# def useless(s):
#     return (max(s)/len(s))
# print(useless([2,3,4,5,10,25]))

# Задача 5

# def list_sort(lst):
#     for i in range(len(lst) - 2):
#         if abs(lst[i]) < abs(lst[i+1]):
#             s=(lst[i])
#             lst[i]=lst[i+1]
#             lst[i+1]=s
#     return (lst)
# print(list_sort([2,3,-4,5,6,-7,8,9,-100,-52,0]))


# Задача 6

# def all_eq(lst):
#     maxx=0
#     for i in range(len(lst)):
#         if i == 0:
#                 maxx = len(lst[i])
#         if maxx < len(lst[i]):
#                 maxx = len(lst[i])
#     print(maxx)
#     for i in range(len(lst)):
#         if len(lst[i]) < maxx:    
#             s = maxx - len(lst[i])
#             lst[i]= lst[i] + "_" * s
# lst = ['крот', 'белка', 'ёжик']
# all_eq(lst)
# print(lst)


