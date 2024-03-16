def prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    else:
        for x in range(2, int(n**0.5) + 1): #square root of n
            if n % x == 0:
                return False
        return True

normal_numbers = list(range(1, 101))
#print("Original list:", normal_numbers)

prime_numbers = list(filter(prime, normal_numbers))
print("Prime numbers:", prime_numbers)
