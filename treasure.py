'''
문제
옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다. 
이 나라의 국왕 김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다.

길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.

S = A[0]×B[0] + ... + A[N-1]×B[N-1]

S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.

S의 최솟값을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. 
둘째 줄에는 A에 있는 N개의 수가 순서대로 주어지고, 셋째 줄에는 B에 있는 수가 순서대로 주어진다. 
N은 50보다 작거나 같은 자연수이고, A와 B의 각 원소는 100보다 작거나 같은 음이 아닌 정수이다.

출력
첫째 줄에 S의 최솟값을 출력한다.
'''

# 처음 풀었던 답(틀린 답)
input_li = []

num = input('정수 배열의 길이를 입력해주세요.')

i = 0
while i < 2:
    contents = input('값을 입력해주세요.')
    if len(contents.split(' ')) != int(num):
        print('값의 개수가 맞지 않습니다. 입력할 값으 수는 ' + num + '개 입니다. 다시 입력해주세요.')
        continue

    input_li.append([int(c) for c in contents.split(' ')])

    i+=1

print(input_li)

result = 0

while input_li:
    result += min(input_li[0]) * max(input_li[1])
    input_li[0].pop(input_li[0].index(min(input_li[0])))
    input_li[1].pop(input_li[1].index(max(input_li[1])))

    if not input_li[0]:
        break

print(result)

# 맞은 정답. 이해 안감.
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse = True)

result = 0

for n,m in zip(A,B):
    result += n * m

print(result)