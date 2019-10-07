
import os
path = "/Users/yuyi/nyt_corpus/data/1996/10/27" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称

for file in files:
	path = "/Users/yuyi/nyt_corpus/data/1996/10/27"
	path = path + "/" + file