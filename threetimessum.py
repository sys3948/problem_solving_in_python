'''
디지털 시계에 하루동안(00:00~23:59) 3이 표시되는 시간을 초로 환산하면 총 몇 초(second) 일까요?

디지털 시계는 하루동안 다음과 같이 시:분(00:00~23:59)으로 표시됩니다.

00:00 (60초간 표시됨)
00:01 
00:02 
...
23:59

00:00 ~ 23:59까지의 3이라고 입력된 시간의 유지시간(60초)의 총 합을 구하시오.
'''

total_sec = 0
for i in range(24):
    for j in range(60):
        if "3" in str(i) or "3" in str(j):
            total_sec += 60

print(total_sec)