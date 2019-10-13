f = open("record.txt","w")
num = [1,2,3,4,5,6,7,8,9,10]
for item in num :
	f.write(str(item)+"\n")


f.close()
