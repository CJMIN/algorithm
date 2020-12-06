

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