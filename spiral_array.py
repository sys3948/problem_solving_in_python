'''
  Spiral Array
  6 6이라는 값을 입력한다면. 6x6 크기의 매트릭스에 나선형 회전을 한 값을 출력한다.
  나선형 회전을 한 값의 예
  0, 1, 2, 3, 4, 5
  19, 20, 21, 22, 23, 6
  18, 31, 32, 33, 24, 7
  17, 30, 35, 34, 25, 8
  16, 29, 28, 27, 26, 9
  15, 14, 13, 12, 11, 10
'''

array = [[ '.' for i in range(5)]] * 5
x = 0
y = 0
max_count = 9
count = 0
num = 0

while count < max_count:
    for i in range(5):
        array[y][x] = num
        if count%2 == 0:
            if count % 4 == 0:
                x += 1
                num +=1
            else:
                x -= 1
                num +=1
        else:
            if (count + 1) % 4 == 0:
                y += 1
                num +=1
            else:
                y -= 1
                num +=1

    count += 1
                