#coding=utf8
from xml.etree import ElementTree as ET
#from pymongo import MongoClient
from time import clock
import sys
import pycurl
import StringIO
import json

def parsepage(str):
	root = ET.fromstring(str)
	doc={}
	rdoc={}
	cdoc={}
	title = root.find('title')
	if(title is not None):
		doc['title']=title.text
	# ns = root.find('ns').text
	# if(ns):
	# 	doc['ns']=ns.text
	id = root.find('id')
	if(id is not None):
		doc['id']=id.text
	revision = root.find('revision')
	redirect = root.find('redirect')
	if(revision is not None):
		rid = revision.find('id')
		if(rid is not None):
			rdoc['id']=rid.text
		parentid = revision.find('parentid')
		if(parentid is not None):
			rdoc['parentid']=parentid.text
		contributor = revision.find('contributor')
		if(contributor is not None):
			username = contributor.find('username')
			if(username is not None):
				cdoc['username']=username.text
			uid = contributor.find('id')
			if(uid is not None):
				cdoc['id']=uid.text
			ip = contributor.find('ip')
			if(ip is not None):
				cdoc['ip']=ip.text
			rdoc['contributor']=cdoc
		comment = revision.find('comment')
		if(comment is not None):
			rdoc['comment']=comment.text
		model = revision.find('model')
		if(model is not None):
			rdoc['model']=model.text
		format = revision.find('format')
		if(format is not None):
			rdoc['format']=format.text
		text = revision.find('text')
		if(text is not None):
			rdoc['text']=text.text
		sha1 = revision.find('sha1')
		if(sha1 is not None):
			rdoc['sha1']=sha1.text
		doc['revision']=rdoc
	return doc

def putData(doc):
	ids = doc['id']
	c = pycurl.Curl()
	url = 'http://localhost:9200/wiki/pages/'+ids
	c.setopt(pycurl.URL, url)
	c.setopt(pycurl.CUSTOMREQUEST, "PUT")
	c.setopt(pycurl.POSTFIELDS, json.dumps(doc))
	c.perform()


if __name__ == '__main__':
	start = clock()
	#client = MongoClient()
	# database name
	#soadb = client['soa']
	# collection name
	#enwiki = soadb['enwiki']

	# fin = open('enwiki-latest-pages-articles.xml','r')
	fin = open('enwiki-latest-pages-articles-firstpart.xml','r')
	# fin=open('testparse.xml','r')
	count = 0
	line = fin.readline()
	while line:
		str = ''
		if line.strip() == '<page>':
			str += line
			line = fin.readline()
			while line:
				str += line
				if line.strip() == '</page>':
					break
				line = fin.readline()
			try:
				count += 1
				doc = parsepage(str)
				print '%d %s' % (count, doc['title'])
				putData(doc)
			except:
				print str
				sys.exit(0)
		line = fin.readline()
	fin.close()
	end = clock()
	costtime = (end - start)
	print 'it take %d seconds' % (costtime)
	print 'finished'
