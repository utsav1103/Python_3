def fact(n):

    #find factorial
    return 1 if (n == 1 or n == 0) else n * fact(n - 1)



num = 2+2
print(fact(num))
