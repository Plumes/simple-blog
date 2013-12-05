#coding:UTF-8
import codecs
from deal_config import caption,domain,catlist,catnamelist,catnamedict,project,catdict
#print(catnamelist)
temp = codecs.open('./template/head-temp.html','r','utf-8')
text = temp.read().format(caption=caption,domain=domain)
temp.close()
l=text.split('#catlist#')
text=l[0]
for key,val in catdict.items():
	s = '<li><a href="{0}/category/{1}.html">{2}</a></li>\n'.format(domain,key,val)
	text = text+s
text=text+l[1]
head = codecs.open('./template/head.html','w','utf-8')
head.write(text)
head.close()
