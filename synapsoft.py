'''
  주어진 문자열(공백 없이 쉽표로 구분되어 있다.)을 가지고 아래 문제에 대한 프로그램을
  작성하세요.

  주어진 문자열
  이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,
  박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌

  문제
   1. 김씨와 이씨는 각각 몇 명인가요?
   2. "이재영"이란 이름이 몇 번 반복되나요?
   3. 중복을 제거한 이름을 출력하세요.
   4. 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
'''

def all_p(name_str):
    one_count = 0
    two_count = 0
    for i in name_str:
        if i[0] == '김' or i[0] == '이':
            one_count += 1
        if i == "이재영":
            two_count += 1

    remove_duplicate_name = set(name_str)
    sort_remove_duplicate_name = list(remove_duplicate_name)
    sort_remove_duplicate_name.sort()

    return one_count, two_count, remove_duplicate_name, sort_remove_duplicate_name


if __name__ == "__main__":
    name_str = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"

    one_result, two_result, three_result, four_result = all_p(name_str.split(','))

    print("1 번 문제 김씨와 이씨는 각각 몇 명인가요? ", one_result)
    print("2 번 문제 '이재영'이란 이름이 몇 번 반복되나요? ", two_result)
    print("3 번 문제 중복을 제거한 이름을 출력하세요. ", three_result)
    print("4 번 문제 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요. ", four_result)
