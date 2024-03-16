sum=0
n = int(input("Enter the number of test case: "))
for i in range(0,n):
    x,y = map(int,input('Enter the values of x and y: ').split())
    for i in range(x,(x+(y*2))):
        if i%2 != 0 :
            sum += i
    print(sum)