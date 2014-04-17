#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys,os,math,re
from decimal import *

class tfidf:
    def __init__(self):
        self.doc_dict = {}
        self.countOfWords=0.0
        self.countOfTweets=0.0
        self.word_count = {}
        self.tfidf = {}

    def addDocument(self, tweet):
        # building a dictionary
        stoplist = set("a about above after again against all am an and any are aren't as at be because been before being below between both but by can't cannot could couldn't did didn't do does doesn't doing don't down during each few for from further had hadn't has hasn't have haven't having he he'd he'll he's her here here's hers herself him himself his how how's i i'd i'll i'm i've if in into is isn't it it's its itself let's me more most mustn't my myself no nor not of off on once only or other ought our ours".split())
        tweet=tweet.lower()        
        list_of_words1=tweet.split(" ")
        list_of_words = [words for words in list_of_words1 if words not in stoplist]

        doc_dict = {}
        self.countOfWords=len(list_of_words)+self.countOfWords
        self.countOfTweets=self.countOfTweets+1.0
        for w in list_of_words:
            self.doc_dict[w] = self.doc_dict.get(w, 0.) + 1.0

        my_set=set(list_of_words)

        for w in my_set:
        	self.word_count[w] = self.word_count.get(w,0.)+1.0
            

    def similarities(self):
    	print self.tfidf

    def calculateTfIdf(self):
    	for k in self.doc_dict.keys():
    		tf=self.doc_dict.get(k)/self.countOfWords
    		idf=self.countOfTweets/self.word_count.get(k)
    		self.tfidf[k]=tf*(math.log(idf)/math.log(2))

    def scoreATweet(self,tweet):
    	stoplist = set("a about above after again against all am an and any are aren't as at be because been before being below between both but by can't cannot could couldn't did didn't do does doesn't doing don't down during each few for from further had hadn't has hasn't have haven't having he he'd he'll he's her here here's hers herself him himself his how how's i i'd i'll i'm i've if in into is isn't it it's its itself let's me more most mustn't my myself no nor not of off on once only or other ought our ours".split())
        tweet = re.sub(r"(?:\@|\#|https?\://)\S+", "", tweet)
        tweet=tweet.lower()        
        list_of_words1=tweet.split(" ")
        list_of_words = [words for words in list_of_words1 if words not in stoplist]
        summOfTfIdf=0
        for w in list_of_words:
        	summOfTfIdf=summOfTfIdf+self.tfidf.get(w)

        return summOfTfIdf/len(list_of_words)