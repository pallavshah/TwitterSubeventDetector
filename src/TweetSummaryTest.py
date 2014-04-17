#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import os,collections,re,linecache
from TweetSummary import *

words = ['fuck', 'fcku', 'ass', 'bitch', 'asshole' ,'nigga', 'nigger', 'negro']
f = open('summary.xml','w')
def summary(line,fileName):
	#fileName='sampletweets.txt'
	r=line.split(',')
	if len(r) < 10:
		return
	t=tfidf()
	#listOfSummary={}
	#print fileName
	
	for num in r:
		line=linecache.getline(fileName,int(num)+1)
		#print line
		if len(line.split("\t")[8])>0:
			line=line.split("\t")[8]
		else:
			continue
	#	checkForBad=line.lower().split(" ")

		if any(i for i, x in enumerate(words) if x in line):
			continue

		line = re.sub(r"(?:\@|\#|https?\://)\S+", "", line)

		t.addDocument(line)

	#t.addDocument("The assault on voting rights... Citizens United squeezes democracy on one end and voter suppression on the other #Ryan #Romney #p2")
	#t.addDocument("America, If you only vote for one one President this year, make it @BarackObama.")
	#t.addDocument("America, If you only vote for one President this year, make it @BarackObama.")
	#t.addDocument("Love Sosa Remix!! #Obama Lmfaooo pic.twitter.com/4boin4xz lmfaooooooooo lmfaooooooooo")
	#t.addDocument("Have a friend who's a last-minute decision maker? Remind them of @BarackObama's record—then get them to the polls. http://twitpic.com/bar409")

	t.calculateTfIdf()
	allResults=[]
	for num in r:
		line=linecache.getline(fileName,int(num)+1)
		#print line
		if len(line.split("\t")[8])>0:
			line=line.split("\t")[8]
		else:
			continue
		checkForBad=line.strip().lower().split(" ")

		if any(i for i, x in enumerate(words) if x in line):
			continue
			
		score= t.scoreATweet(line)
		if(len(allResults)<5):
			allResults.append((score,line))	
			allResults=list(set(allResults))	
			allResults.sort(key=lambda tup: -tup[0])

		elif allResults[-1][0]<score:
			del allResults[-1]
			allResults.append((score,line))	
			allResults=list(set(allResults))
			allResults.sort(key=lambda tup: -tup[0])
	if not allResults:
		return
	if not allResults[0]:
		return
	f.write('<subevent>\n')
	line_topic = re.sub(r"(?:\@|\#|https?\://)\S+", "", allResults[0][1])
	line_topic=re.sub(r'[^\x00-\x7F]+','',line_topic)
	if line_topic.strip() == '':
		line_topic =allResults[0][1]
	f.write('<heading>'+line_topic.replace('<', '').replace('>', '').replace('&', '&amp;')+'</heading>\n')

	for x in allResults:
		if not (x[1] is None):
			t=re.sub(r'[^\x00-\x7F]+','', x[1])
			if t is not None:
				f.write('<tweet>'+t.replace('<', '').replace('>', '').replace('&', '&amp;')+'</tweet>')
	f.write('</subevent>\n')
#print t.scoreATweet("America, If you only vote for one President this year, make it @BarackObama.")
#print t.scoreATweet("Love Sosa Remix!! #Obama Lmfaooo pic.twitter.com/4boin4xz lmfaooooooooo lmfaooooooooo")
#print t.scoreATweet("Have a friend who's a last-minute decision maker? Remind them of @BarackObama's record—then get them to the polls. http://twitpic.com/bar409")
#print t.scoreATweet("The assault on voting rights... Citizens United squeezes democracy on one end and voter suppression on the other #Ryan #Romney #p2")
def callSummary(mainFile,outFile):
	f.write('<tweets>\n')
	for line in open(outFile):
		summary(line,mainFile)
	f.write('</tweets>\n')
	f.close()

if len(sys.argv) >= 1:
	filename = sys.argv[1]
	callSummary('SNOW2014_dev.txt',filename)
else:
	print "File name missing! Give file name as a parameter!"


