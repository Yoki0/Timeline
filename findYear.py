import re
import os
#from xml.etree.ElementTree import ElementTree,Element  
#import  xml.dom.minidom
from xml.etree import ElementTree as ET




def getString(path):
	per=ET.parse(path)
	p=per.findall('./body/body.content/block')
	inputString = ""
	for oneper in p:
		for child in oneper:
			inputString = inputString + " " + str(child.text)
	return inputString

def matchYear(inputString):
	pattern = r"[12][0-9]{3}"    # Years from 1000 to 2999
	match = re.findall(pattern,inputString)
	return match


def getAll():
	totalFiles = 0 
	num = [0,0,0,0,0,0,0,0,0,0,0]
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
		if number <= 3:
			num[0] += 1
		elif number <= 6:
			num[1] += 1
		elif number <= 9:
			num[2] += 1
		elif number	<= 12:
			num[3] += 1 
		elif number <= 15:
			num[4] += 1
		elif number <= 18:
			num[5] += 1 
		elif number <= 21:
			num[6] += 1
		elif number <= 24:
			num[7] += 1
		elif number <= 27:
			num[8] += 1
		elif number <= 30:
			num[9] += 1
		else :
			num[10] += 1

		if number > 40:
			print()
			print()
			print(path)
			print()
			print()



	print(totalFiles)
	print("0-3:",num[0])
	print("3-6:",num[1])
	print("6-9:",num[2])
	print("9-12:",num[3])
	print("12-15:",num[4])
	print("15-18:",num[5])
	print("18-21:",num[6])
	print("21-24:",num[7])
	print("24-27",num[8])
	print("27-30",num[9])
	print("more than 30:",num[10])


getAll()
