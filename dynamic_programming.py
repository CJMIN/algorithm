

'''

1로 만들기 설계

문제 :
정수 x가 주어질 때
정수 x에 사용할 수 있는 연산은 4가지이다.
1. x가 5로 나누어 떨어지면 5로 나눈다.
2. x가 3으로 나누어 떨어지면 3으로 나눈다.
3. x가 2로 나누어 떨어지면 2로 나눈다.
4. x에서 1을 뺀다.

정수 x 가 주어졌을 때
연산 4개를 적절히 사용해서 1을 만들려고 한다.
연산을 사용하는 횟수의 최소값을 구하시오



입력 :
1. x [1,30000]



출력 :
1. 연산을 하는 횟수의 최소값



아이디어 : 다이나믹 프로그래밍 적용하여 풀기

<다이나믹 프로그램 조건 2가지>
  1. 최적의 부분 구조 :
    큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있다.
  2. 중복되는 부분 문제 :
    동일한 작은 문제를 반복적으로 해결해야 한다.

1. 어떻게 하면 이 문제를 작은 문제로 나눌 수 있을까?
작은 문제 4가지 경우의 수 중에 어떤 것을 선택해야하는지

2. 어떻게 하면 그 작은 문제를 모아서 이 문제를 해결할 수 있을까?
완전탐색으로 모든 경우의 수를 확인하면 된다. (완전탐색)

3. 반복되는 동일한 작은 문제는 어떤 것이 있을까?
N이 최대 3만이므로 최대 3만개의 동일한 작은 문제가 생길 수 있다.

일단 반복문으로 한번 구현해보고 난 후에
재귀함수로 다시 구현해봐야겠다.

바텀업 방식인 상향식으로 구현하기위해서
1부터 시작해서 아래와 같은 연산을 수행하겠다.
1. 5를 곱한다
2. 3을 곱한다.
3. 2를 곱한다.
4. 1을 더한다.


설계 :

1. 입력 받기
2. 크기가 3만인 중복 확인 리스트 만들기
3. while list[x]==0 and queue:
    큐에서 값을 하나 빼서
    해당 값에 연산 4개를 하며 반복하고
    연산을 한 값을 인덱스로하는 list 값이 0이고 인덱스값이 30000보다 작거나 같으면
    해당 인덱스의 값을 연산횟수로 초기화하고 큐에 넣는다.
    아니면 패스
4. list[x] 출력

내가 구현한 코드 :

from collections import deque

x = int(input())

n_list = [0] * 30010

count = 0
queue = deque([[1, count]])

while n_list[x] == 0 and queue:

    current_node = queue.popleft()

    check = []

    check.append(current_node[0] * 5)
    check.append(current_node[0] * 3)
    check.append(current_node[0] * 2)
    check.append(current_node[0] + 1)
    current_node[1] += 1

    for i in range(4):
        if check[i]>30000:
            continue
        if n_list[check[i]] == 0:
            n_list[check[i]] = current_node[1]
            queue.append([check[i], current_node[1]])

print(n_list[x])

피드백 :
저자는 2부터 x까지 카운트를 모두 계산해서 리스트에 초기화하는 방식으로
바텀업 방식을 구현하였다.

저자가 세운 이 문제의 점화식은 " a(i) = min(a(i-1),a(i/2),a(i/3),a(i/5))+1 " 이다.

저자가 구현한 간단한 코드를 숙지하도록 하자


저자가 구현한 코드 :

x=int(input())

d=[0]*30001

for i in range(2,x+1):

    d[i]=d[i-1]+1

    if i%2==0:
        d[i] == min(d[i], d[i // 2] + 1)
    if i%3==0:
        d[i] == min(d[i], d[i // 3] + 1)
    if i%5==0:
        d[i] == min(d[i], d[i // 5] + 1)

print(d[x])



'''



x=int(input())

d=[0]*30001

for i in range(2,x+1):

    d[i]=d[i-1]+1

    if i%2==0:
        d[i] == min(d[i], d[i // 2] + 1)
    if i%3==0:
        d[i] == min(d[i], d[i // 3] + 1)
    if i%5==0:
        d[i] == min(d[i], d[i // 5] + 1)

print(d[x])
