
def fibonachu(n):
    f1,f2 = 0,1
    for i in range(n):
        f1, f2 = f2,f1 + f2
        yield f1

n = 1000
for f in fibonachu(n):
    print(f)