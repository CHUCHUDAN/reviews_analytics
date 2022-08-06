data=[]
sum = 0
with open("reviews.txt","r") as f:
	for line in f:
		data.append(line)
	for oo in data:
		n = len(oo)
		sum += n

print("每筆平均資料長度是", sum/len(data))
	

	
