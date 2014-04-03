#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import os,collections,re,linecache
from TweetSummary import *

def summary(line,fileName):
	#fileName='sampletweets.txt'
	r=line.split(',')
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
		score= t.scoreATweet(line)
		if(len(allResults)!=5):
			allResults.append((score,line))	
			allResults=list(set(allResults))	
			allResults.sort(key=lambda tup: -tup[0])

		elif allResults[-1][0]<score:
			del allResults[-1]
			allResults.append((score,line))	
			allResults=list(set(allResults))
			allResults.sort(key=lambda tup: -tup[0])

	for x in allResults:
		print x[1]
#print t.scoreATweet("America, If you only vote for one President this year, make it @BarackObama.")
#print t.scoreATweet("Love Sosa Remix!! #Obama Lmfaooo pic.twitter.com/4boin4xz lmfaooooooooo lmfaooooooooo")
#print t.scoreATweet("Have a friend who's a last-minute decision maker? Remind them of @BarackObama's record—then get them to the polls. http://twitpic.com/bar409")
#print t.scoreATweet("The assault on voting rights... Citizens United squeezes democracy on one end and voter suppression on the other #Ryan #Romney #p2")
def callSummary(mainFile,outFile):
	for line in open(outFile):
		print '****************'
		summary(line,mainFile)

