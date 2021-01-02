




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


'''

커리큘럼
 
문제 :

각 온라인 강의는 선수 강의가 있을 수 있는데,

선수 강의가 있는 강의는 선수강의를 먼저 들어야만 해당 강의를 들을 수 있다.
 
총 N개의 강의를 듣고자 한다. 

모든 강의는 1번부터 N번까지의 번호를 가진다.

또한 동시에 여러 개의 강의를 들을 수 있다고 가정한다.

N개의 강의 정보가 주어졌을때 N개의 강의에 대하여

수강하기까지 걸리는 최소 시간을 각각 출력하는 프로그램을 작성하시오

 
 

입력 :

1. 듣고자하는 강의의 수 [1,   500]

2~.각 강의 시간[1,   100,000], 선수 강의 번호들 , -1 (정보의 순서가 강의 번호이다.)  

 


출력 :

1~N. 각 강의를 수강하는데 걸리는 최소 시간을 각 줄에 출력한다.


 

아이디어 :

위상정렬 알고리즘을 이용하여 선수 과목에 대한 처리를 하면 될 것 같다.

어차피 선수과목을 다수강해야 들을 수 있기 때문에 선수과목 수강 여부만 파악하면 된다.

선수과목들의 최소 시간을 저장하기위한 연결리스트를 생성하자

 


설계 :

1. 과목 수를 입력받는다. 

2. 과목에 대한 정보를 연결리스트a에 입력받는다.

3. 과목을 수강했는지 체크할 체크리스트b를 만든다.

4. 과목의 수강시간을 저장할 리스트c를 만든다.

5. 선수 과목들의 최소 시간을 저장할 연결리스트d를 만든다.

6. result 결과를 저장할 리스트e를 만든다.


7. 연결리스트의 인덱스의 길이가 0인 것과 체크리스트를 이용하여 인접차수가 0인 과목A를 찾는다.

8. 체크리스트에서 과목A를 체크한다.

9. 과목A의 최소 시간을 연결리스트d의 정보와 리스트c의 정보를 합하여 리스트e에 저장한다.

10. 연결리스트a에서 과목A의 정보를 지운다.

11. 과목A의 최소 시간을 지웠던 연결리스트d의 인덱스에 저장한다.   

12. 체크리스트가 모두 체크될때까지 7번부터 반복한다.

 


내가 구현한 코드 :

import sys
input_sys=sys.stdin.readline

# 1. 과목 수를 입력받는다. 
N= int(input())

# 2. 과목에 대한 정보를 입력받기 위한 연결리스트a를 만든다.
input_graph=[[] for i in range(N+1)]

# 3. 과목을 수강했는지 체크할 체크리스트b를 만든다.
check_list=[0 for i in range(N+1)]
check_list[0]=1

# 4. 과목의 수강시간을 저장할 리스트c를 만든다.
time_list=[0 for i in range(N+1)]

# 5. 선수 과목들의 최소 시간을 저장할 연결리스트d를 만든다.
find_min_list=[[] for i in range(N+1)]

# 6. result 결과를 저장할 리스트e를 만든다.
result_time_list=[0 for i in range(N+1)]

#.7 과목에 대한 정보를 연결리스트a에 입력받는다.
for i in range(1,N+1):
    temp=list(map(int,input_sys().rstrip().split()))
    time_list[i]=temp.pop(0) # 8. 과목의 수강시간을 리스트c에 저장한다.

    for j in temp:
        if j!=-1:
            input_graph[i].append(j)

flag= True

# 9. 체크리스트가 모두 체크될때까지 반복한다.
while flag:
    idx=0
    for i in input_graph:

		# 10. 연결리스트의 인덱스의 길이가 0인 것과 체크리스트를 이용하여 인접차수가 0인 과목A를 찾는다.
        if len(i)==0 and check_list[idx]==0:
        
        	# 11. 체크리스트에서 과목A를 체크한다.
            check_list[idx]=1
            
            # 12. 과목A의 최소 시간을 연결리스트d의 정보와 리스트c의 정보를 합하여 리스트e에 저장한다.
            if len(find_min_list[idx])==0:
                result_time_list[idx]=time_list[idx]
            else:
                result_time_list[idx]=max(find_min_list[idx])+time_list[idx]

            iidx=0
            for j in input_graph:
                if idx in j:
                	# 13. 연결리스트a에서 과목A의 정보를 지운다.
                    input_graph[iidx].pop(j.index(idx)) 
                    
                    # 14. 과목A의 최소 시간을 지웠던 연결리스트d의 인덱스에 저장한다.  
                    find_min_list[iidx].append(result_time_list[idx])

                iidx+=1

        idx+=1

    if 0 in check_list:
        continue
    else:
        flag=False

# 15. 출력한다.
for i in range(1,N+1):
    print(result_time_list[i])
    
    
    
    
저자가 구현한 코드 :

from collections import deque
import copy

# 노드의 개수 입력받기
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (v + 1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫 번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in range(1, v + 1):
        print(result[i])

topology_sort()




피드백 :

저자의 코드가 더 직관적이고 간단하다. 

저자의 코드 중에서 최소시간 리스트를 갱신하는 코드가 인상적이었다.

나중에 구현할때 사용해봐야겠다.

for i in graph[now]:

	result[i] = max( result[i] , result[now] + time[i] )
	

리스트의 값은 복제해야 할 때는 deepcopy( ) 함수를 사용하면 된다고 하니 숙지해두자.

(파이썬의 경우 리스트는 reference이므로 함수를 이용하여 복제해야한다.)
 
import copy

time=[ 1 for _ in range(10)]

result = copy.deepcopy(time)
 





'''






































