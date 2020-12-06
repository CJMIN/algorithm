

'''
<위에서 아래로 설계>



문제 :

하나의 수열에는 다양한 수가 존재한다.

수열을 내림차순으로 정렬하는 프로그램을 만드시오



입력 :

1. 수열에 속해 있는 수의 개수 N [1,500]

2~N+1. N개의 수가 입력된다. [1,100000]



출력 : 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다.



아이디어 :

sort() 메서드를 사용하자



설계  :

1. 입력 받기

2. 정렬하기

3. 출력하기



내가 구현한 코드 :

n=int(input())

input_list=[]


for i in range(n):
    input_value=int(input())
    input_list.append(input_value)

input_list.sort(reverse=1)

for i in range(len(input_list)):
    print(input_list[i],end=' ')

'''




'''

<성적이 낮은 순으로 학생 출력하기>



문제 :

N명의 학생 정보 (학생의 이름과 학생의 성적으로 구분된다.)

각 학생의 이름과 성적정보가 주어졌을때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오



입력 :

1. 학생의 수 N

2~N+1. 학생이름 학생성적 (성적은 100이하이다.)



출력 :

성적이 낮은 순으로 이름을 출력한다.

성적이 동일하면 자유롭게 출력해도 된다.



아이디어 :

리스트에 튜플 형태로 입력 받기

sorted()의 key 인자로 함수를 입력받는다.





설계 :

1. N 입력 받기

2. 튜플로 이름 성적 입력받기

3. sorted의 key 인자에 들어갈 튜플 중에 성적을 반환하는 함수 만들기

4. 정렬하기

5. 출력하기



내가 구현한 코드 :

n=int(input())

student_list=[]

for i in range(n):
    name, score = input().split()
    student_list.append((name,score))

def retuen_score(tuple_data):
    return tuple_data[1]

sorted_list=sorted(student_list,key=retuen_score,reverse=1)

print(sorted_list)



피드백 :

lambda 문법 숙지할 것

sorted_list=sorted(student_list, key=lambda tuple_data : tuple_data[1], reverse=1)


'''








'''

두 배열의 원소 교체 설계

문제 :

N개의 자연수 원소로 구성된 두개의 배열 A와 B가 있다.

최대 k번 바꿔치기 연산을 수행할 수 있다.

바꿔치기 연산이란 배열A에 있는 원소 하나와 배열B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것이다.

최종 목표는 배열A의 모든 원소의 합이 최대가 되도록 하는 것이다.

N K A배열 B배열의 정보가 중졌을때 최대 K번의 바꿔치기 연산을 수행하여

만들 수 있는 배열 A의 모든 원소의 합의 최대값을 출력하는 프로그램을 작성하시오



입력 :

1. N [1,10만], K 

2. A의 원소들이 공백으로 구분되어 입력 (모든 원소는 1000만보다 작은 자연수)

3. B의 원소들이 공백으로 구분되어 입력 (모든 원소는 1000만보다 작은 자연수)




출력:

최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열A의 모든 원소의 최대값을 출력한다.





아이디어 : 

A 배열과 B 배열을 리스트로 구현하고

sort() 메서드를 이용하여 B의 최대값과 A의 최소값을 비교하여

B의 최대값이 더 크면 바꿔치기 연산을 최대 k번 수행한다.



설계:

1. N,K 입력받기

2. 리스트로 A와 B 입력받기

3. k번 반복문 돌리기

4. 비교하여 바꿔치기 연산하기



내가 구현한 코드 :

n,k=map(int,input().split())

A_array=list(map(int,input().split()))
B_array=list(map(int,input().split()))

A_array.sort()
B_array.sort(reverse=1)

for i in range(k):
    
    if A_array[0]<B_array[0]:
        A_array[0],B_array[0]=B_array[0],A_array[0]
    else:
        break
print(sum(A_array))
피드백 : 



연산 횟수가 10억번을 넘어가면 일반적으로 시간 초과이다.



이때 N은 10만이므로 N^2이면 시간초과이다.



log100000/log2 = 약 16 이다.

 

O(NlogN)을 보장하는 정렬 알고리즘을 이용하면 시간초과가 없다.



파이썬 기본 정렬 메서드는 최악의 경우에도 O(NlogN)을 보장한다. 

'''




























