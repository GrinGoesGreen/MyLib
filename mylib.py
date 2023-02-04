def even(a):
    count = 0
    for i in range(1,a+2):
        if a % i == 0:
            count+=1
            if count >2:
                break
    return (count <= 2)

def nod(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return(a)

def fact(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return(s)

def fib(n):
    lst = [1, 1]
    for i in range(2, n):
        lst.append(lst[i - 1] + lst[i - 2])
    print(*lst)

def tree(n):
    for i in range(n):
        print(' ' * (n - i - 1), "*" * (i * 2 + 1))

def quadric_solution(a, b, c):
    if a + b + c == 0:
        return 1, int(c/a)
    if a == 0:
        return None
    d = a**2 - 4*a*b
    if d > 0:
        d = d ** 0.5
        return (-b + d)/(2*a), (-b - d)/(2*a)
    elif d == 0:
        return (-b + d)/2*a
    elif d < 0:
        return None

def spiral(n,m):
    matrix = [[0] * m for _ in range(n)]
    dx, dy, x, y = 0, 1, 0, 0

    for i in range(1, n * m + 1):
        matrix[x][y] = i
        if matrix[(x + dx) % n][(y + dy) % m]:
            dx, dy = dy, -dx
        x += dx
        y += dy
    for line in matrix:
        print(*(f'{i:<3}' for i in line), sep='')

def LastSurvivor (n,k):
    last = 0
    for i in range(1, n + 1):
        last = (last + k) % i
    return (last + 1)

def proizv_cifr(n):
    s = 1
    while n >= 1:
        a = n % 10
        n = n// 10
        s *= a
    return s