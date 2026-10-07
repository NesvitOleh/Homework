#Завдання 3.3
# Розділити один список на два списки

lst = [1, 2, 3, 4, 5, 6]
mid = (len(lst) + 1) // 2
lst_1 = lst[:mid]
lst_2 = lst[mid:]
print(lst_1, lst_2)
