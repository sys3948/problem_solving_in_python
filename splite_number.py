'''
10~1000까지 각 숫자 분해하여 곱하기의 전체 합 구하기

예로, 10~15까지의 각 숫자 분해하여 곱하기의 전체 합은 다음과 같다.

10 = 1 * 0 = 0
11 = 1 * 1 = 1
12 = 1 * 2 = 2
13 = 1 * 3 = 3
14 = 1 * 4 = 4
15 = 1 * 5 = 5

그러므로, 이 경우의 답은 0+1+2+3+4+5 = 15

'''
mu_sum = 1
min_num = 10
max_num = 15

for i in range(min_num,max_num + 1):
    for j in str(i):
        mu_sum = mu_sum * int(j)
    sum += mu_sum
    mu_sum = 1

print(sum)


# li_s = [[int(j) for j in str(i)] for i in range(min_num, max_num + 1)]

# print(li_s)