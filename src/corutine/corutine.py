
def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.__next__()
        return cr
    return start

@coroutine
def printer():
    while True:
        line = (yield)
        print(line)

@coroutine
def sender():
    num = 0;
    while True:
        yield num
        num+=1

prn = printer()
prn.send("1")
prn.send("2")
prn.send(3)
prn.send(4)
prn.send("5 func python")

print()

sen = sender()
print(sen.__next__())
print(next(sen))
print(sen.__next__())
print(next(sen))
print(sen.__next__())
print(next(sen))






