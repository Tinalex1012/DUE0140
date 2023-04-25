# 047_guess_number
# 猜數字遊戲
# 學習點：
#       import random
import random
min_n, max_n = map(int,input('請輸入起始值和結束值（空格分開）:').split())
cnt = 0
ans = random.randint(min_n,max_n) # 整數亂數種子
while True:
    cnt += 1
    guess_num = int(input('請輸入數字 '+str(min_n) +"~"+ str(max_n)+ " ："))
    if guess_num == ans:
        print('用了',cnt,'次機會，你答對了！')
        break
    elif guess_num > ans:
        max_n = guess_num
        print('猜錯了，答案小於',guess_num)
    elif guess_num < ans:
        min_n = guess_num
        print('猜錯了，答案大於',guess_num)
    else:
        print('答案介於',min_n,'~',max_n,'之間')