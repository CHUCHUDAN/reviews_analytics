data=[]
sum = 0
with open("reviews.txt","r") as f:
	for line in f:
		data.append(line)
	for oo in data:
		n = len(oo)
		sum += n

print("每筆平均資料長度是", sum/len(data))
	
new = []
for d in data:
	if len(d) < 100:
		new.append(d)

print("一共有", len(new), "筆小於100的資料")
	
print(new[0])
print(new[1])