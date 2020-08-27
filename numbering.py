'''
각 숫자의 개수를 구하기!
수의 자리마다 있는 1 ~ 9까지의 개수를 구한다!
수는 1 ~ 1000까지~
'''

num_dict = {}
for i in range(0, 10):
    num_dict[str(i)] = 0

for i in range(1, 1001):
    for j in str(i):
        if num_dict[j] == 0 or num_dict[j]:
            num_dict[j] = num_dict[j] + 1

for i in num_dict:
    print(str(i) + " : " + str(num_dict[i]) + "개", end=', ')