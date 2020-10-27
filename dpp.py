'''
    다음 입사문제 중에서
    1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 
    함수를 작성하시오.(단 점들의 배열은 모두 정렬되어있다고 가정한다.)
'''

dot_point = [1, 2, 3, 4, 8, 13, 17, 20]
dict_dot_point = dict()
min_num = 0

for i in range(len(dot_point) - 1):
    dict_dot_point[-(dot_point[i] - dot_point[i + 1])] = (dot_point[i], dot_point[i + 1])

print(dict_dot_point.get(min(dict_dot_point.keys())))
