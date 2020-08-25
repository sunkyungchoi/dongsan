import turtle as t

t.shape("turtle")   # 거북이 모양
t.color("hotpink")  # 선 색깔
t.pensize(5)        # 선 굵기

# 사각형 그리기
for x in range(4):
    t.forward(100)
    t.left(90)

