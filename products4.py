import os # operating system，OS模組，有更大權力，不用上網下載
products = []
if os.path.isfile('products.csv'): #電腦資料夾有沒有這個檔
#os的path模組的isfile功能
	print('yeah!找到檔案了！')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			#continue是跳出本次for迴圈，跳到下一回，
			#而剩下的二行也是本迴圈，也要跳過
			#break是跳出整個迴圈
			name, price = line.strip().split(',')
			#先用strip去掉\n換行，再用split以逗點切割字串
			#把姓名(第一項)存在name, 價格(第二項)存在price
			#這是簡化的寫法
			products.append([name, price])
	print(products)
else:
	print('找不到檔案…哭哭')


#讓使用者輸入

while True:
	name = input('請輸入商品名稱')
	if name == 'q':
		break
	price = input('請輸入商品價格')

	#p = []
	#p.append(name)
	#p.append(price)#可以簡化成 p = [name, price]
	#products.append(p) 
	products.append([name, price])
print(products)

#印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案

with open('products.csv', 'w', encoding='utf-8') as f: #w是寫入模式，會產生products.txt
	#也會覆蓋原來的products檔
	#f是代表這個txt檔案
	#csv用excel開仍有亂碼，須excel，資料匯入，文字csv，選字碼
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
