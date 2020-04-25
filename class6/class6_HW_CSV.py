# 调用requests库
import requests,csv
# 调用BeautifulSoup库
from bs4 import BeautifulSoup 
headers={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
results=[]

# 创建工作簿
csv_file=open('/Users/hua/Desktop/test/class6/HW6_CSV.csv','w',newline='',encoding='utf_8_sig') 
#中文乱码csv问题解决了
writer = csv.writer(csv_file)
writer.writerow(['number','name','link','star','recomd'])
for j in range(10):
    link_number=str(j*25)
    link='https://movie.douban.com/top250?start='+link_number+'&filter=' 
    # 返回一个response对象，赋值给res
    res =requests.get(link,headers=headers)
    # 把res解析为字符串
    html=res.text
    # 把网页解析为BeautifulSoup对象
    soup = BeautifulSoup(html,'html.parser')
    main_body=soup.find('ol',class_='grid_view')
    li_tag=main_body.find_all('li')  
    for i in range(len(li_tag)):
        try:
            number=li_tag[i].find('em',class_="").text
        except AttributeError:
            number=''
        try:
            name=li_tag[i].find('span', class_="title").text
        except AttributeError:
            name=''
        try:
            link=li_tag[i].find('a', class_="")['href']
        except AttributeError:
            link=''
        try:
            star=li_tag[i].find('span',class_="rating_num").text
        except AttributeError:
            star=''
        try:
            recomd=li_tag[i].find('span',class_="inq").text
        except AttributeError:
            recomd=''
        #print('rank: '+number+'\n'+' name: '+name+'\n'+' star: '+star+'\n'+link+'\n'+recomd+'\n')
        results.append([number,name,link,star,recomd])
        writer.writerow([number,name,link,star,recomd])
# 写入完成后，关闭文件就大功告成啦！
csv_file.close()   