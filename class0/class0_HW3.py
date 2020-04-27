# 体验爬虫
# 引入requests库
import requests

# requests.get是在调用requests库中的get()方法，它向服务器发送了一个请求，括号里的参数是你需要的数据所在的网址，然后服务器对请求作出了响应。
# 我们把这个响应返回的结果赋值给变量res
res = requests.get('URL')

import requests 

res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png') 
# 打印变量res的响应状态码，以检查请求是否成功
print(res.status_code)

# 引入requests库
import requests

# 发出请求，并把返回的结果放在变量res中
res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')
# 把Reponse对象的内容以二进制数据的形式返回
pic = res.content
# 新建了一个文件ppt.jpg，这里的文件没加路径，它会被保存在程序运行的当前目录下。
# 图片内容需要以二进制wb读写。你在学习open()函数时接触过它。
photo = open('ppt.jpg','wb')
# 获取pic的二进制内容
photo.write(pic) 
# 关闭文件
photo.close()

# 引用requests库
import requests

# 下载《三国演义》第一回，我们得到一个对象，它被命名为res
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
# 把Response对象的内容以字符串的形式返回
novel=res.text
# 现在，可以打印小说了，但考虑到整章太长，只输出800字看看就好。在关于列表的知识那里，你学过[:800]的用法。
print(novel[:800])

import requests
res=requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
novel=res.text
print(novel[:800])

# 之后，我们就可以用通过读写文件把小说保存到本地了。这是Python基础语法知识，你应该已经学会了。下面直接给出做法，你也可以在自己的本地电脑上做尝试练习。
# 引入requests库
import requests
#下载《三国演义》第一回，我们得到一个对象，它被命名为res
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
# 把Response对象的内容以字符串的形式返回
novel = res.text
# 创建一个名为《三国演义》的txt文档，指针放在文件末尾，追加内容
k = open('《三国演义》.txt','a+')
# 写进文件中 
k.write(novel)
# 关闭文档    
k.close()

#下载图片
#引入requests库
import requests

# 发出请求，并把返回的结果放在变量res中
res=requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')
# 把Reponse对象的内容以二进制数据的形式返回
pic=res.content 
# 新建了一个文件ppt.jpg，这里的文件没加路径，它会被保存在程序运行的当前目录下。
# 图片内容需要以二进制wb读写。你在学习open()函数时接触过它。
photo=open('rainbow.mp3','wb')
# 获取pic的二进制内容
photo.write(pic)
# 关闭文件
photo.close()
