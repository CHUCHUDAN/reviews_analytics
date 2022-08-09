data=[]
count = 0
with open("reviews.txt","r") as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
# print("檔案讀取完了,總共有",len(data),"筆資料")
# print(data[0])

wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
			
		else:
			wc[word] = 1

for word in wc:
	if wc[word] >= 1000000:
		print(word,wc[word])

print(len(wc))
print(wc["Daniel"])

while True:
	word = input("想查詢甚麼字?: ")
	if word == "q":
		break
	if word in wc:
		print(word,"出現過",wc[word],"次")
	else:
		print("資料中沒這個字")

print("感謝您使用本查詢系統")






# sum_len = 0
# for d in data:
# 	n = len(d)
# 	sum_len += n
		
# print("每筆平均資料長度是", sum_len/len(data))


	
# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)

# print("一共有", len(new), "筆小於100的資料")

# good = []
# for d in data:
# 	if "good" in d:
# 		good.append(d)

# print(len(good))