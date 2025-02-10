#1
print('#1')
def squares_to_N(N):
    cnt=1
    while cnt <=N:
        yield cnt*cnt
        cnt+=1
series=squares_to_N(10)
for i in series:
    print(i)

#2
print('#2')
def even_numbers_to_N(N):
    cnt=0
    while cnt<=N:
        if cnt%2==0:
            yield cnt
        cnt+=1
N=int(input())
series=even_numbers_to_N(N)
for i in series:
    print(i)

#3
print('#3')
def numbers_divisible_by_3_and_4(N):
    cnt=0
    while cnt<=N:
        if cnt%3==0 and cnt%4==0:
            yield cnt
        cnt+=1
N=int(input())
series=numbers_divisible_by_3_and_4(N)
for i in series:
    print(i)

#4
print('#4')
def squares(a,b):
    while a<=b:
        yield a*a
        a+=1
series=squares(1,7)
for i in series:
    print(i)

#5
print('#5')
def all_numbers_down_to_0(N):
    cnt=N
    while cnt>=0:
        yield cnt
        cnt-=1
series=all_numbers_down_to_0(10)
for i in series:
    print(i)

    