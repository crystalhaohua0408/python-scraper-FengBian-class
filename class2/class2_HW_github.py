# 题目要求：你需要爬取的是网上书店Books to Scrape (http://books.toscrape.com/) 中所有书的分类类型，并且将它们打印出来。
# 它的位置就在网页的左侧，如：Travel，Mystery，Historical Fiction…等。
#please scrape the comment part for this website
# https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/
# 调用requests库
import requests 
# 调用BeautifulSoup库
from bs4 import BeautifulSoup 
# 返回一个response对象，赋值给res
res =requests.get('http://books.toscrape.com/')
# 把res解析为字符串
html=res.text
# 把网页解析为BeautifulSoup对象
soup = BeautifulSoup(html,'html.parser')
side_cat=soup.find(class_='nav nav-list') 
j=side_cat.li
j1=j.ul
items = j1.find_all('a')
for item in items:
    print(item.text)

# 题目要求：你需要爬取的是网上书店Books to ScrapeTravel这类书中，所有书的书名、评分、价格三种信息，并且打印提取到的信息。
#please scrape the comment part for this website
# https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/
# 调用requests库
import requests 
# 调用BeautifulSoup库
from bs4 import BeautifulSoup 
# 返回一个response对象，赋值给res
res =requests.get('http://books.toscrape.com/')
# 把res解析为字符串
html=res.text
# 把网页解析为BeautifulSoup对象
soup = BeautifulSoup(html,'html.parser')
section=soup.find('section') 
section1=section.ol
li=section1.find_all('li')
for item in li:
    star=item.find('p')
    print(star['class'][1])
    name=item.find('h3')
    print(name.a.text)
    price=item.find(class_='product_price')
    print(price.p.text)

#please scrape the comment part for this website
# https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/
# 调用requests库
import requests 
# 调用BeautifulSoup库
from bs4 import BeautifulSoup 
# 返回一个response对象，赋值给res
res =requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/')
# 把res解析为字符串
html=res.text
# 把网页解析为BeautifulSoup对象
soup = BeautifulSoup(html,'html.parser')
# 通过匹配属性class='comment byuser comment-author-master bypostauthor even thread-even depth-1'提取出我们想要的comments元素
items = soup.find_all(class_='comment-content')
#class_="comment byuser comment-author-master bypostauthor even thread-even depth-1"
for item in items:
    # 在列表中的每个元素里，匹配属性class_='comment-content'提取出数据   
    brief = item.text
    print(brief)
