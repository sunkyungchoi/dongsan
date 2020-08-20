print("♠ 환율 계산기 ♠")
print("")

won = 10000     # 바꾸고 싶은 우리나라 돈
usa = 1128.20   # 달러 환율
jpn = 10.12     # 엔 환율
chn = 171.75    # 위안 환율

print(won, "원을 환전하면?")
print("미국 :", round(won/usa, 2), "달러")
print("중국 :", round(won/chn, 2), "위안")
print("일본 :", round(won/jpn, 2), "엔")

