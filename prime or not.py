
def is_prime(n):
    if n<=1 :
        return False
    elif n<=3 :
        return True
    else :
        for i in range(2,int(n**.5)+1) :
            if n%i == 0 :
                return False
        return True
print(is_prime(int(input('Enter number: '))))

"""
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

print(is_prime(4))  # False
print(is_prime(5))  # True
"""