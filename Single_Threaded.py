#coding:utf-8
# 单线程爬虫  1000页用时280s左右
import os
import urllib.request
from lxml import etree
#import MySQLdb as mysql

# # 打开数据库连接
# db = mysql.connect(user="root", passwd="123456", db="mysql", host="localhost", charset="utf8")
# db.autocommit(True)
# # 使用cursor()方法获取操作游标
# cur = db.cursor()
for j in range(100):
    url = 'https://www.gushiwen.org/shiwen/default_0A0A'+'%s'%str(j+1)+'.aspx' # 每次请求的url
    response = urllib.request.urlopen(url) # 获取页面返回所有内容
    html = response.read().decode("utf-8") # 读取页面内容 
    tree = etree.HTML(html) # 分析页面节点
    aa = tree.xpath('/html/body/div/div/div/div/div/@id') # 获取所以id的属性
    tangshi = []
    # 一个页面10诗，循环10次
    for i in range(10):
        a = 3+(i*2)
        title = tree.xpath('/html/body/div[2]/div[1]/div[%d]/div[1]/p[1]/a/b/text()'%a) # 标题
        author1 = tree.xpath('/html/body/div[2]/div[1]/div[%d]/div[1]/p[2]/a[1]/text()'%a) # 朝代
        author2 = tree.xpath('/html/body/div[2]/div[1]/div[%d]/div[1]/p[2]/a[2]/text()'%a) #作者
        contents =  tree.xpath("//*[@id='%s']/text()"%aa[i+1]) # 古诗内容
        if contents[0] == '\n':
            contents =  tree.xpath("//*[@id='%s']/p/text()"%aa[i+1])

        # sql = 'insert into memory (Time, VmSize, VmRSS, MemTotal, MemFree, Buffers, Cached, Mem_use)' \
        #       ' value (%s,%s,%s,%s,%s,%s,%s,%s)'\
        #       % (Time, VmSize, VmRSS, MemTotal, MemFree, Buffers, Cached, Mem_use)
        #cur.execute(sql)
        author = author1 + author2
        tangshi.append(title)
        tangshi.append(author)
        tangshi.append(contents)
    # 写入文本
    with open('tangshi3.txt','a+',encoding='utf-8') as f:
        f.write(str(tangshi))

    print(j)