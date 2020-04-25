# 调用requests库
import requests 
# 调用BeautifulSoup库
from bs4 import BeautifulSoup 
headers = {
    'origin':'www.kuaidi100.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://www.kuaidi100.com/',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }
url='https://www.kuaidi100.com/query'
name=input('请输入您要查询的快递公司：（用拼音表示）')
num=input('请输入您要查询的快递单号：')
params={
    'type': name,
    'postid': str(num),
    'temp': str(0.30397791605786306),
    'phone':'' 
}
res_music = requests.get(url,headers=headers,params=params)
json_music = res_music.json()
json_data=json_music.get('data')
for item in json_data:
    print(item.get('time'))
    print(item.get('context'))
    print('-------------------------')