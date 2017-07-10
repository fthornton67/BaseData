#!/usr/bin/env python
f = open('myersBriggsQuestionList.txt','r')
fWrite = open('myersBriggsQuestions.txt','w')   

for line in f:
	if len(line.strip()) > 0 and not("YES" in line):
		fWrite.write(line)