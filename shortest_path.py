'''

다익스트라 최단경로 알고리즘

import sys
input=sys.stdin.readline
INF=int(1e9)

n,m=map(int, input().split())

start=int(input())

graph=[ [] for i in range(n+1) ]

visited = [False] * (n+1)

distance = [INF]*(n+1)


for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value=INF
    index = 0
    for i in range(1,n+1):
        if distance[i]< min_value and not visited[i]:
            min_value = distance[i]
            index=i
    return index

def dijkstra(start):

    distance[start]=0
    visited[start]=True
    for j in graph[start]:
        distance[j[0]]=j[1]

    for i in range(n-1):
        now = get_smallest_node()
        visited[now]=True

        for j in graph[now]:
            cost=distance[now]+j[1]
            if cost<distance[j[0]]:
                distance[j[0]]=cost

dijkstra(start)


for i in range(1,n+1):
    if distance[i]==INF:
        print("infinity")
    else:
        print(distance[i])

'''


'''
내가 구현한 우선순위 큐를 이용한 다익스트라 알고리즘 

import sys
import heapq

# 1. 노드 개수와 간선 개수 입력 받기
n,l = list(map(int,sys.stdin.readline().rstrip().split()))

# 시작 노드 입력 받기
start_node=int(sys.stdin.readline().rstrip())

# 노드 연결 정보 graph에 입력받기
graph = []
for i in range(l*2):
    temp=list(map(int,sys.stdin.readline().rstrip().split()))
    graph.append(temp)

# 2. 출발 노드로부터의 최단거리를 갱신하기 위한 리스트 만들기

INF = int(1e9)
shortest_list = [INF for i in range(n+1)] # start노드가 결정되면 shortest_list[start]=0 해줘야한다.
shortest_list[start_node]=0

# 3. 우선순위 큐 초기화하기
start = [0,start_node]
pri_q = [start]

# 4. 방문 체크 리스트 만들기
visited=[False for i in range(n+1)]
visited[0]=True


# 5. 다익스트라 함수 구현하기


# 우선순위 큐가 빌떄까지 반복하는 반복문을 걸어준다. 초기값은 [0,start_node] 이다.
# 우선순위 큐에서 pop해서 노드 정보와 거리 정보를 나눈다.
# graph에 저장된 정보만큼 반복하여 최단 거리 리스트를 갱신한다.
# pop한 노드를 방문 체크한다.


def dijkstra():
    while pri_q:
        s_n = heapq.heappop(pri_q)

        s_len = s_n[0] # 우선순위 큐에서 pop한 것의 거리 정보
        s_node = s_n[1] # 우선순위 큐에서 pop한 것의 노드 정보

        for i in graph:

            p_len=i[1] + s_len #거리
            p_node=i[2] #노드

            if i[0]!=s_node or visited[p_node]==True:
                continue

            if p_len < shortest_list[p_node]:

                shortest_list[p_node]=p_len
                heapq.heappush(pri_q,[p_len,p_node])

        visited[s_node]=True
    return 0

# 6. 다익스트라 함수 실행하기
dijkstra()

# 7. 출력하기
print(shortest_list)
'''



'''

미래도시

문제 : 

공중 미래 도시에는 1번부터 n번까지의 회사가 있다.

특정회사끼리는 서로 도로를 통해 연결되고 있다. (연결된 2개의 회사는 양방향으로 이동가능하다)

A의 현재 위치는 1번 회사이고 x번 회사에 방문 하고자 한다. 

회사 끼리 연결되어 있다면 정확히 1만큼의 시간으로 이동할 수 있다.



k번 회사에 소개팅상대가 존재한다.

A는 k번 회사가서 소개팅을 한 후에 x번 회사에 갈 예정이다.

이때 A가 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성하시오 




입력 : 

1. N(노드 수) M(간선 수) [1,100]

2~M+1. 연결된 두 회사 의 번호 

M+2. X K [1,100]




출력 :

A가 k번회사를 거쳐 x번 회사로 가는 최소 이동 시간을 출력

만약 x에 도달할 수 없다면 -1을 출력




아이디어 : 

다익스트라 알고리즘을 이용하여 출발점이 1일 때 k까지의 최단거리와

출발점이 k일 때 x까지의 최단거리의 합을 구해서 출력하자




설계 : 

1. 입력받기

2. 최단경로를 저장할 리스트 만들기

3. 방문을 체크할 리스트 만들기

4. 다익스트라 알고리즘 구현하기

5. 출발점이 1이고 도착점이 k일 때 최단 거리 구하기

6. 출발점이 k이고 도착점이 x일 때 최단 거리 구하기

7. 5와 6의 합 출력하기



내가 구현한 코드 :



import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)

n, m= map(int,input().rstrip().split())

graph=[]

for _ in range(m):

    temp=list(map(int,input().split()))
    graph.append(temp)

x,k=map(int,input().split())


start_first=1
start_second=k
goal=x

shortest_list=[INF for _ in range(n+1)]
visited=[False for _ in range(n+1)]

shortest_list2=[INF for _ in range(n+1)]
visited2=[False for _ in range(n+1)]

def dijkstra(start,shortest_list_v,visited_v):

    pri_q = []
    heapq.heappush(pri_q,[0,start])
    shortest_list_v[start]=0

    while pri_q:

        temp=heapq.heappop(pri_q)

        shortest_node = temp[1]
        shortest_len = temp[0]

        for i in graph:

            if visited_v[shortest_node]==True:
                continue

            if i[0]==shortest_node:
                another_node=i[1]
            elif i[1]==shortest_node:
                another_node = i[0]
            else:
                continue

            if shortest_list_v[another_node]>shortest_len+1:
                shortest_list_v[another_node]=shortest_len+1
                heapq.heappush(pri_q,[shortest_list_v[another_node],another_node])

        visited_v[shortest_node]=True
    return shortest_list_v


list_1=dijkstra(start_first,shortest_list,visited)
first=list_1[start_second]

list_2=dijkstra(start_second,shortest_list2,visited2)
second=list_2[goal]

if first==INF or second==INF:
    print(-1)
else:
    print(first+second)


Test Case:

5 7 
1 2 
1 3 
1 4 
2 4 
3 4 
3 5 
4 5 
4 5 

결과 : 3

4 2 
1 3 
2 4 
3 4

결과 : -1

9 12
1 2
1 4
1 5
2 3
2 5
3 5
4 5
4 7
5 6
5 8
6 8
6 9
9 5

결과 : 3


피드백 :

input=sys.stdin.readline().rstrip 이렇게 쓰면 오류가 나서

input=sys.stdin.readline 이렇게 변경하니 오류가 없어졌다. 참고하자



나는 리스트를 인자로 넘기면 call by value 이라고 착각하고 있었는데

결과적으로는 call by reference였다.

따라서 해당 인자에 들어가야하는 값인 shortest_list와 visited를 하나씩 더 만들었다.

파이썬에서 인자 값은 정확하게는 call by object reference라고 한다.

인자로 어떤 값이 들어가는지에 따라 call by value인지 call by reference인지 결정되는 것 같다.

어떤 형태의 인자가  어디에 해당되는지는 아래 블로그를 참고하자


www.pymoon.com/entry/Python-%EC%9D%80-callbyvalue-%EC%9D%BC%EA%B9%8C-callbyreference-%EC%9D%BC%EA%B9%8C
developer-alle.tistory.com/339

'''


