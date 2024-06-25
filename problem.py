#palindrome
for i in range(1,201):
    i =str(i)
    p = i[::-1]
    if p==i:
        print(p)
#method 2
print([i for i in range(1,201) if str(i)[::-1]==str(i)])