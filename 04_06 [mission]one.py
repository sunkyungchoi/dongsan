import turtle as t
 
# 색상 지정하기
t.color("orange")
t.pensize(5)

# 별 그리기
for x in range(5):
    t.forward(100)
    t.right(144)
    
# 오각형
t.left(36)
for x in range(5):
    t.forward(60)
    t.right(72)


