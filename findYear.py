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
			inputString = inputString + " " + child.text
	return inputString

def matchYear(inputString):
	pattern = r"[12][0-9]{3}"    # Years from 1000 to 2999
	match = re.findall(pattern,inputString)
	return match


def getAll():
	pre_path = "/Users/yuyi/data"
	files= os.listdir(pre_path)
	for file in files:
		path = pre_path + "/" + file
		inputString = getString(path)
		matchResult = matchYear(inputString)
		print(matchResult)
		print(len(matchResult))
		print()


getAll()
