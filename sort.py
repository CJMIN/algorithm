

'''
위에서 아래로 설계



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

'''

n=int(input())

input_list=[]


for i in range(n):
    input_value=int(input())
    input_list.append(input_value)

input_list.sort(reverse=1)

for i in range(len(input_list)):
    print(input_list[i],end=' ')

