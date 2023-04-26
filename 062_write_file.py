# 學習點：
#       open file,list使用,檔案寫入
#       程式碼離開with 檔案自動close, 所以不需要close file指令
#       編碼使用 utf-8 萬國編碼
#       檔案開檔讀取與寫入
#       導入系統import os 檢查檔案狀況

products = []
import os # operation system
file_name = 'products.csv'
if os.path.isfile(file_name):
    print('檔案存在')
    # 讀取檔案
    with open(file_name,'r',encoding='utf-8')as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name,price = line.strip().split(',')
            products.append(([name,price]))
            print(products)
else:
    print('檔案不存在')

# 清單建立
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = int(input('請輸入商品價格：'))
    p=[name,price]
    products.append(p)
# 印出建立清單
for p in products:
    print(p[0],'的價格是',p[1])
# 寫入檔案
with open(file_name,'w',encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0]+','+p[1]+'\n')