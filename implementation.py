


'''


상하좌우 설계

문제 :
가장 왼쪽 위 좌표 (1, 1)
가장 오른쪽 아래 좌표 (N, N)
A는 상하좌우로 움직일 수 있고 시작 좌표는 (1, 1)이다.
A가 N x N 범위를 벗어나는 움직임은 무시된다.
LRUD 중 하나의 문자가 반복적으로 적혀있는 계획서대로 움직인다.

입력 :
첫째 줄 N (1이상 100이하)
둘째 줄 계획서 (1이상 100이하)

출력 : x y

아이디어 : 리스트를 N*N 길이로 선언해서 나눈 몫과 나머지를 이용하여 행과 열을 표현하자. 몫=행, 나머지=열
              temp 좌표와 current 좌표를 추가해서 temp좌표가 범위를 벗어나지 않았으면 갱신
              상하좌우에 맞는 이동함수를 만든다. 범위를 벗어났는지 확인하는 함수를 만든다.



설계 :
# 1. 입력 받기
# 2. 이동 함수 만들기
# 3. 범위 함수 만들기
# 4. 조건문으로 4가지 경우의 수 만들기
# 5. 경우의 수에 맞게 temp 좌표 조정하기
# 6. temp 좌표가 범위 내에 있는지 확인하기
# 7. 범위 내에 있으면 current 좌표 갱신하기
# 8. 계획서 횟수만큼 반복하기

내가 구현한 코드 :


N=int(input()) # 1. 입력 받기

plan=list(input().split())

plan.reverse()



def move(direction): # 2. 이동 함수 만들기



    if direction=='L': # 4. 조건문으로 4가지 경우의 수 만들기

        return_value=[0,-1]

        return return_value



    elif direction == 'R':

        return_value = [0, 1]

        return return_value



    elif direction == 'U':

        return_value = [-1, 0]

        return return_value

    else :

        return_value = [1, 0]

        return return_value



def range_function(x_y_list,n): # 3. 범위 함수 만들기



    if(x_y_list[0]>=1 and x_y_list[0]<=n and x_y_list[1]>=1 and x_y_list[1]<=n):



        return True

    else :

        return False



temp_xy=[1,1]



current_xy=[1,1]



x=0

y=0



for i in range(len(plan)):    # 8. 계획서 횟수만큼 반복하기



    direction = plan.pop()



    x=move(direction)[0]

    y=move(direction)[1]



    temp_xy[0]+=x          # 5. 경우의 수에 맞게 temp 좌표 조정하기

    temp_xy[1]+=y



    flag=range_function(temp_xy,N)    # 6. temp 좌표가 범위 내에 있는지 확인하기



    if(flag==True):            # 7. 범위 내에 있으면 current 좌표 갱신하기

        current_xy=temp_xy

    else:

        temp_xy[0] -= x

        temp_xy[1] -= y



print(current_xy[0],current_xy[1])

피드백 : 범위를 벗어났다면 temp의 위치도 원상복구 시켜줘야한다.
           굳이 나눈 몫과 나눈 나머지를 이용하지 않아도 된다.
           연산은 2000만번을 초과하지 않으므로 시간 제한은 신경쓸 필요가 없다.
           일련의 명령에 따라서 개체를 차례대로 이동시킨다는 점에서
           시뮬레이션 유형으로 분류되며 구현이 중요한 대표적인 문제 유형이다.

dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L', 'R', 'U', 'D']


위와 같은 방식으로 구현하는 것이 나중에 명령의 경우의 수가 많아졌을 때 덜 혼동될 것 같다.


'''










