




'''

서로소 집합 자료구조 동작과정


문제 :



서로소 집합 자료구조의 합치기 연산이 여러 개가 주어졌을때
해당 연산을 수행하고 난 후의 각 노드가 속해있는 집합의 루트 노드를 출력하고
각 노드의 부모 노드를 출력하는 프로그램을 작성하라



입력 :

1. 노드의 개수, 간선의 개수
2~. 합치기 연산의 정보



출력 :

각 노드의 루트노드와 부모노드 출력하기
(노드A, 노드A의 루트 노드, 노드A의 부모노드)


아이디어 :

서로소 집합 자료구조의 연산인 합치기 연산과 루트 노드 반환 연산 2가지를 구현해서 해당 문제를 해결하면 될 듯 하다.



설계 :

1. 입력 받기
2. 노드의 부모 노드를 가리키는 리스트 만들기 (해당 노드의 번호를 리스트의 인덱스로 설정하기)
3. 부모 노드를 가리키는 리스트의 초기화는 INF로 설정하기
4. 루트 노드를 반환하는 함수 구현하기
5. 루트 A와 루트 B가 중에 더 작은 함수가 부모노드가 되도록 하는 합치기 연산 구현하기
6. 출력하기



내가 구현한 코드 :



node_num,lin_num = map(int,input().split())
INF=int(1e9)
parent_list=[INF for i in range(node_num+1)]

union_info=[]


for i in range(lin_num):

    temp=[]
    temp=list(map(int,input().split()))
    union_info.append(temp)




# def root_return(parent_list,node_num):
#
#     return_value = node_num
#
#     while True:
#         if parent_list[node_num] != INF:
#              node_num=parent_list[node_num]
#              return_value=node_num
#
#         else:
#             return return_value


def root_return(parent_list,node_num):

    if parent_list[node_num]!=INF:
        parent_list[node_num]=root_return(parent_list,parent_list[node_num])
    return parent_list[node_num]



def union_func(parent_list,node_A,node_B):

    if root_return(parent_list,node_A) > root_return(parent_list,node_B):

        parent_list[root_return(parent_list,node_A)]=root_return(parent_list,node_B)

    elif root_return(parent_list,node_A) < root_return(parent_list,node_B):

        parent_list[root_return(parent_list,node_B)] = root_return(parent_list,node_A)
    else :
        print("같은 집합")




for i in union_info:

    union_func(parent_list,i[0],i[1])

root_list=[0]

for i in range(1,node_num+1):
    root_list.append(root_return(parent_list,i))

print(root_list)
print(parent_list)



'''






'''

문제 :

크루스칼 알고리즘 구현하기





입력 :

1. 노드개수 , 간선 개수
2~. 간선정보(가중치.노드1,노드2)



출력 :

부모 노드 리스트 출력
간선정보의 합 출력





아이디어 :

간선들의 정보를 오름차순으로 정렬하고
작은 간선부터 차례대로 선택하여 사이클을 생성하는지
서로소 집합자료구조를 이용하여 확인하고
사이클을 생성하지 않는다면 해당 간선을 포함시킨다.
모든 간선에 대해서 확인한다.



설계 :

1. 입력받기
2. 간선들의 정보를 오름차순으로 정렬하기
3. 서로소 집합 자료구조 연산 2가지 함수 구현하기
4. 서로소 집합 연산을 이용하여 사이클을 생성하는지 확인하는 함수 구현하기
5. 모든 간선들에 대하여 사이클을 생성하는지 확인하고 사이클을 생성하지 않는다면 집합에 추가하는 것을 반복한다.





내가 구현한 코드 :

import sys

input=sys.stdin.readline

node_num,line_num=map(int,input().rstrip().split())

weight_list = []

for i in range(line_num):
    temp=list(map(int,input().rstrip().split()))
    temp[0],temp[2]=temp[2],temp[0]
    weight_list.append(temp)

weight_list.sort()

root_list=[i for i in range(node_num+1)]


def root_return(root_list,node): #find

    if root_list[node]!=node:
        root_list[node]=root_return(root_list,root_list[node])
    return root_list[node]

def union(root_list,node1,node2):

    if root_return(root_list,node1)>root_return(root_list,node2):
        root_list[root_return(root_list,node1)]=root_return(root_list,node2)
    elif root_return(root_list,node1)<root_return(root_list,node2):
        root_list[root_return(root_list,node2)]=root_return(root_list,node1)
    else:
        return False

sum_of_weight=0

for i in weight_list:
    flag=union(root_list,i[1],i[2])
    if flag!=False:
        sum_of_weight+=i[0]


print("sum_of_weight :",sum_of_weight)
'''





