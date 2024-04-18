# this file was created by miles crooks

def f1(x,y):
    print(x *y)
    return x * y

f1(2, 5)

def f2(x, y):
    print(str(x)+' times '+str(y)+' = '+str(f1(x,y)))

f2(3, 4)

def f3(x, y):
    count = 0
    while count != 10:
        print(count)
        f1(x, y)
        f2(x, y)
        count += 1

f3(5, 5)