#!/usr/bin/python

import sys
from gensim import corpora, models, similarities
import re
from TweetSummaryTest import *
from re import compile
from lshash import LSHash



filename = "SNOW2014_dev.txt"
stopwords = ['http', 'www', 'com', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
removeUseless = compile(r'([\s]@[\S]*)|([\s]#[\S]*)|(^#[\S]*])|(^@[\S]*)|(\b[\S]{1}\b)')
specialChar = compile('[^a-zA-Z0-9 ]+')
regexEliminator = re.compile(r'(^.*(.)\2{2,}.*$)|(^.*[^a-zA-Z0-9 ]{2,}.*$)|(^([\S]+([\s]+)?){1,3}$)|(^.*[\s][^@#][\S]{12,}[\s].*$)|(^[^A-Z].*$)')




def filterHash(tweet):
	return removeUseless.sub('', tweet)

def filterSpecialChar(tweet):
	return specialChar.sub(' ', tweet)

def filterTweet(tweet):
	filteredTweet = regexEliminator.sub('', tweet).strip()
	return filteredTweet

def parse_data(inputfile):
	outputfile = inputfile + ".data"
	tweet = []
	f = open (outputfile,'w') 
	for line in open(inputfile):
		tweet = line.split()[8:-9]
		extract = filterTweet(' '.join(tweet))
		if( extract != ''):
			f.write(extract+"\n")
		#print ' '.join(tweet)
	print "Tweets parsed and stored in "+outputfile

def create_dictionary(inputfile):
	outputfile = inputfile + ".dict"
	dictionary = corpora.Dictionary(filterSpecialChar(filterHash(line)).lower().split() for line in open(inputfile+".data"))
	stop_ids = [dictionary.token2id[stopword] for stopword in stopwords if stopword in dictionary.token2id]
	once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
	dictionary.filter_tokens(stop_ids + once_ids)
	dictionary.compactify()
	dictionary.save(outputfile)
	print "Dictionary created successfully and stored in "+outputfile


def create_corpus(inputfile):
	dictfile = inputfile + ".dict"
	outputfile = inputfile + ".mm"
	datafile = inputfile + ".data"
	dictionary = corpora.Dictionary.load(dictfile)
	with open(datafile) as all_tweets:
		corpus = [dictionary.doc2bow(filterSpecialChar(filterHash(tweet)).lower().split()) for tweet in all_tweets]
	corpora.MmCorpus.serialize(outputfile, corpus)
	print "Corpus created successfully and stored in "+outputfile


def getDenseVector(vector, length):
	denseVector = [0]*length
	for i in vector:
		denseVector[i[0]] = 1
	return denseVector

def getSparseVector(vector):
	sparseVector = []
	for i in range(len(vector)):
		if (vector[i] != 0):
			sparseVector.append(tuple([i,1.0]))
	return tuple(sparseVector)

def detect_subevent(filename):
	dictionaryFile = filename + ".dict"
	corpusFile = filename + ".mm"
	outputFile = filename + ".out"
	outputVector = []
	tempDict = {}
	outputdict={}
	corpus = corpora.MmCorpus(corpusFile)
	dictionary = corpora.Dictionary.load(dictionaryFile)
	lsh = LSHash(30, dictionary.__len__())
	index = 0
	for index in range(len(corpus)):
		#print str(index)+",",
		#print corpus[index]
		denseVector = getDenseVector(corpus[index], lsh.input_dim)
		#print getSparseVector(denseVector)
		result = lsh.query(denseVector, num_results = 50, distance_func = "euclidean")
		#print result
		#no similar tweets
		
		if(result == []):
			outputdict[index]=[]
			tempDict[getSparseVector(denseVector)] = index
			lsh.index(denseVector)
			#continue
		
		else:
			for r in result:
				if(outputdict.has_key(tempDict[getSparseVector(r[0])])):
					outputdict[tempDict[getSparseVector(r[0])]].append(index)
					break
			
		
		
	#print outputdict
	with open(outputFile, 'w') as out:
		for key in outputdict.iterkeys():
			line = str(key) 
			for i in outputdict[key]:
				line += ", " + str(i)
			out.write(line+"\n")
	
	print "Please check the output file:", outputFile
			
def getDistance(vectorA, vectorB):
	match = 0
	index = 0
	for index in range(len(vectorA)):
		if (vectorB[index] == vectorB[index]):
			match = match + 1
		
	length = min (vectorA.count(1), vectorB.count(1))
	if(match > length/2):
		return True
	return False	


if len(sys.argv) >= 2:
	filename = sys.argv[-1]
else:
	print "File name missing! Give file name as a parameter!"

if(sys.argv[1] == "-P" or sys.argv[1] == "--parse"):
	parse_data(filename)
elif(sys.argv[1] == "-D" or sys.argv[1] == "--dict"):
	create_dictionary(filename)
elif(sys.argv[1] == "-C" or sys.argv[1] == "--corp"):
	create_corpus(filename)
elif(sys.argv[1] == "-S" or sys.argv[1] == "--sub"):
	detect_subevent(filename)
elif(sys.argv[1] == "-A" or sys.argv[1] == "--all"):
	parse_data(filename)
	create_dictionary(filename)
	create_corpus(filename)
	detect_subevent(filename)
	callSummary(filename,filename + ".out")
else:
	print "Fatal Error! Invalid Arguments!"

