# 扇贝网：https://www.shanbay.com/已经有一个测单词量的功能，
# 我们要做的就是把这个功能复制下来，并且做点改良，搞一个网页版没有的功能 ———— 自动生成错词本。
# 在这一步，请阅读文档的同时打开浏览器的扇贝网，跟着我一步步来。

# （0）. 选择题库。
# 写这个程序，要用到requests模块。
# 先用requests下载链接，再用res.json()解析下载内容。
# 让用户选择想测的词库，输入数字编号，获取题库的代码。
# 提示：记得给input前面加一个int()来转换数据类型
import requests
while True:
    choice=int(input('what level do you want to test? 0:GMAT; 1:kaoyan; 2:gaokao; 3:CET4; 4:CET6; 5:TEM; 6:TOEFL; 7:GRE; 8:IELTS; 9:None'))
    if choice==0:
        url_fux='GMAT'
        break
    elif choice==1:
        url_fux='NGEE'
        break
    elif choice==2:
        url_fux='NCEE'
        break
    elif choice==3:
        url_fux='CET4'
        break
    elif choice==4:
        url_fux='CET6'
        break
    elif choice==5:
        url_fux='TEM'
        break
    elif choice==6:
        url_fux='TOEFL'
        break
    elif choice==7:
        url_fux='GRE'
        break
    elif choice==8:
        url_fux='IELTS'
        break
    elif choice==9:
        url_fux='NONE'
        break
    else:
        print('you must choice a number between 0 and 9')
        continue
url='https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+url_fux+'&_=1588644839013'
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}   
res=requests.get(url,headers=headers)  
json=res.json()
words=json['data']
# 创建一个空的列表，用于记录每个level的50个单词。
word50=[]
# 创建一个空的列表，用于记录用户认识的单词。
words_know=[]
# 创建一个空的列表，用于记录用户不认识的单词。
words_nokonw=[]
# build another empty list to store the questions which they answered correct or wrong
ans_correct=[]
ans_wrong=[]
# 启动一个循环，循环的次数等于单词的数量。
for x in words:
    word=x['content']
    # 记得加一个\n，用于换行。
    print('Do you know what does '+word+' mean?'+'\n')
    while True:
        # 让用户输入自己是否认识。
        answer=int(input('If yes, please input 1. If no, please input 0.'))
        # 如果用户认识：
        if answer==1:
            word50.append(word)
            # 就把这个单词，追加进列表words_knows。
            words_know.append(word)
            choice_dic={}
            for num in range(4):
                choice=x['definition_choices'][num]['definition']
                pk=x['definition_choices'][num]['pk']
                rank=x['definition_choices'][num]['rank']
                choice_dic[num]=[choice,pk,rank]
                print(str(num)+':'+choice)
            while True:
                try:
                    clint_answer=int(input('please input your choice (0,1,2,3)'))
                    correct_answer_pk=x['pk']
                    correct_answer_rank=x['rank']
                    compare=choice_dic.get(clint_answer)
                    if compare[1]==correct_answer_pk and compare[2]==correct_answer_rank:
                        ans_correct.append(word)
                    else:
                        ans_wrong.append(word)
                    break
                except ValueError:
                    print('please input a value between 0 and 3')
                except TypeError:
                    print('please input a value between 0 and 3')
            break
        # 否则
        elif answer==0:
            word50.append(word)
            # 就把这个单词，追加进列表not_knows。
            words_nokonw.append(word)
            break
        else:
            print("please input 1 or 0")
            continue
        # 打印一个统计数据：这么多单词，认识几个，认识的有哪些？
print('Out of 50 words, you know '+str(len(words_know))+'. And below are the words you know.')
for i in words_know:
    print(str(i)+'\n'+'-----------------------------')
print('Among all the words you know, you answered '+str(len(ans_correct))+' words correct')
for i in ans_correct:
    print(i+'\n'+'----------------------------------')
print('Among all the words you know, you answered '+str(len(ans_wrong))+' words wrong')
for i in ans_wrong:
    print(i+'\n'+'----------------------------------')

import csv
# 创建工作簿
csv_file=open('/Users/hua/Desktop/test/class7/HW7_CSV.csv','w',newline='') 
#中文乱码csv问题解决了
writer = csv.writer(csv_file)
writer.writerow(['word'])
for i in ans_wrong:
    writer.writerow([i])
# 写入完成后，关闭文件就大功告成啦！
csv_file.close() 