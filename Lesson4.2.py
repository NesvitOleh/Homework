# Завдання 4.2
lst = [0, 1, 7, 2, 4, 8]
if len(lst) == 0:
    result = 0
else:
    total = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            total += lst[i]
    result = total * lst[-1]
print(result)
