import turtle as t
import random

# 그래픽 설정하기
t.color("sky blue")
t.pensize(5)
t.speed(0)

for y in range(40, 240, 40):
    # 펜 올리고(그리지 않고) 이동
    t.penup()
    t.goto(0, -y)

    # 펜 내리고 그리기
    t.pendown()
    t.circle(y)
    



