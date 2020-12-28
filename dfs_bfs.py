'''

bfs 함수 구현  :

from collections import deque

def bfs(graph,start,visited):

    queue = deque([start])

    visited[start] = True

    while queue :

        v = queue.popleft()

        print(v, end='')

        for i in graph[v]:

            if not visited[i]:
                queue.append(i)
                visited[i] = True
'''


'''

음료수 얼려 먹기

 

문제 :

N x M 크기의 얼음 틀이 있다.

뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.

구멍이 뚫려있는 것들끼리 상하좌우로 붙어있으면 연결되어 있는 것으로 간주한다.

이때 얼음 틀의 모양이 주어졌을때

생성되는 아이스크림의 총 개수를 구하는 프로그램을 작성하라

 

입력 :

1. N M [1,1000]

2~N+1. 얼음틀의 형태

 

ex)

15 14

00000111100000

11111101111110

11011101101110

11011101100000

11011111111111

11011111111100

11000000011111

01111111111111

00000000011111

01111111111000

00011111111000

00000001111000

11111111110011

11100011111111

11100011111111

 

출력 : 총 개수

 

아이디어 :

2차원 배열을 그래프 형태로 생각하고 풀어보자

BFS를 이용해서 0인 부분부터 시작해서 0인 부분만 탐색하고 방문처리하자

연산이 백만번이므로 완전탐색을 써도 될 것 같다.

그래프에 0이 없을 때까지 계속 찾자.

탐색을 한번 끝마칠때마다 카운트를 증가시키자.

 

설계 :

#1. 그래프 형태로 입력 받기

#2. 테두리에 1로 경계만들기

#3. BFS 함수 만들기 (0일때 방문하고 방문처리를 1로 하기)

#4. 그래프에 0이 있는 확인하는 함수 만들기 // 0이 있다면 해당 좌표를 반환하기 (완전탐색으로 구현하기)

#5. 그래프에 0이 없어질때까지 반복하기 

 

내가 구현한 코드 :

   

from collections import deque


n,m=map(int,input().split())

graph=[]

dir=[(1,0),(-1,0),(0,1),(0,-1)]


for i in range(1,n+1):

    for j in range(1,m+1):

        per_row = []
        for k in dir:



            if i+k[0]>=1 and i+k[0]<=n and j +k[1]>=1 and j+k[1]<=m:

                per_row.append((i+k[0],j+k[1]))
                graph.append(per_row)



input_vlaue=[]


updown_value=['1']*(m+2)

input_vlaue.append(updown_value)



#1. 그래프 형태로 입력 받기

for i in range(n):

    n=list(input())
    n.append('1')
    n.reverse()
    n.append('1')
    n.reverse()

    input_vlaue.append(n)



input_vlaue.append(updown_value)


def BFS(graph,start,visited):

    queue = deque([start])
    visited[start[0]][start[1]]=1

    while queue:

        v = queue.popleft() #튜플 형태


		# 1행의 원소들붙 쭉 입력되므로 (row-1)*m+col -1 이 인덱스이다.

        for i in graph[(v[0]-1)*m+v[1] -1]:

			if visited[i[0]][i[1]]=='0':

                queue.append(i)
                
                visited[i[0]][i[1]]='1'

    return visited



def check_zero(visited):

    row=len(visited)
    col=len(visited[0])


    for i in range(row):

        for j in range(col):

            if visited[i][j]=='0':
                return i,j

    return "AB"


count=0


while True:

    start = list(check_zero(input_vlaue))

    if start[0]=='A':
        break

    input_vlaue=BFS(graph,start,input_vlaue)

    count+=1


print(count)



피드백 :

list( map( int,input() ) )

이렇게 111111111111을 입력받으면

[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 이 된다.

 

graph를 전역으로 쓰므로 함수에서 사용할 수 있게 하였다.

 

인접리스트로 그래프를 구현하는 것보다

이런 좌표형태에서는 인접행렬로 그래프를 구현해서 DFS를 쓰는 것이 좀 더 효율적인 것 같다.

dfs를 상하좌우로 재귀적 호출하므로서 코드가 굉장히 간단해졌다.

'''

'''

미로 탈출

 

문제 : 

N x M 크기의 직사각형 형태의 미로에 갇혀있다.

시작 위치 (1, 1)

미로 출구 (N, M) 

한번에 한 칸씩 이동할 수 있다.

괴물이 있는 부분은 0

괴물이 없는 부분은 1 로 표시되어 있다.

미로를 탈출하기위해 움직여야하는 최소 칸의 개수를 구하라

칸을셀때는 시작칸과 마지막칸을 모두 포함해서 센다.

 

입력 :

1. N M [4, 200]

2~N+1. 미로정보

 

5 6
101010
111111
000001
111111
111111

6 6
101010
111111
000001
111111
100000
111111

 

출력 :

1. 최소 이동 칸의 개수

 

아이디어 : 

 

DFS에서 오른쪽과 아래의 우선순위를 왼쪽과 위의 우선순위보다

높게 하면 최소 이동칸을 구할 수 있을 것 같다.

깊이가 바로 최소이동칸-1 이다.

 

BFS를 이용하여 추가할때마다 깊이를 같이 큐에 묶어서 추가해주면 큐에 n,m이 삽입될 때의 깊이가 최소 이동칸이다.

 

설계 :

1. 입력받기 (테두리 1로 만들기)1

2. BFS 함수 만들기 (인수 : 미로, 시작점) (반환 : 최소 이동칸수)

3. BFS로 최소 이동 칸 수 찾기

4. 출력하기

 

내가 구현한 코드 :

from collections import deque
    

n, m = map(int, input().split())

graph=[]

graph.append([0]*(m+2))

for i in range(n):

    temp=list(map(int,input()))
    temp.append(0)
    temp.reverse()
    temp.append(0)
    temp.reverse()
    graph.append(temp)

graph.append([0]*(m+2))


dir_v=[(0,1),(1,0),(0,-1),(-1,0)] # 오른쪽 아래 왼쪽 위
start=(1,1,1) # 좌표 깊이


def bfs(graph,start):

    F_row=len(graph)-2
    F_col=len(graph[0])-2

    queue=deque([start])

    while queue:
        check=queue.popleft()
        row=check[0]
        col=check[1]
        depth=check[2]
        if row == F_row and col == F_col :
            return depth


        for i in range(4):
            if graph[row+dir_v[i][0]][col+dir_v[i][1]]==1:
                queue.append((row+dir_v[i][0],col+dir_v[i][1],depth+1))


result_count=bfs(graph,start)
print(result_count)
 

피드백 :

처음에 DFS로 구현을 하였지만 최소 이동 칸 수를 구할 수 없었다.

다음번에는 최소 이동 칸수 문제가 나오면 바로 BFS로 구현을 해야겠다.

BFS 대신에 꼭 DFS로만 풀어야하는 문제가 있는지 확인해봐야겠다.

만약 없다면 무조건 BFS로만 풀어야겠다.

 

내 방법이 저자방법보다 조금 더 간단한 것 같다.

'''