'''

시각 설계

문제 : 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 
         3이 하나라도 포함되어있는 경우의 수를 구하는 프로그램을 작성하시오

입력 : 첫째줄 N (0이상 23이하)

출력 : 경우의 수 출력

아이디어 : 1시간에 3 포함되는 경우의 수를 구하여 N을 곱한다.

              시 : 03, 13 ,23 

              분 : 03, 13, 23, 30, 31, 
                    32, 33, 34, 35, 36, 
                    37, 38, 39, 43, 53 (15)

              초 : 03, 13, 23, 30, 31, 
                    32, 33, 34, 35, 36, 
                    37, 38, 39, 43, 53 (15)
             
            
             03, 13, 23 : 60*60 = 3600         
             나머지 : 15*60 + 45*15 = 1575
             ex) 5이면 1575*5 + 3600 = 11475

설계 : 
1. 입력 받기
2.  03시 13시 23시에는 3600을 더하고 이외의 시에는 1575를 더한다.
3 .출력한다.

내가 구현한 코드 :

N=int(input())  # 1. 입력 받기

# 2.  03시 13시 23시에는 3600을 더하고 이외의 시에는 1575를 더한다.
if N<3: 
    result = (N+1)*1575 

elif N>=3 and N<13 : 
    result= N*1575 + 3600

elif N>=13 and N<23 : 
    result= (N-1)*1575 +3600*2 

elif N==23: 
    result= (N-2)*1575 +3600*3 

print(result)
 

저자의 완전 탐색 구현 :

N=int(input()) 

count=0 

for i in range(N+1): 
    for j in range(60): 
        for k in range(60): 
            if '3' in str(i)+str(j)+str(k): 
                count+=1 
print(count)



피드백 : 
되도록이면 수학적 계산보다는 컴퓨터의 빠른 연산을 이용한 단순한 방법을 이용해라
수학적인 방법은 휴먼에러를 발생시킬 확률이 높다. 
그냥 반복문 3개를 겹쳐서 단순하게 하는 것이 휴먼 에러가 안날 확률이 가장 높다.

3중 반복문을 돌면서 모든 경우의 수에 대해서 3이 들어간 수를 카운팅하는 방식이 완전탐색이다.





'''


'''

왕실의 나이트 설계

문제 : 8*8 좌표 평면상에서 나이트의 위치가 주어졌을 때 
        나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오 
        나이트는 좌표평면 상에서 벗어날 수 없고 
        수직으로 2칸 수평으로 1칸 또는 수직으로 1칸 수평으로 2칸 이동할 수 있다.
        최대 8가지 이동경로가 존재한다.

입력 : 
첫쨰줄에 좌표가 주어진다. ex) "a1"

출력 : 경우의 수 출력

아이디어 : 
완전탐색과 구현으로 이루어진 유형인듯 하다. (유형파악)
8가지의 경우의 수가 있고 이 경우의 수가 범위를 벗어났지 확인하는 함수를 만들자           
상하좌우에서의 이동경로 방식을 구현해보자

설계 : 
# 1. 입력받기
# 2. 입력받은 문자 해석하기 첫번째 글자 열 두번쨰글자 행
# 3. 좌표가 범위를 벗어났는지 확인해주는 함수 구현
# 4. 8가지 경우의 확인하면서 카운트하기
# 5. 카운트 출력하기


내가 구현한 코드 : 

n=input()          # 1. 입력받기


def change_num(col):              # 문자를 숫자로 바꾸는 함수 구현
    if col == 'a': 
        return 1 
    elif col == 'b': 
        return 2 
    elif col == 'c': 
        return 3 
    elif col == 'd': 
        return 4 
    elif col == 'e': 
        return 5 
    elif col == 'f': 
        return 6 
    elif col == 'g': 
        return 7 
    elif col == 'h': 
        return 8 

col = int(change_num(n[0]))          # 2. 입력받은 문자 해석하기 첫번째 글자 열 두번쨰글자 행
row = int(n[1]) 


def check_TF(row,col):          # 3. 좌표가 범위를 벗어났는지 확인해주는 함수 구현

    if row<1 or row>8 or col<1 or col>8 : 
        return False 
    else : 
        return True 

direction_row=[-2,-2,2,2,-1,-1,1,1] 
direction_col=[1,-1,1,-1,2,-2,2,-2] 

count=0 

# 4. 8가지 경우의 확인하면서 카운트하기

for i in range(len(direction_row)): 
    if check_TF(row+direction_row[i],col+direction_col[i])==True: 
        count+=1 

print(count)              # 5. 카운트 출력하기


피드백 : 
ord() 함수를 이용해서 문자의 아스키코드 값을 얻을 수 있다.
이 ord() 함수를 이용하면 굳이 changE_num 이라는 함수를 구현 안해도 된다.           
이번 저자는 리스트에 튜플을 담아서 이동방향을 기록하였다. 
저자는 두가지 형태 모두 자주 사용되므로 참고하라고 한다.

'''



