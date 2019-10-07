import re
#from xml.etree.ElementTree import ElementTree,Element  
#import  xml.dom.minidom
from xml.etree import ElementTree as ET

def getString():
	per=ET.parse('0885735.xml')
	p=per.findall('./body/body.content/block')
	inputString = ""
	for oneper in p:
		for child in oneper:
			inputString = inputString + " " + child.text
	return inputString

def matchYear(string):
	pattern = r"[12][0-9]{3}"    # Years from 1000 to 2999
	match = re.findall(pattern,string)
	return match


inputString = getString()
matchResult = matchYear(inputString)
print(matchResult)
print(len(matchResult))