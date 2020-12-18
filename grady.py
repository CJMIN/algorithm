

'''



큰수의 법칙 설계

문제 : 배열크기 N , 숫자가 더해지는 횟수 M, 연속으로 더해질수 있는 횟수 K
다양한 수로 이루어진 배열을 이용하여 같은 인덱스의 수를 K번 이상 더하지 않고
M번 더하여 만들 수 있는 가장 큰 수를 구하여라





입력 : 2<= N <2000 , 1<= M <10000 , 1<= K <10000
첫째 줄 : N M K
둘쨰 줄 : N개의 자연수 (1이상 1000이하)





출력 : 가장 큰 수





설계 :
1. 입력 받기
2. 배열 정렬하기
3. 가장 큰 수 k번 더한 후 두 번쨰로 큰 수 1번 더하는 것을 총 M번까지 반복하기
4. 더한 숫자 출력하기





내가 구현한 코드 :

# 1. 입력받기
N,M,K=map(int,input().split())

data =list( map( int,input().split() ) )


# 2. 배열 정렬하기
data.sort(reverse=1)


first=data[0]

second=data[1]



count=0

result=0


# 3. 가장 큰 수 k번 더한 후 두 번쨰로 큰 수 1번 더하는 것을 총 M번까지 반복하기
while True:

    for i in range(K):

        if count==M:
            break

        result+=first
        count+=1


    if count==M:
        break


    result+=second
    count+=1


# 4. 더한 숫자 출력하기

print(result)


피드백 : 가장 큰 수와 두번쨰로 큰 수를 이용하는 것이 그리디 아이디어인 것 같다.
            입력받는 방법 숙지할 것




'''




'''

숫자 카드 게임 설계

문제 : 
숫자가 쓰인 카드들이 N X M 형태로 놓여 있다.
뽑고자하는 행을 선택한 후 그 행에서 가장 작은 카드를 뽑는다.
즉, 각각의 행들이 가지고 있는 가장 작은 카드들 중 가장 큰 카드에 적혀있는 숫자를 출력해야한다.




입력 : 
첫째 줄 N M (1이상 100이하)
둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. (1이상 10000이하) 



  
출력 : 각각의 행들이 가지고 있는 가장 작은 카드들 중 가장 큰 카드에 적혀있는 숫자를 출력




설계 : 
# 1.  n, m 입력 받기
# 2. 'list_input'에 입력받기
# 3. 입력받은 리스트 정렬하기
# 4. 최소값을 "list_n"에 넣기 
# 5. list_input' 초기화하기
# 6. "list_n" 정렬해서 가장 큰 수 출력하기




내가 구현한 코드 :

# 1.  n, m 입력 받기
n,m=map(int,input().split())

list_input=[]
list_reult=[]


for i in range(n):

    list_input=list(map(int,input().split()))  # 2. 'list_input'에 입력받기  
    list_input.sort()                              # 3. 입력받은 리스트 정렬하기
    list_reult.append(list_input[0])          # 4. 최소값을 "list_n"에 넣기 
    list_input=[]                                # 5. list_input' 초기화하기


# 6. "list_n" 정렬해서 가장 큰 수 출력하기    
list_reult.sort(reverse=1)
result=list_reult[0]


print(result)


피드백 : max(), min()함수를 사용해도 괜찮을 것 같다.
           각 행의 최소값을 리스트에 넣는 것이 그리디 아이디어인 것 같다.


'''



'''

1이 될 때까지 설계

문제 : 어떤 수 N이 1이 될떄까지 2가지 연산을 반복한다.
        1. N-1
        2. if(n%k==0) N//k 
연산의 횟수가 최소가 되게 하는 프로그램을 작성해라




입력 : 
첫째 줄 N K (둘다 2이상 십만이하, N>=K)




출력 : 연산 최소횟수 출력




아이디어  :  K^t <= N <= k^t+1 인 t를 찾는다. 
                1연산을 N-K^t번하면 N=K^t이다. 
                따라서 이후에 2연산을 t번한 것이 연산의 최소값이다.
                2연산을 최대한 많이 하고 1연산을 최소한 적게하는 것이 전체 연산의 최소이다.
                즉, N - K^t + t가 연산의 최소값이다.




설계 : 
# 1. N K 입력받기
# 2. 반복문으로 K를 계속 곱하면서 N과 대소 비교를 하고 N이 더 작은 순간의 k를 곱한 횟수를 t에 저장한다.
# 3. N - K^t + t를 출력한다.




내가 구현한 코드 : 



import math

    
n,k = map(int, input().split())  # 1. N K 입력받기

t=1
temp=k


# 2. 반복문으로 K를 계속 곱하면서 N과 대소 비교를 하고 N이 더 작은 순간의 k를 곱한 횟수를 t에 저장한다.

while True:         

    if n==k:
        break

    temp *= k
    t += 1

    if n<temp:
        t-=1
        break
    elif n==temp:
        break


# 3. N - K^t + t를 출력한다.

result= n-math.pow(k,t) +t 

print(int(result))


피드백 : k가 2이상의 자연수이므로 최대한 2연산을 많이 하는 것이 그리디 아이디어인 것 같다.

'''




















