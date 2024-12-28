# Задача 5*
# def shortener(st):
#     stack = []
#     result = []
    
#     for char in st:
#         if char == '(':
#             stack.append(len(result))
#         elif char == ')':
#             if stack:
#                 start_index = stack.pop()
#                 result = result[:start_index]
#         else:
#             if not stack:
#                 result.append(char)
    
#     return ''.join(result)

# text = "привет (пока пропрропдырад) рваопрфопфо (раоплр(паовр))"
# print(shortener(text))

# Задача 6
# def cleaned_str(st):
#     clean_lst = []
#     for symbol in st:
#         if symbol == '@' and clean_lst:
#             clean_lst.pop()
#         elif symbol != '@':
#             clean_lst.append(symbol)
#     return ''.join(clean_lst)

# print(cleaned_str('гр@оо@лк@оц@ва'))