# Завдання 3.2
# Перемістити елемент у списку

lst = [12, 3, 4, 10]
if len(lst) > 1:
    last = lst.pop()
    lst.insert(0, last)
print(lst)