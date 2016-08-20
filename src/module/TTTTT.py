for n in [2,3,4,5,6,7,8,9]:
    print("-- {}단 --".format(n));
    for i in [1,2,3,4,5,6,7,8,9]:
        print("{} * {} = {}".format(n,i,n*i));


for i in [1,2,3]:
    if i==4:
        break;
else:
    print("no break");   #for 문이 break를 거치지 않고 정상 종료된경우 출력


#range - 수열튜플을 생성한다.
for i in range(10,20,3):
    print(i);
