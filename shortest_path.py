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




'''