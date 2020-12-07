



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


'''











