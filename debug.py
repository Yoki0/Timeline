#coding=utf-8
from xml.etree import ElementTree as ET
per=ET.parse('test.xml')
p=per.findall('./body/body.content/block')

inputString = ""
for oneper in p:
    for child in oneper:
        inputString = inputString + " " + child.text

print(inputString)
print(len(inputString))