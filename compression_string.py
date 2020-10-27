'''
    문자열을 입력받아서, 같은 문자가 연속적으로 반복되는 경우에 
    그 반복 횟수를 표시하여 문자열을 압축하기.

    입력 예시 : aaabbccca
    출력 예시 : a3b2c3a1
'''


original_str = "aaabbcccaaaaaddddd"
compression_str_list = []
idx = 0
for s in original_str:
    if len(compression_str_list) == 0:
        compression_str_list.append([s, 1])
    else:
        for st in compression_str_list[idx:]:
            if s == st[0]:
                compression_str_list[idx][1] += 1
            else:
                compression_str_list.append([s, 1])
                idx += 1
for csl in compression_str_list:
    print(csl[0]+str(csl[1]), end='')