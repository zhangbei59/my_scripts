#_*_ coding：utf-8 _*_
import os
import json
import requests

jsurl=r'http://player.polyv.net/videojson/'
course=open('C:\\Users\\ly199\\Desktop\\list.txt')
csrtxt=course.readlines()
for i in csrtxt:
    crlist = json.loads(i)
    vid=(crlist[ 'polyv_vid'])
    crno=(crlist['name'])
    crname=(crlist['course_name'])
    rejsurl=jsurl+vid+'.js'
    vlinkget=requests.get(rejsurl)
    linklist = json.loads(vlinkget.content)
    linkre=linklist['videolink']
    print(crno+linkre)
    m3u8txt = open('C:\\Users\\ly199\\Desktop\\'+crname+'.txt', 'a')
    m3u8txt.write(crno+linkre)
    m3u8txt.write('\n')
course.close()
m3u8txt.close()



