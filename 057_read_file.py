# 留言分析程式
# 學習點：
#       open file, 清單篩選

# 清單讀取建立
data = []
file_name = 'reviews.txt'
with open(file_name,'r') as f: #開啟檔案，讀取模式
    for line in f:
        data.append(line)
print('檔案讀取完畢，一共有',len(data),'筆留言')
# 清單篩選
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有',len(new),'筆留言長度小於100')
good = []
# for d in data:
#     if 'good' in d:
#         good.append(d)
good = [d for d in data if 'good' in d] #快寫法 list comprehension
# output = [(number-1) for number in reference if number %2 == 0]
#              運算          變數        清單          篩選條件
bad = ['bad' in d for d in data]

print('一共有',len(good),'筆留言中提到good')

