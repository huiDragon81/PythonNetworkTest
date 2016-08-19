

def countdown(n):
    while n > 0:
        yield n
        n -= 1
# 계속 이딴식으로 하면 StopIteration 익셉션이 나게 되어있음 그래서 트라이 캐치가 필요함 파이썬 개새끼야
# cnt = countdown(10);
# print (cnt.__next__());
# print (cnt.__next__());
# print (cnt.__next__());
# print (cnt.__next__());
# print (cnt.__next__());
# print (cnt.__next__());
# print (cnt.__next__());
# print (cnt.__next__());
# print (cnt.__next__());
# print (cnt.__next__());
# print (cnt.__next__());
# print (cnt.__next__());
# print (cnt.__next__());
# print (cnt.__next__());
# print (cnt.__next__());
# print (cnt.__next__());
# print (cnt.__next__());

# 하지만 for문은 알아서 익셉션을 잡아줌 파이썬 개새끼야
for i in countdown(10):
    print(i);

print("////////////////////////////////////////////////////////////////////")


#### 존나 제일 황당한건 yeild문법 파라미터 위치에 따라서 제네레이터냐 코류틴이냐가 달라진다 파이썬 개새끼야!!!

# 코루틴 - 데이터를 입력받아서 처리
# 제네레이터 - 데이터를 리턴
# 씨발 그럼 같이 쓰는건 뭐라고 부르냐 파이썬 개새끼야!!!

# 코루틴은 생성하고 나서 반드시 __next__를 해줘야 yield위치까지 이동을 하는 반면
# 제네레이터는  시발 하면 안됨

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



prn = printer()
prn.send("1")
prn.send("2")
prn.send(3)
prn.send(4)
prn.send("5 func python")

print("////////////////////////////////////////////////////////////////////")


#@coroutine  << --- sender함수는 제네레이터라고 불리기 때문에 이걸 붙이면 병신같이 되지 , 밑에서 출력이 1부터 나오게 되지
def sender():
    num = 0;
    while True:
        yield num
        num+=1

sen = sender()
print(sen.__next__())
print(next(sen))
print(sen.__next__())
print(next(sen))
print(sen.__next__())
print(next(sen))


print("////////////////////////////////////////////////////////////////////")
