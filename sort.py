

n=int(input())

input_list=[]


for i in range(n):
    input_value=int(input())
    input_list.append(input_value)

input_list.sort(reverse=1)

for i in range(len(input_list)):
    print(input_list[i],end=' ')

