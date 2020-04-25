import requests
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
# 这是请求歌曲评论的url
headers = {
    'origin':'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }
for i in range(1,3):
    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'remoteplace': 'txt.yqq.lyric',
        'searchid': '100775862865662582',
        'aggr': '0',
        'catZhida': '1',
        'lossless': '0',
        'sem': '1',
        't': '7',
        'p': str(i),
        'n': '5',
        'w': '周杰伦',
        'g_tk_new_20200303': '1815176207',
        'g_tk': '1815176207',
        'loginUin': '1152921504717557181',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }
    res_music = requests.get(url,headers=headers,params=params)
    # 发起请求
    # 使用json()方法，将response对象，转为列表/字典
    json_music = res_music.json()
    json_list=json_music.get('data').get('lyric').get('list')
    for item in json_list:
        lyric=item.get('content')
        print(lyric)
        print('-------------------------------------')
