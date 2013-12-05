#Coding:UTF-8
import os
import codecs
from deal_config import caption,domain,catlist,catnamelist,catnamedict,project

def convert(rawname):
	raw = codecs.open('./rawpost/'+rawname+'.txt','r','utf-8')
	

	catalog = codecs.open('catalog.txt','a','utf-8')
	#处理日期
	line = (raw.readline()).strip()
	date = line.split(':')[1].split('-')
	year = date[0]
	month = date[1]
	day = date[2]
	#处理时间
	line = (raw.readline()).strip()
	hour = line.split(':')[1]
	minute = line.split(':')[2]
	#处理 tag
	taglist=[]
	line = (raw.readline()).strip()
	if(len( line.split(':') )>1 and line.split(':')[1] !=""):
		taglist = (line.split(':')[1]).split(',')
	#处理归类
	line = (raw.readline()).strip()
	if(len( line.split(':') )>1 and line.split(':')[1] !=""):
		cat = line.split(':')[1]
	else:
		cat = "未分类"
	#处理标题
	line = (raw.readline()).strip()
	#print(line)
	title = line.split(':')[1]

	catalog.write('{0}{1}{2}{3}{4}\n'.format(year,month,day,hour,minute))
	catalog.write('name:{0}\n'.format(rawname))
	catalog.write('tag:')
	if len(taglist)>0:
		for tag in taglist:
			catalog.write('{0}/'.format(tag))
	catalog.write('\n')
	catalog.write('cat:{0}\n'.format(cat))
	catalog.close()

	res = codecs.open('./'+project+'/post/'+rawname+'.html','w','utf-8')
	shortres = codecs.open('./shortpost/'+rawname+'.html','w','utf-8')
	head = codecs.open('./template/head.html','r','utf-8')
	
	for i in range(1,9):
		tmp = head.readline()
		res.write(tmp)
	res.write('<title>'+title+' | 羽音</title>\n')
	tmp = head.readline()
	for tmp in head:
		#tmp = head.readline()
		res.write(tmp)
	head.close()
	res.write('\n<div class="post" id="post1">\n')
	res.write('<div class="post-title">'+title+'</div>\n')
	shortres.write('<div class="post-title"><a href={0}/post/{1}.html>'.format(domain,rawname)+title+'</a></div>\n')
	
	res.write('<div class="post-detail">发表于 '+year+'年'+month+'月'+day+'日')
	shortres.write('<div class="post-detail">发表于 '+year+'年'+month+'月'+day+'日')
	
	res.write(' 标签：')
	shortres.write(' 标签：')
	for tag in taglist:
		res.write(tag+' / ')
		shortres.write(tag+' / ')
	res.write('</div>\n')
	shortres.write('</div>\n')
	res.write('<div class="post-content">\n')
	shortres.write('<div class="post-content">\n')

	#lines = raw.readlines();
	i=0
	kill_p=0
	for line in raw:
		#print(line)

		if '<pre' in line:
			kill_p=3
		if '</pre>' in line:
			kill_p=2
		if kill_p==0:
			line = line.rstrip()
			line  = '<p>'+line+'</p>\n'
			#res.write('<p>'+line+'</p>')
		elif kill_p==1:
			line = line.replace('&','&amp;')
			line = line.replace('<','&lt;')
			line = line.replace('>','&gt;')
			
			#res.write(line)
		elif kill_p == 2:
			kill_p = 0
		elif kill_p == 3:
			kill_p = 1
		res.write(line)
		if i<10:
			shortres.write(line)	
			i=i+1
		
		

	res.write('\n<p id="entry_cr"><img alt="知识共享许可协议" src="http://anegie.com/images/cc.png" /><br />版权声明：本文版权属于作者 Plumes，并受法律保护。<br />本作品采用知识共享「<a href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh" target="_blank">署名 - 非商业性使用 - 相同方式共享 3.0 未本地化版本</a>」许可协议进行许可。</p>\n')
	res.write('</div>\n\t\t\t</div>\n')
	shortres.write('\n<p class="readmore"><a href={0}/post/{1}.html>阅读全文</a></p>\n</div>\n'.format(domain,rawname))
	shortres.close()
	raw.close()

	foot = codecs.open('./template/post-foot.html','r','utf-8')
	for line in foot:
		res.write(line)

	res.close()
	foot.close()



tmpl = os.listdir('./rawpost')
if ".gitignore" in tmpl:
	tmpl.remove(".gitignore")
rawlist=[]
for i in tmpl:
	rawlist.append(i[0:-4])

tmpl = os.listdir('./'+project+'/post')
postlist=[]
for i in tmpl:
	postlist.append(i[0:-5])

for rawname in rawlist :
	if rawname not in postlist:
		convert(rawname)