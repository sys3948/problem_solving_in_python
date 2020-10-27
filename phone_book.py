'''
전화번호 목록

전화번호부에 적힌 전화번호 중, 
한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다. 

전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421

전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록
solution 함수를 작성해주세요.
'''


# 문제 풀은 본인 코드
def solution(phone_book):
    phone_book.sort()
    answer = True
    break_check = False
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            '''
            try:
                if phone_book[j].index(phone_book[i]) == 0:
                    answer = False
                    break_check = True
            except ValueError:
                continue
            '''
            if phone_book[i] in phone_book[j]:
                if phone_book[j].index(phone_book[i]) == 0:
                    answer = False
                    break_check = True
        if break_check:
            break
    return answer


# 깔끔한 코드
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True