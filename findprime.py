def prime(n):
    for i in range(2,(n//2)+1):
        if n % i ==0:
            return False
    return True
print([i for i in [2,3,4,12,13] if prime(i) == True])    