products = []
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

for product in products:
	print(product[0], '的價格是', product[1])

with open('products.csv', 'w', encoding='utf-8') as f: #w是寫入模式，會產生products.txt
	#也會覆蓋原來的products檔
	#f是代表這個txt檔案
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
