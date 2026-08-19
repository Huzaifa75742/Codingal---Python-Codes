num = int(input("Enter a number: "))
t = num
numlen = 0
while t > 0:
    numlen = numlen + 1
    t = int(t / 10)

if numlen >= 4:
    numlen = int(numlen / 2)
    chk = 0
    while numlen > 0:
        rem = num % 10
        if chk == numlen:
            midOne = rem
        elif chk == (numlen - 1):
            midTwo = rem
        num = int(num / 10)
        chk = chk + 1
    prod = midOne * midTwo
    print("\nproduct of Middle two digits of the number is: ", prod)
else:
    print("\nthe number does not have enough digits to find the middle two digits.")

