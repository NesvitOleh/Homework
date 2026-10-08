# Завдання 4.1
lst = [0, 1, 0, 12, 3]
pos = 0
for i in range(len(lst)):
    if lst [i] != 0:
       lst [pos] = lst[i]
       pos += 1
for i in range(pos, len(lst)):
    lst [i] = 0

print(lst)