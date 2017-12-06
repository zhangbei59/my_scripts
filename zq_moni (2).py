#!/usr/bin/env python
# -*- coding:utf8 -*-

import urllib
import urllib2
import re
import smtplib
from email.mime.text import MIMEText



key_word='2017年12月2日'
url="http://www.sac.net.cn/cyry/kspt/kscjcx/"

sender = 'zhangbei@58kuyun.com'
my_pass= 'Es8NX4EP9JcecRjx'
receiver='402151718@qq.com'

def mail():
    ret = True
    try:
        content = "主人，12月3日的证券考试成绩已经发布，请火速查看,网址"+url
        print(content)
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = "12月3日证券成绩发布通知"
        server = smtplib.SMTP("smtp.exmail.qq.com",587)
        server.starttls()
	server.login(sender, my_pass)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
    except Exception as e:
        ret = False
        print(e)
    return ret



req = urllib2.Request(url)
res = urllib2.urlopen(req)
res_index=(res.read().find(key_word))
print res_index
if res_index > 0:
    mail()
else:
   print  '无内容更新'

res.close()

