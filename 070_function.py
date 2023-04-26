# 070_function.py
# function建立
# 學習點：
#       function：函式/功能 是用來【收納】程式碼
#       def function(parameter):
#       參數有預設值時就不一定要設定
#   理想的function應該只做一件事，重構程式的核心概念就是把程式碼不斷改寫，寫成越來越小的function
#   讓function儘量只做一件事
#   程式最好有main() function為程式的進入點 (refactor)
def wash(dry = False,water = 8):
    print('加水',water,'分滿')
    print('加洗衣精')
    print('旋轉')
    if dry:
        print('烘衣')
wash()
print('-----------')
wash(True)
print('-----------')
wash(6)
print('-----------')
wash(True,6)
print('-----------')
wash(dry = True)
print('-----------')
wash(water = 6)

#函數回傳值
list1 = [2,5,8]
def avg(number):
    return sum(number) / len(number)
print(avg(list1))


import os # operation system
# 讀取檔案
def read_file(file_name):
    products = []
    with open(file_name,'r',encoding='utf-8')as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name,price = line.strip().split(',')
            products.append(([name,price]))
    return products
# 清單建立
def user_input(products):
    while True:
        name = input('請輸入商品名稱：')
        if name == 'q':
            break
        price = int(input('請輸入商品價格：'))
        p=[name,price]
        products.append(p)
    return products
# 印出建立清單
def print_products(products):
    for p in products:
        print(p[0],'的價格是',p[1])
# 寫入檔案
def write_file(file_name,products):
    with open(file_name,'w',encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0]+','+str(p[1])+'\n')
def main():
    products = []
    file_name = 'products.csv'
    if os.path.isfile(file_name):
        products = read_file(file_name)
    else:
        print('檔案不存在')
    products = user_input(products) #增加新產品
    print_products(products)
    write_file(file_name,products)
main()