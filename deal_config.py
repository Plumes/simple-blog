import codecs

config = codecs.open('config.txt','r','utf-8')
caption = (config.readline().strip()).split(':')[1]
domain = 'http://'+(config.readline().strip()).split(':')[1]
tmp = (config.readline().strip()).split(':')
catlist=[]
if(len(tmp)>1):
	catlist = tmp[1].split(',')
catlist.append('uncategorized')
tmp = (config.readline().strip()).split(':')
catnamelist=[]
if(len(tmp)>1):
	catnamelist = tmp[1].split(',')
catnamelist.append('未分类')
catnamedict = dict(zip(catnamelist,catlist))
#中文名为key
catdict=dict(zip(catlist,catnamelist))
#英文名为key
project = (config.readline().strip()).split(':')[1]
config.close()
#得到中文分类名称对应的英文分类名称