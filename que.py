'''

문제 회전하는 큐
지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 
지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.

지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

1. 첫 번째 원소를 뽑아낸다. 
   이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.

2. 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.

3. 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.


큐에 처음에 포함되어 있던 수 N이 주어진다. 
그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 
이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

'''


input_num = 0


input_list = []
que_list = [] # 큐
output_num = [] # 추출할 원소 리스트

while input_num < 2:
    if input_num == 0:
        contents = input('순환 큐의 원소 수와 뽑아내려고 하는 원소의 개수를 입력하세요. 입력 예: 큐 크기 원소수 뽑아내려는 원소 개수')
        if len(contents.split(' ')) != 2:
            print('입력을 잘 못 하셨습니다. 다시 입력해주세요.')
            continue
    else:
        contents = input('뽑아내려는 원소 수를 입력해주세요.')
        if len(contents.split(' ')) > int(input_list[0].split(' ')[1]):
            print('뽑아내려는 원소 수의 최대 개수가 초과되었습니다. 뽑으려는 원소 개수는 ' + input_list[0].split(' ')[1] + '개 입니다.')
            continue
    input_list.append(contents)
    input_num += 1

print('입력 값은 다음과 같습니다.')
print(input_list)

for i in range(1, int(input_list[0].split(' ')[0])+1):
    que_list.append(i)

for i in input_list[1].split(' '):
    output_num.append(int(i))

op_two_num = 0
op_three_num = 0
center_num = len(que_list)/2

def op_one():
    # 1. 첫 번째 원소를 뽑아낸다.
    que_list.pop(0)
    output_num.pop(0)
    return True

def op_two(op_two_num):
    # 2. 왼쪽으로 한 칸 이동시킨다.
    num = que_list[0]
    count = 0
    while count < len(que_list)-1:
        que_list[count] = que_list[count + 1]
        count += 1
    que_list[-1] = num
    op_two_num += 1
    return op_two_num

def op_three(op_three_num):
    # 3. 오른쪽으로 한 칸 이동시킨다.
    num = que_list[- 1]
    count = len(que_list) - 1
    while count:
        que_list[count] = que_list[count - 1]
        count -= 1
    que_list[0] = num
    op_three_num += 1
    return op_three_num


while output_num:
    if que_list[0] == output_num[0]:
        op_one()
        center_num = len(que_list)/2
    else:
        if que_list.index(output_num[0]) > center_num:
            # 중심점보다 출력 원소 위치가 높으면 3번 연산
            print('3번 연산 진행')
            op_three_num = op_three(op_three_num)
        else:
            print('2번 연산 진행')
            op_two_num = op_two(op_two_num)

print('Result : ' + str(op_two_num + op_three_num))
