n = 1
a = int(input("a = ? "))
x = " "
while n < 0.9*a:
    i = 2*n-1
    k = int(((2*a-1)-(2*n-1))/2)
    if n == 1:
        print(x*k + "O"*i + x*k)
    else:
        print(x*k + "*"*i + x*k)
    n = n + 1
while n >= 0.9*a and n <= a:
    i = 2*n-1
    k = int(((2*a-1)-(2*n-1))/2)
    print(x*(n-1) + "U" + x*(n-1))
    n = n + 1





