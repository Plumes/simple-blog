#coding:utf-8
import os
import codecs
import math
from operator import itemgetter
from deal_config import caption,domain,catlist,catnamelist,catnamedict,project
postdict={}
#该篇日志对应发表时间
tagdict={}
#该篇日志对应标签字符串
catdict={}
#该篇日志对应中文分类名称字符串



for catpage in catlist:
	tmppage=codecs.open('./'+project+'/category/'+catpage+'.html','w','utf-8')
	head = codecs.open('./template/head.html','r','utf-8')
	for tmp in head:
		#tmp = head.readline()
		tmppage.write(tmp)
	head.close()
	tmppage.close()
#创建各个分类页，并写入头部模板

catalog = codecs.open('catalog.txt','r','utf-8')

i=0
name=""
for line in catalog:
	line = line.strip()
	if len(line)>0:
		if i==0:
			date=int(line)
			i=i+1
		elif i==1:
			name=(line.split(':')[1])
			i=i+1
		elif i==2:
			tagstr=""
			if len(line.split(':')) >1 and line.split(':')[1] !="":
				tagstr = line.split(':')[1]
			i=i+1
		elif i==3:
			cat=line.split(':')[1]
			i=0
			postdict[name]=date
			tagdict[name]=tagstr
			catdict[name]=cat

postdict=sorted(postdict.items(), key=itemgetter(1), reverse=True)
print (postdict)
#对所有文章按照发表时间从新到旧排序，新的排在最前

postcnt=len(postdict)
lastpage = math.ceil(postcnt/6)

pagenum=0;

while(postcnt>0):
	maxcnt = min(6,postcnt)
	postcnt = postcnt-maxcnt
	if pagenum==0:
		page = codecs.open('./'+project+'/index.html','w','utf-8')
	else:
		page = codecs.open('./'+project+'/page{0}.html'.format(pagenum),'w','utf-8')
	head = codecs.open('./template/head.html','r','utf-8')
	for tmp in head:
		#tmp = head.readline()
		page.write(tmp)
	head.close()

	for i in range(pagenum*6,pagenum*6+maxcnt):
		postname=postdict[i][0]
		catname = catnamedict[catdict[postname]]
		catpage = codecs.open('./'+project+'/category/'+catname+'.html','a','utf-8')
		page.write('\n<div class="post" id="post{0}">\n'.format(i))		
		catpage.write('\n<div class="post" id="post{0}">\n'.format(i))		
		
		shortpost = codecs.open('./shortpost/{0}.html'.format(postdict[i][0]),'r','utf-8')

		for line in shortpost:
			page.write(line)
			catpage.write(line)
		shortpost.close()
		
		page.write('\n</div>\n')
		catpage.write('\n</div>\n')
		catpage.close()
	if pagenum >0:
		if pagenum==1:
			page.write('<div id="prevpage"><a href="index.html">&larr;&nbsp;Prev</a></div>')
		else:
			page.write('<div id="prevpage"><a href="page{0}.html">&larr;&nbsp;Prev</a></div>'.format(pagenum-1))
	if pagenum<lastpage-1:
		page.write('<div id="nextpage"><a href="page{0}.html">Older &rarr;</a></div>'.format(pagenum+1))
	foot = codecs.open('./template/foot.html','r','utf-8')
	for line in foot:
		page.write(line)

	page.close()
	pagenum=pagenum+1
	foot.close()

for catpage in catlist:
	tmppage=codecs.open('./'+project+'/category/'+catpage+'.html','a','utf-8')
	foot = codecs.open('./template/foot.html','r','utf-8')
	for line in foot:
		#tmp = head.readline()
		tmppage.write(line)
	foot.close()
	tmppage.close()



