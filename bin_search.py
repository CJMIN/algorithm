



''''

부품 찾기 설계

문제 :
전자 매장에 N개 종류의 부품이 있다.
손님이 M개 종류의 부품의 견적서를 요청했을때
부품이 있는 없는지 확인하는 프로그램을 작성하라

입력 :
1.N [1,100만]
2.N개의 정수가 공백으로 구분되어 입력된다.
3.M[1,10만]
4.M개의 정수가 공백으로 구분되어 입력된다.

출력 :
순서대로 확인하여 있으면 yes 없으면 no를 출력한다. 공백으로 구분한다.

아이디어 :

순차탐색의 경우
시간복잡도가 O(N)이므로 한번 탐색하는데 100만번의 연산이 필요하다.
따라서 10만 X 100만 = 1000억 이므로 시간초과이다.
보통 연산횟수가 10억번 이상이면 시간초과이다.
따라서 순차탐색은 사용할 수 없다.

이진탐색의 경우
log100만 = 약 19이고 NlogN=약 2000만이다.
따라서 이진 탐색의 시간 복잡도는 O(logN)이므로
탐색읋 한번하는데 최대 약 20번의 연산이 필요하다.
리스트를 정렬하는 시간 복잡도가 O(NlogN)이므로
N이 백만이면 2000만번의 연산이 필요하다.
2000만 + 20X10만 = 2200만 의 연산이 필요하다.

따라서 이진탐색을 이용해서 구현가능하다.

print("yes",end=" ")을 이용해서 출력하면 행변경이 되지 않고 출력할 수 있다.

설계 :
1. 입력받기
2. 이진탐색 함수 구현하기
3. N리스트 정렬하기
4. M번 반복하여 이진탐색함수로 확인하여 출력하기

내가 구현한 코드 :

import sys

n=int(input())
n_list=list(map(int,sys.stdin.readline().rstrip().split()))
m=int(input())
m_list=list(map(int,sys.stdin.readline().rstrip().split()))

def bin_search(array,target,start,end):

    mid=(start+end)//2

    if start>end:
        return print("no",end=" ")

    if array[mid]==target:
        return print("yes",end=" ")
    elif array[mid]>target:
        bin_search(array,target,start,mid-1)
    else:
        bin_search(array,target,mid+1,end)

n_list.sort()

for i in range(m):

    bin_search(n_list,m_list[i],0,n-1)

피드백 :
O(MlogN) + O(NlogN) =O((M+N)logN) 이다.

계수정렬과 집합 자료형을 이용하는 방법도 숙지해두자.

set() 함수를 이용하면 굉장히 간단하게 초기화 할 수 있다.
set() 함수는 집합 자료형을 초기화할 때 사용한다.
집합자료형은 단순히 특정한 데이터가 존재하는지 검사할때에 매우 효과적으로 사용할 수 있다고 한다.
집합자료형을 이용하면 시간 복잡도가 어떻게 되는건지 확인할 수 가 없네 흠..


'''



'''
 

떡볶이 떡 만들기 설계

문제 :
떡볶이 떡의 길이는 일정하지 않는데 한봉지에 들어가는 떡의 총길이를 절단기로 잘라서 맞춘다.
손님이 가져가는 떡의 길이 = (떡의 길이 - 절단기의 길이)을 N개의 떡개수 만큼 반복한 것의 합
손님이 요청한 길이가 M일때 적어도 M만큼의 떡을 얻기 위해
절단기에 설정할 수 있는 높이의 최대값을 구하는 프로그램을 작성하시오

입력 :
1.떡의 개수 N [1,100만], 요청한 길이 M [1,20억]
2.N개 떡의 개별 높이 입력 , 떡의 길이 범위[0,10억]


출력 : 절단기 높이의 최대값

 



아이디어 :

범위가 크므로 이진탐새을하기위해 리스트를 정렬한다.(2000만번)
이진탐색 연산은 log10억=약 30 그리고
손님이 가져가는 떡의 길이를 구하기 위해여 약 100만 원소를 빼고 더하는 연산을 하므로 약 100만번
대략적으로 30*100만 = 3000만 이므로 10억 보다 작다. 따라서 시간초과가 나지 않는다.



설계:

1. 입력받기
2. 떡의 길이의 정보를 담은 리스트를 정렬한다. (2000만번 연산)
3. 떡의 길이 리스트와 절단기의 길이를 인자로 받고 손님이 가져가는 떡의 길이를 반환하는 함수 구현하기
4. 이진탐색 함수 구현하기 (인자 : 떡의 길이 리스트,손님이 요청한 떡의 길이, start, end) (반환값 : 최대 절단기 길이)

(기저 조건 경우의 수 잘세서 구현하기)
5. 출력하기



내가 구현한 코드 :

import sys

n,m=map(int,input().split())
n_list=list(map(int,sys.stdin.readline().split()))

n_list.sort()


def return_ricecake(n_list,h):
    sum=0
    for i in range(len(n_list)):
        piece=n_list[i] - h
        if piece>0:
            sum+=piece
    return sum

start=0
end=n_list[len(n_list)-1]


def bin_search(n_list,target,start,end):
    mid=(start+end)//2

    if start>end:
        while True:

            start -= 1
            end += 1

            if return_ricecake(n_list,start)>target and return_ricecake(n_list,start+1)<target :
                return start
            elif return_ricecake(n_list,end-1)>target and return_ricecake(n_list,end)<target :
                return end-1

    if return_ricecake(n_list,mid) > target :
        return bin_search(n_list,target,mid+1,end)
    elif return_ricecake(n_list,mid) < target :
        return bin_search(n_list,target,start,mid-1)
    else:
        return mid

H=bin_search(n_list,m,start,end)
print(H)


피드백 :

항상 10억번 연산이 시간초과의 기준이 아닌가보다.

1초에 몇 번 연산이 파이썬에서 리미트인지 알아봐야겠다.

1초에 2000만번 연산이라고 생각하면 좋을 것 같다.고 한다.

따라서 2초이므로 4000만번이기 때문에 저자는 아슬아슬하다고 했다.

 

저자는 일반적으로 파라메트릭 서치 문제 유형은 이진 탐색을 재귀적으로 구현하지 않고

반복문으로 이용해 구현하면 더 간결하게 문제를 풀 수 있다고 한다.

 

재귀로 풀면 기저 조건이 고려해야할 경우의 수가 많아지므로 휴먼에러가 발생할 수 있을 것 같다.

 

이진 탐색을 구현하는 두 가지 방법이 쓰이는 곳이 다양하므로

재귀적인 구현방법과 반복적인 구현방법을 모두 암기하고 있어야겠다.


'''


