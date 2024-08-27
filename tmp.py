import time

def nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

st = time.time()
c = nod(10000000,1)
ed = time.time()
tt = st - ed
print(c)
print(tt)
