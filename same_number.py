'''
  앞 뒤가 같은 수
  앞 뒤가 같은 수는 바로 쓴 값고 거꾸로 쓴 값이 같은 수이다. 
  다음과 같은 예를 들 수 있다.

  입력 : 1
  출력 : 0

  입력 : 4
  출력 : 3
  
  입력 : 30
  출력 : 202
'''


n = input('몇 번째의 같은 수를 찾으시겠습니까? > ')

n = int(n)

value = 0
count = 1


while True:
    check = True
    if len(str(value)) > 1:
        if str(value)[0] == str(value)[-1]:
            for i in range(len(str(value))//2):
                if str(value)[i] != str(value)[-1-i]:
                    check = False
                    break

            if check:
                if count == n:
                    print("입력 : " + str(n) + " 출력 : " + str(value))
                    break
                count += 1
        
    else:
        if count == n:
            print("입력 : " + str(n) + " 출력 : " + str(value))
            break
        count += 1
    value += 1
