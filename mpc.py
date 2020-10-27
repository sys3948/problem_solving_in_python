'''
    프로그래머스 코딩테스트 연습 해시 > 완주하지 못한 선수
'''


def solution(participant, completion):
    # 처음 풀었던 것... 효율성 문제로 실패.
    answer = ''
    for c in completion:
        participant.remove(c)
    
    for p in participant:
        answer += p
    
    return answer


def solution(participant, completion):
    # 효율성 개선
    participant.sort()
    completion.sort()
    for i in range (len(completion)):
        if completion[i] != participant[i]:
            return participant[i]
    return participant[len(participant)-1]


import collections


def solution(participant, completion):
    # 해당 문제의 최상의 풀이법
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]