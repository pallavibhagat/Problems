def even_fib():
    limit = 4000000
    sum = 0
    a,b = 0,1
    c = b
    while c < limit:
        if c%2 == 0:
            sum += c
        c = a+b
        a,b = b,c
    print sum

if __name__ == '__main__':
    even_fib()