# -*- coding:utf-8 -*-
#使用multiprocessing模块线程方法 优化爬虫速度，100线程 1000页 用时50s左右
import time
import urllib.request
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool

def changepage(total):
	urls = []
	for i in range(total):
		url = 'https://www.gushiwen.org/shiwen/default_0A0A'+'%s'%str(i+1)+'.aspx'
		urls.append(url)
	return urls

def spider(urls):
	response = urllib.request.urlopen(urls)
	html = response.read().decode("utf-8")
	tree = etree.HTML(html)
	aa = tree.xpath('/html/body/div/div/div/div/div/@id') # 获取所以id的属性
	tangshi = []
	for i in range(10):
		a = 3+(i*2)
		title = tree.xpath('/html/body/div[2]/div[1]/div[%d]/div[1]/p[1]/a/b/text()'%a)
		author1 = tree.xpath('/html/body/div[2]/div[1]/div[%d]/div[1]/p[2]/a[1]/text()'%a)
		author2 = tree.xpath('/html/body/div[2]/div[1]/div[%d]/div[1]/p[2]/a[2]/text()'%a)
		contents =  tree.xpath("//*[@id='%s']/text()"%aa[i+1])
		if contents[0] == '\n':
			contents =  tree.xpath("//*[@id='%s']/p/text()"%aa[i+1])
		author = author1 + author2    
	saveinfo(title, author,contents)
	print(a)
	
def saveinfo(title, author,contents):
    with open('file.txt','a+',encoding='utf-8') as f:
        f.write(str(title) + '\n')
        f.write(str(author) + '\n')
        f.write(str(contents) + '\n\n')

if __name__ == '__main__':
	print('开始')
	start_time = time.time()
	pool = ThreadPool(10)
	urls = changepage(100)
	pool.map(spider, urls)
	#pool.wait()
	pool.close()
	pool.join()
	print ('爬取成功！')
	print('%d second'% (time.time()-start_time))