'''
문제 :

위상정렬 알고리즘 구현하기




입력 :

1. 노드 개수, 간선 개수
2~. 시작 노드, 끝 노드




출력 : 

방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열한 결과 출력하기




아이디어 :

진입차수를 확인하는 리스트를 만든다.
진입차수가 0인 노드를 출력하는 함수를 만든다.
진입차수가 0인 된 노드를 큐에 집어넣는다.
큐에서 꺼낸 노드가 연결하는 간선을 끊고 진입차수리스트를 갱신한다.
큐가 빌때까지 반복한다.





설계 :

# 1. 입력받기
# 2. 진입차수 갱신리스트를 만든다.
# 3. 진입차수가 0인 노드를 반환하는 함수를 만든다.
# 4. 노드가 연결하는 간선을 끊고 진입차수 리스트를 갱신하는 함수를 만든다.
# 5. 큐에 진입차수가 0인 초기 값 노드를 집어넣는다.
# 6. 큐에 pop된 노드와 연결된 노드를 끊고 진입차수 리스트를 갱신하고
# 진입차수가 0인 노드를 큐에 넣는 행위를 큐가 빌때까지 계속한다.
# 7. pop한 노드는 순서대로 순서 리스트에 넣는다.
# 8. 순서리스트를 출력한다.





내가 구현한 코드 :

import sys
from collections import deque
input=sys.stdin.readline

node_num,line_num=map(int,input().rstrip().split())

node_info=[]

input_line_list=[0 for i in range(node_num+1)]
input_line_list[0]=-1

for i in range(line_num):
    temp=list(map(int,input().rstrip().split()))
    input_line_list[temp[1]]+=1 # 진입차수 리스트 초기화를 위한 코드
    node_info.append(temp)
print(input_line_list)

def return_zero_node(input_line_list):

    if 0 in input_line_list:
        return input_line_list.index(0)
    else :
        return False

def renewal_input_line_list(node_info,input_line_list,node):

    for i in node_info:
        if i[0]==node:
            input_line_list[i[1]]-=1

node_q=deque([])

node_q.append(return_zero_node(input_line_list))

order_list=[]

while node_q:

    pop_node=node_q.popleft()
    input_line_list[pop_node]=-1
    order_list.append(pop_node)
    renewal_input_line_list(node_info,input_line_list,pop_node)

    while 0 in input_line_list :

        zero_node=return_zero_node(input_line_list)
        node_q.append(return_zero_node(input_line_list))
        input_line_list[zero_node]=-1

print(order_list)

'''


