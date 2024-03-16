lst = list(range(40,61))
for i in lst :
    if i%2 == 0:
        lst[lst.index(i)] = i+5
    elif i%5 == 0:
        lst[lst.index(i)] = i+2
print(lst)