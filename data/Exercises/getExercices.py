#!/usr/bin/python
import httplib, urllib
import xml.etree.ElementTree as ET
import time

from htmlentitydefs import name2codepoint


import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")
for i in range(1,400):     
	conn = httplib.HTTPConnection("www.sparkpeople.com")
	conn.request("GET", "/resource/exercises-pop-indiv.asp?ID=%d" % (i))
	response = conn.getresponse()   
	print(response.status)
	if response.status == 200:
		data = response.read()
		# instantiate the parser and fed it some HTML  
		data = data.replace("<br>","<br/>").replace("<BR>","<BR/>")
		with open("exercise/ex_id_%d.htm" % (i), "a") as exFile:
			exFile.write(data)       
conn.close() 