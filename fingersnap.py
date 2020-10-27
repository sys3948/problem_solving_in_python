'''
타노스는 프로그램의 균형을 위해서는 리스트의 원소 절반을 무작위로 삭제해야 한다고 믿고 있다.

타노스가 손가락을 튕겼을 때(프로그램을 실행했을 때) 입력된 리스트에서 절반의 원소를 무작위로 
삭제하여 리턴하는 인피니티 건틀렛 프로그램을 작성하시오.

(무작위 삭제이므로 입력값이 같아도 출력값이 매번 달라야 합니다)

입력 예시

[2, 3, 1, 6, 5, 7]
출력 예시 1

[2, 5, 7]
출력 예시 2

[3, 6, 5]
참고: 리스트의 원소가 홀수개일 경우 절반의 확률로 절반보다 많은 원소가 삭제되거나 
절반보다 적은 원소가 삭제되어야 합니다.

(만약 리스트의 원소가 7개라면 절반의 확률로 3개 또는 4개의 원소가 삭제됨)
'''

from random import *

input_li = [5, 6, 10, 3, 4, 8, 15]

snap_count = len(input_li)//2

for i in range(snap_count):
    delete_num = randrange(len(input_li))
    input_li.pop(delete_num)

print(input_li)


'''
위의 풀이의 입력 값이 홀수 일 경우 절반의 확률로 짝수 또는 홀수의 원소가 삭제되지 않는 문제가 발생
추천 수 많은 풀이.
import random as rd
def delete_half(x):
    rd.shuffle(x)
    t = len(x)//2
    if len(x) % 2 and rd.random() < 0.5: t += 1
    return x[:t]
'''




