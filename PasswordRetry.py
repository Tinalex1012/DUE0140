# 猜密碼遊戲，三次錯誤跳出迴圈
# 學習點：
#       輸出入、while迴圈(while,break,continue)、if 的使用

password = 'a123456' #初始答案
cnt = 3 # 剩餘機會
while True:
    pwd = input('請輸入密碼：')
    if pwd.strip() == '':
        continue
    elif pwd == password:
        print('登入成功')
        break
    else:
        cnt -= 1
        if cnt == 0:
            print('沒機會了，結束')
            break
        print('輸入錯誤，你還有',cnt,'次機會')