'''

게임 개발 설계


문제 : 
NxM 크기의 직사각형으로 각각의 칸은 육지와 바다이고
캐릭터는 동서남북 중 한 곳을 바라본다.
맵 각각의 칸은 (A,B)로 나타내고 북쪽과 서쪽으로부터 떨어진 칸의 개수이다.
캐릭터는 상하좌우로 움직일 수 있고 바다로 되어 있는 공간에는 갈 수 없다.

1. 현재위치 현재방향을 기준으로 왼쪽방향부터 차례대로 갈 곳을 정한다.
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면 
왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
왼쪽방향에 아직 가보지 않은 칸이 존재하지 않는다면 
왼쪽으로 방향만 회전하고 1단계로 돌아간다.
3. 만약 4방향 모두 가본 칸이거나 바다로 되어있는 경우 
바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
단 뒤쪽이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

위의 3가지 메뉴얼에 따라 이동시킨 후 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 작성하라

입력 :
1. N M [3,50]
2. A B 처음 바라보는 방향(n:0 e:1 s:2 w:3) 시계방향
3~3+N. NXM 모양형태로 바다1인지 육지0인지 정보가 주진다.

출력 : 
캐릭터가 방문한 칸 수를 출력

아이디어 :
방문한 곳을 체크하기위한 리스트를 하나 더 만든다.

왼쪽방향에 가보지 않은 칸이 있는지 없는지 확인하는 함수를 만들기
왼쪽방향으로 회전하는 함수 만들기
1칸 앞으로 가는 함수 만들기
4방향이 가본 칸이거나 바다인칸인 경우를 분별하는 함수 만들기
바라보는 방향은 유지한채로 한 칸 뒤로 가는 함수 만들기
뒤쪽이 바다인 칸인지 확인하는 함수 만들기

설계 :
1. 입력받기
2. 왼쪽방향에 가보지 않은 칸이 있는지 없는지 확인하는 함수1를 만들기
3. 왼쪽방향으로 회전하는 함수2 만들기
4. 1칸 앞으로 가는 함수3 만들기
5. 4방향이 가본 칸이거나 바다인 칸인 경우를 분별하는 함수4 만들기
6. 바라보는 방향은 유지한채로 한 칸 뒤로 가는 함수5 만들기
7. 뒤쪽이 바다인 칸인지 확인하는 함수6 만들기

8. 무한 루프를 건다.
9. 조건문의 조건으로 함수1을 설정하고 조건에 해당하면 함수2 함수3을실행한다.
조건에 해당하지 않으면 함수2만 실행한다.
10.9 번을 반복한다.
11. 함수4 가 True이면  함수6이 True인지 확인하고 True이면 멈추고 break하고 False이면 함수5를 실행시킨다.

내가 구현한 코드 :



 

n_row,m_col=map(int,input().split())

 

current_row, current_col, current_dir =map(int,input().split())

 

map_array=[]

check_array=[]

 

for i in range(n_row):

 

    if i==0 :

        check_list = []

        for j in range(m_col+2):

            check_list.append(100)

        map_array.append(check_list)

 

    check_list=list(map(int,input().split()))

    check_list.reverse()

    check_list.append(100)

    check_list.reverse()

    check_list.append(100)

 

    map_array.append(check_list)

 

    if i==n_row-1 :

        check_list = []

        for j in range(m_col+2):

            check_list.append(100)

        map_array.append(check_list)

 

# for i in range(n_row+2):

#     print(map_array[i])

 

 

def func1(row,col,dir):

 

    when_north=(0,-1)

    when_east=(-1,0)

    when_south=(0,1)

    when_west=(1,0)

 

 

    if dir==0: #가보지 않았으면 트루

 

        if map_array[row+when_north[0]][col+when_north[1]]==0 :

            return True

        else :

            return False

    elif dir==1:

        if map_array[row+when_east[0]][col+when_east[1]]==0 :

            return True

        else :

            return False

    elif dir==2:

        if map_array[row+when_south[0]][col+when_south[1]]==0 :

            return True

        else :

            return False

    elif dir==3:

        if map_array[row+when_west[0]][col+when_west[1]]==0 :

            return True

        else :

            return False

 

 

def func2(dir):

    if dir-1<0:

        return 3

    else:

        return dir-1

 

 

def func3(row,col,dir): #앞으로 한칸이동한 좌표 반환

    when_north = (-1, 0)

    when_east = (0, 1)

    when_south = (1, 0)

    when_west = (0, -1)

 

    if dir==0:

        return row+when_north[0],col+when_north[1]

    elif dir==1:

        return row+when_east[0],col+when_east[1]

    elif dir==2:

        return row+when_south[0],col+when_south[1]

    else:

        return row+when_west[0],col+when_west[1]

 

 

def func4(row, col): #4방향이 가본칸이거나 바다인경우 트루 반환

    when_north = (-1, 0)

    when_east = (0, 1)

    when_south = (1, 0)

    when_west = (0, -1)

 

    if map_array[row+when_north[0]][col+when_north[1]]==0 :

 

        return False

    elif map_array[row+when_east[0]][col+when_east[1]]==0 :

        return False

 

    elif map_array[row+when_south[0]][col+when_south[1]]==0 :

        return False

 

    elif map_array[row+when_west[0]][col+when_west[1]]==0 :

        return False

    else:

        return True

 

def func5(row,col,dir): # 뒤로 한칸 이동한 좌표 반환

    when_north = (1, 0)

    when_east = (0, -1)

    when_south = (-1, 0)

    when_west = (0, 1)

 

    if dir == 0:

        return row + when_north[0], col + when_north[1]

    elif dir == 1:

        return row + when_east[0], col + when_east[1]

    elif dir == 2:

        return row + when_south[0], col + when_south[1]

    else:

        return row + when_west[0], col + when_west[1]

 

 

 

def func6(row,col,dir): #뒤쪽이 바다인 칸이면 트루 반환

    when_north = (1, 0)

    when_east = (0, -1)

    when_south = (-1, 0)

    when_west = (0, 1)

 

    if dir == 0:

 

        if map_array[row + when_north[0]][col + when_north[1]] == 1:

            return True

        else:

            return False

    elif dir == 1:

        if map_array[row + when_east[0]][col + when_east[1]] == 1:

            return True

        else:

            return False

    elif dir == 2:

        if map_array[row + when_south[0]][col + when_south[1]] == 1:

            return True

        else:

            return False

    elif dir == 3:

        if map_array[row + when_west[0]][col + when_west[1]] == 1:

            return True

        else:

            return False

 

count=0

 

while True:

 

    if func4(current_row,current_col):

        if func6(current_row,current_col,current_dir):

            break

        else:

            current_row,current_col=func5(current_row,current_col,current_dir)

 

    if func1(current_row,current_col,current_dir):

        current_dir=func2(current_dir)

        current_row,current_col=func3(current_row,current_col,current_dir)

        count+=1

        map_array[current_row][current_col]=100

    else:

        current_dir = func2(current_dir)

 

 

 

print(count)

피드백 : 
맵의 테두리를 고려하지 않아서 코드가 설계와는 다르게 조금 꼬였다.
그래도 기능들을 모듈화 해놓아서 금방 재설계 할 수 있었다.
아마 테스트 케이스를 여러개 넣어보지 않았다면 찾지 못했을 것이다.
설계부터 테스트 케이스를 넣을 수 있다면 넣어보는 습관을 들여야겠다.

파이썬에서는 2차원 배열을 구현할때 리스트안에 리스트를 넣는다.
2차원 배열값을 입력받는 방식을 숙지해라

d=[[0]*m for _in range(n)] 
이 코드를 숙지둘 것

<저자가 말하는 문제풀이를 위한 중요한 테크닉>

일반적으로 방향을 설정해서 이동하는 문제 유형에서는 
dx, dy라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적이라고한다.

      북 동 남 서
dx=[-1,  0,  1,  0]
dy=[ 0,  1,  0, -1]

나는 해당 함수마다 해당 방향에 따라 움직여야하는 숫자를 정의했는데
위의 방식이 좀 더 효율적인 것 같다.

북쪽방향일 때 뒤로 이동하려면 row-dx[0] , col-dy[0] 해주면 되서 편한 것 같다.

'''













