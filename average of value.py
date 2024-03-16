def avg(lst) :
    s=n=0
    for i in lst:
        s+=i
        n+=1
    return s/n
        
dic1 = {
    'Math' : [90,85,88,92,95],
    'Physics' : [75,80,85,90,95],
    'Chemistry' : [85,90,92,88,82]
}
dic2 = {}
for i, j in dic1.items() :
    dic2[i] = avg(j)
print(dic2)