'''


팀 결성


문제 : 

학생들에게 0번부터 N+1번까지 번호를 부여했다.
처음에는 모든 학생들이 서로다른 팀으로 구별되어 총 N+1개의 팀이 존재한다.
팀 합치기 연산과
같은 팀 여부 확인 연산이 존재한다.
M개의 연산이 수행되는데 이중에 같은 팀 여부를 확인하는 연산의 결과만 출력하는 프로그램을 작성하여라



입력 :
1. N M [1,  100,000]
2~. 연산종류(0,1) 학생1 학생2



출력 :
같은 팀 확인 여부를 YES와 NO로 출력하기



아이디어 :
서로소 집합 자료구조를 이용하면 될 것 같다.



설계 :
# 1. 입력받기
# 2. 부모 노드를 저장하기위한 리스트 선언하기
# 3. 루트노드 출력하는 함수 구현하기
# 4. 합치기 연산 함수 구현하기
# 5. 같은 팀 여부 확인하는 함수 구현하기 (반환 YES NO)
# 6. 해당연산에 맞는 연산 수행하기



내가 구현한 코드 :

import sys
input=sys.stdin.readline
N,M=map(int,input().rstrip().split())

cal_info=[]



for i in range(M):
    temp=list(map(int,input().rstrip().split()))
    cal_info.append(temp)

parent_list=[i for i in range(N+1)]



def return_root(parent_list, node):

    if parent_list[node]!=node:
        parent_list[node]=return_root(parent_list,parent_list[node])
    return  parent_list[node]



def union_cal(parent_list,node1,node2):

    if return_root(parent_list,node1)<return_root(parent_list,node2):
        parent_list[return_root(parent_list,node2)]=return_root(parent_list,node1)
    elif return_root(parent_list,node2)<return_root(parent_list,node1):
        parent_list[return_root(parent_list,node1)]=return_root(parent_list,node2)
    else :
        return 0

def check_team(parent_list,node1,node2):

    if return_root(parent_list,node1)==return_root(parent_list,node2):
        print("YES")
    else :
        print("NO")



for i in cal_info:

    if i[0]==0:
        union_cal(parent_list,i[1],i[2])
    elif i[0]==1:
        check_team(parent_list,i[1],i[2])
'''





'''

도시 분할 계획

문제 : 

마을은 N개의 집과 집들을 연결하는 M개의 길로 이루어져있다.
무방향이다.
길에는 가중치가 존재한다.
마을을 2개의 분리된 마을로 분할하려고 한다.
마을을 분할할때는 집들이 서로 연결되도록 분할해야한다.
그리고 마을에는 집이 최소 한개 이상 있어야한다.

마을을 분리시킨후 필요없는 길은 없앤다.
분리된 마을안에서도 분리된 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없앨 수 있다.
(길이 연결만 된다면 최적화 시켜도 된다는 말)

이 조건들을 만족하면서 존재하는 길의 가중치의 합을 최소로 하게하는 프로그램을 작성하라.




입력 :

1. 집의 개수 N [2,  100,000], 길의 개수 M [1,   1,000,000]
2~.집1 집2 가중치




출력 :

마을을 분리시키고 길을 없애고 남은 길들의 가중치의 합




아이디어 : 

크루스칼 알고리즘을 이용하여 모든 노드를 이은 간선의 가중치들의 합에서 가장 큰 가중치를 빼면 될 것 같다.




설계 : 

1. 입력받기
2. 가중치 정렬하기
3. 서로소 집합 자료구조 연산 2개 함수로 만들기

  (1) 루트 노드 반환하는 함수
  (2) 합치기 함수(사이클 확인 가능)

4. 크루스칼 알고리즘 구현
5. 간선들의 합에 가장 큰 간선을 뺀 값을 출력하기







내가 구현한 코드 : 

import sys

input=sys.stdin.readline

N,M=map(int, input().rstrip().split())

graph_info=[]


for i in range(M):

    node1,node2,weight=map(int,input().rstrip().split())
    graph_info.append([weight,node1,node2])


graph_info.sort()

parent_list=[i for i in range(N+1)]

def return_root(parent_list,node):

    if parent_list[node]!=node:
        parent_list[node]=return_root(parent_list,parent_list[node])
    return parent_list[node]

def union(parent_list,node1,node2):

    if return_root(parent_list,node1)<return_root(parent_list,node2):
        parent_list[return_root(parent_list,node2)] = return_root(parent_list,node1)
        return True
    elif return_root(parent_list,node1)>return_root(parent_list,node2):
        parent_list[return_root(parent_list,node1)] = return_root(parent_list,node2)
        return True
    else:
        return False

max = 0
sum=0

for i in graph_info:

    flag=union(parent_list,i[1],i[2])

    if flag:
        if max < i[0]:
            max = i[0]
        sum+=i[0]


print(sum-max)


'''




































