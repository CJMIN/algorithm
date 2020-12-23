




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


















