'''

전보

문제 :

N개의 도시가 있다.

도시 x에서 도시 y로 전보를 보내고자 한다면

도시 x에서 도시 y로 향하는 통로가 설치되어 있어야 한다.



x에서 y 통로만 있고 , y에서 x 통로가 없다면 y에서 x로는 전보를 보낼 수 없다.



통로를 거쳐 메세지를 보낼 경우 일정 시간이 소요된다.



c도시에서 위급상황이 발생되어 최대한 많은 도시로 메세지를 보냈을 때

메세지를 받은 도시의 개수와 

도시들이 모두 메세지를 받을때까지 걸리는 시간을 출력하는 프로그램을 작성하라









입력 :

1. N M C

도시의 개수, 통로의 개수, 메세지를 보내고자하는 도시

[1,30000] [1,200000] [1,N]

2~M+1. X Y Z

z [1,1000]







출력 :

메세지를받은도시의총개수  총걸린시간







아이디어 :

다익스트라를 이용하여 각 노드의 최단거리를 갱신하고

INF가 아닌 원소의 수를 계산하고

INF를 모두 -1로 초기화한 후에

MAX함수를 이용하여 가장 오래 걸린 시간을 출력한다.







설계 :

1. 입력 받기

2. 최소 거리 갱신 리스트 구현하기

3. 방문 체크 리스트 구현하기

4. 초기값 변수 선언하기



. 다익스트라 알고리즘 함수 구현하기

. INF인 원소를 index함수를 이용해 찾아내고 -1로 초기화 시키기 INF가 없을떄까지 반복하면 카운트세기

(이때 -1 해줘야 한다.)

. MAX함수를 이용하여 최대 시간 구하기

.카운트와 최대시간 출력하기





내가 구현한 코드 :

import sys
import heapq
input=sys.stdin.readline

INF=int(1e9)

n,m,c=map(int,input().split())

graph=[]

for _ in range(m):
    temp=list(map(int,input().split()))
    graph.append(temp)

shortest_list=[INF for _ in range(n+1)]
shortest_list[c]=0

visited=[False for _ in range(n+1)]

start_city=c


def dijkstra(start):

    pri_q=[]
    heapq.heappush(pri_q,[0,start])

    while pri_q:

        temp=heapq.heappop(pri_q)

        shortest_len=temp[0]
        shortest_node=temp[1]

        for i in graph:

            start_node=i[0]
            end_node=i[1]
            s_len=i[2]

            if start_node != shortest_node:
                continue

            if visited[start_node]==True:
                continue

            if shortest_list[end_node] > shortest_len + s_len:
                shortest_list[end_node] = shortest_len + s_len
                heapq.heappush(pri_q,[shortest_list[end_node],end_node])
        visited[shortest_node]=True
    return 0

dijkstra(start_city)

count=0
while True:
    if max(shortest_list)!=INF:
        break
    index=shortest_list.index(INF)
    shortest_list[index]=-1
    count+=1

the_num_of_city=len(shortest_list)-(count+1)
max_len=max(shortest_list)

print(the_num_of_city,max_len)



Test Case :



9 24 1 
1 2 1 
1 4 1 
1 5 1 
2 1 1 
2 3 2 
2 5 2 
3 2 2 
3 5 2 
4 1 1 
4 5 2 
4 7 2 
5 1 1 
5 2 2 
5 3 2 
5 4 2 
5 6 2 
5 8 2 
6 5 2 
6 8 3 
6 9 3 
7 4 2 
8 5 2 
8 6 3 
9 6 3 

결과 값 : 8 6

피드백 : 

n과 m이 충분히 크므로 O(n^3)의 시간복잡도를 가진 플로이드 워셜 알고리즘은 불가능하다 따라서

다익스트라 알고리즘을 사용하여야 한다.

'''































