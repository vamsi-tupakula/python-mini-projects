def fibo(n):
    a = 0
    b = 1
    print(a, b, end=" ")
    for i in range(2,n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c

n = int(input("Enter the length of fibo series you want : "))
fibo(n)