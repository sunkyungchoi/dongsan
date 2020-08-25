import turtle as t
import random

# 그래픽 설정하기
t.color("orange")
t.speed(0)

for i in range(50):
    # 무작위 x, y 위치 정하기
    x = random.randint(-400, 400)
    y = random.randint(-300, 300)
    
    # 펜 올리고(그리지 않고) 이동
    t.penup()
    t.goto(x, y)

    # 펜 내리고 그리기
    t.pendown()
    t.circle(50)
    



