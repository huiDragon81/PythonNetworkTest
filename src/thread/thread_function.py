import threading
import time

def say(msg):
    while True:
        time.sleep(1)
        print(msg)

for msg in ['you', 'need', 'python']:
    t = threading.Thread(target=say, args=(msg,)) # 자바나 씨랑 별반 다를게 없음
    t.daemon = True # 프로그램이 죽으면 너도 죽어라
    t.start() # thread가 끝날때 까지 기다릴래믄 join함수를 걸고 , 걍 니혼자 돌다 알아서 죽어라 할래믄 dettach함수를 걸긔

for i in range(100):
    time.sleep(0.1)
    print(i)