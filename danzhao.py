#!/usr/bin/env python3
# -*- coding:utf8 -*-

import urllib
import smtplib
import urllib.request
from email.mime.text import MIMEText


#定义新闻标题关键字，由于不确定发布的标题，但是应该是这3天内发布，所以监控3天的日期，如果页面出现这个日期，代表有文章更新
key_word=['2020-11-22','2020-11-23','2020-11-24']
#定义监控页面的url
url="https://zsjy.hnzj.edu.cn/zsxx.htm"

my_pass= 'qq邮箱授权码'
mail_from='402151718@qq.com'
mail_to='402151718@qq.com'

subject='河南职业技术学院新闻更新'
content = "主人，河南职业有最新新闻更新，请火速查看,网址"+url #定义发送内容
msg = MIMEText(content, 'plain', 'utf-8') #重构发送信息
msg['From'] = mail_from
msg['To'] = mail_to
msg['Subject'] = subject


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


#查找网页源码，找关键日期

req = urllib.request.urlopen(url)
print(req.getcode())
html = str(req.read())
#循环查找这3个日期
for des_date in key_word:
    print(des_date)
    if des_date in html:
        mail()
    else:
        print('暂时无内容更新')
req.close()


