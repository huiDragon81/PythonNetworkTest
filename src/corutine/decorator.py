import time

def checkTime(func):
    def newFunc(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(end - start)
    return newFunc

@checkTime
def aFunc(maxValue):
    for i in range(1,maxValue+1):
        print(i)

@checkTime
def bFunc():
    print("This is Function-B")

@checkTime
def cFunc(start, end):
    for i in range(start, end+1):
        print (i)

aFunc(100)
bFunc()
cFunc();