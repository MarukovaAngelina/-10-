# Задача 1
# def search_substr(subst, st):
#     if subst.lower() in st.lower():
#         	return 'Есть контакт!'
#     else:
#     	return 'Мимо!'
# print(search_substr('Боб', 'бОбОвЫЕ'))

# Задача 2
# def first_last(letter, st):
#     first = st.find(letter)
#     if first < 0:
#         return None, None
#     last = st.rfind(letter)
#     return first, last
# print(first_last('a', 'pro'))

# Задача 3
# def top3(st):

#     count = {}
    
#     for char in st:
#         if char != ' ':  
#             if char in count:
#                 count[char] += 1
#             else:
#                 count[char] = 1
    
#     sorted_count = sorted(count.items(), key=lambda item: item[1], reverse=True)

#     top_symbols = sorted_count[:3]

#     result = ', '.join(f'{symbol} – {count}' for symbol, count in top_symbols)
    
#     return result
# text = "Петр Григорьевич позвал на устное собеседование"
# print(top3(text))

# Задача 4

def camel(st):
    new_st = ''
    letter_counter = 0
    for index, val in enumerate(st):
        if val.isalpha():
            if letter_counter % 2 == 0:
                new_st += val.upper()
            else:
                new_st += val.lower()
            letter_counter += 1
        else:
            new_st += val
    return new_st

print(camel('Ужас! Новый ГОД ЧЕрез 3 дНЯ!!!'))