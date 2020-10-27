'''
    완전수 구하기.
    자기 자신을 제외한 모든 양의 약수들의 합이 자기 자신이 되는 자연수를 완전수라고 한다.
    입력한 값이 완전수인지를 확인하는 프로그램을 작성하라.
'''


num = 16 # 입력한 수
perfect_num = {}
measure = [] # 입력한 수의 약수
sum_num = 0 # 약수들을 더한 값



for i in range(1, num):
    if num%i == 0:
        measure.append(i)

measure = set(measure)

for i in measure:
    sum_num += i


if num == sum_num:
    print("%d 는 완전수 입니다." %num)
else:
    print("%d 는 완전수가 아닙니다." %num)
