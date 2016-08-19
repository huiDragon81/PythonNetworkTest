
# 첫문자만 대문자로
result = "PYTHON".capitalize();
print(result);

# 주어진 문자가 몇번이나 있는가
result = "python is powerful".count('p');
print(result);

result = "python is powerful".count('p',5,-1); # 범위주기 , -1이라면 끝까지, 근데 굳이 -1을 안줘도 끝까지 함
print(result);

# 인코딩 파이썬은 기본 utf-8
result = "python".encode('cp949');
print(result);

result = "python".encode('utf8');
print(result);

# 끝나는 부분 compare , startswith는 반대
result = "python".endswith('on');
print(result);

result = "python".endswith('on',0,3);
print(result);

# 탭을 공백으로 치환 , 기본 4
result = "python\tpython\tpython\tpython".expandtabs(10) # 공백갯수 씨발 근데 왜 첫번째탭은 병신처럼 동작하는가
print(result)
result = "1\t2\t3\t4".expandtabs(10) # 공백갯수 씨발 근데 왜 첫번째탭은 병신처럼 동작하는가
print(result)
result = "aaa\tbbb\tccc\tddd".expandtabs(10) # 공백갯수 씨발 근데 왜 첫번째탭은 병신처럼 동작하는가
print(result)
result = "123123123123123123123123\t123123123123123123123123123\t123123123123123123123123123123\t12312312312312".expandtabs(10) # 공백갯수 씨발 근데 왜 첫번째탭은 병신처럼 동작하는가
print(result)


# find 첫번째 인덱스 반환 못찾으면 -1 , lfind, rfind
result = "python is powerful".find("p");
print(result)

result = "python is powerful".find("p",5,-1);
print(result)

# find 와 같지만 못찾으면 ValueError익셉션 , lindex, rindex
result = "python is powerful".index("p");
print(result)

#막간을 이용한 트라이캐치 구문 문법
try:
    result = "python is powerful".index("ppp",5,-1);
    print(result)
except ValueError:
    print("ValueError");
finally:
    print("씨발 파이썬 개새끼야")


# 알파벳숫자 찾기 , isalpha , isnumeric
result = "sdifjp;lasijdf;asf9023749-287349028u3".isalnum();
print(result);

# join 주어진 문자열 사이에 끼워넣기
result = " ".join("HOT");
print(result);

result = " ".join(["python","is","powerful"]);
print(result);

# 주어진 문자열로 해당 문자열 나누기, 세개의 튜플이 반환 , 못찾으면 걍 문자열만 리턴
result = "python is powerful".partition("is")
print(result)

# replace 모두가 알고 있는 그것
result = "python is powerful".replace("p","P",1) #maxcount 횟수만큼 바꾼다.
print(result)


# split 모두가 알고 있는 그것 , 기본으로 공백 분리,
result = "python is              powerful".split()
print(result)

result = "python is              powerful".split(' ',1)
print(result)


# strip 아마 그게 맞겠지 , lstrip, rstrip, 기본공백
result = "***********python############**************".strip("*")
print(result);






