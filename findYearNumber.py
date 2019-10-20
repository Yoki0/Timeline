import re
import os
#from xml.etree.ElementTree import ElementTree,Element  
#import  xml.dom.minidom
from xml.etree import ElementTree as ET




def getString(path):      # you give me path of .xml file, I give you content in file
	per=ET.parse(path)
	p=per.findall('./body/body.content/block')
	inputString = ""
	for oneper in p:
		for child in oneper:
			inputString = inputString + " " + str(child.text)
	return inputString

def matchYear(inputString):      # you give me text, I give you math reulst
	pattern = r"[12][0-9]{3}"    # Years from 1000 to 2999
	match = re.findall(pattern,inputString)
	return match


def getAll():
	f = open("record.txt","w")
	
	totalFiles = 0 
	num = []
	i = 0
	while (i<100):
		num.append(0)
		i += 1
	
	pre_path = "/home/yoki/Desktop/data"
	files= os.listdir(pre_path)
	for file in files:
		totalFiles += 1
		path = pre_path + "/" + file
		inputString = getString(path)
		matchResult = matchYear(inputString)
		number = len(matchResult)
		print(matchResult)
		print(number)
		if number > 1000:
			f.write(path+"\n")
		if number >= 100:
			continue
		num[number] += 1

	print(num)		
	print(totalFiles)
	f.close()


getAll()
