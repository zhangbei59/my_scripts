#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import urllib
import smtplib
import urllib.request
from email.mime.text import MIMEText
import json


#定义关键字，可以通过查看返回数据找到所有监控的关键字，可以一个或者多个
key_word=['''bookState":"0"''']
#定义监控页面的url，这里具体为请求域名的具体查询链接，可以根据需要去network里面获取
url="http://checksolr.xinnet.com/domain/domainBookSearch?callbackparam=jQuery17208028104623956083_1606397646236&domainName=&notDomainName=&deleteDate=&location=contains&domainLengthStart=1&domainLengthEnd=4&domainKindType=LET&domainXSType=&domainSuffix=.com&pageSize=30&pageNo=1&lengthSortDesc=false&_=1606398368116"
#快速链接而已，邮件内容一部分，方便快速打卡新网域名列表
new_url = "http://www.xinnet.com/domain/domain_book_search.jsp?f=nva"


#获取网页数据，并且转换为json格式，loads为dict格式，对数据进行解析读取

req = urllib.request.urlopen(url)
html = req.read()
# 处理返回数据为utf8
code_data = str(html, encoding='utf-8')
#优化返回数据结构，掐头去尾保留为可解析的json数据
code_data1 = "{"+(code_data[91:-3])+"}"
# print(code_data1)
#json数据解析为dict数据
json_data = json.loads(code_data1)
# print(type(json_data))

#定义一个空字符串，没读取到一个域名，拼接一个域名内容并换行，解析后为dict字典数据，可以根据键名去依次获取
domain_str = ''
for i in range(len(json_data["list"])):
    bookstate = json_data["list"][i]["bookState"]
    domainname = json_data["list"][i]["domainName"]
    if bookstate == "0":
        domain_str=domain_str + "未预定" +" "+domainname+"\n"
    else:
        domain_str = domain_str + "已预定" +" "+ domainname+"\n"
req.close()


#定义发送邮件发送方及收件方,注意密码要使用邮箱授权密码才能发送邮件
my_pass = '此处为授权密码'
mail_from ='402151718@qq.com'
mail_to ='402151718@qq.com'

#定义邮件主题和内容及发送形式
subject='有最新的未预定.com域名'
content = "主人,com域名更新,请火速查看,网址\n"+new_url+"\n"+"详情请看    \n"+ domain_str #定义发送内容
msg = MIMEText(content, 'plain', 'utf-8') #重构发送信息
msg['From'] = mail_from
msg['To'] = mail_to
msg['Subject'] = subject



#定义邮件发送函数，随时调用
def mail():
    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', smtplib.SMTP_SSL_PORT)
        server.login(mail_from,my_pass)
        server.sendmail(mail_from,mail_to, msg.as_string())
        print('发送邮件成功')
    except Exception as e:
        print('发送邮件异常')
        print(e)
    finally:
        server.quit()


#循环查找列表内关键字，可设置多个关键字符
for des_date in key_word:
    if des_date in code_data:
        mail()
    else:
        print('暂时无内容更新')
