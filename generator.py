def natural(start, end):
    i = start
    while i< end:
        yield i
        i = i+1


def febonacci(a,b,limit):
    c = a+b
    yield a
    yield b
    while (a+b) < limit:
        c = a+b
        yield c
        a = b
        b = c