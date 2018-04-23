# -*- conding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
import os



def xiaoe_login():
    cookies = {
        'XIAOEID': '06c8e4c5459e4dfd844d763a7a8e3782',
        'xe_username': '13253610707',
        'xe_passwd': 'password', #密码
        'tgw_l7_route': 'ecf102e7e9af5242ac9836569b5d93b5',
        'Hm_lvt_081e3681cee6a2749a63db50a17625e2': '1524211665,1524211698,1524211907,1524462157',
        'channel': 'pingpai_area',
        'Hm_lvt_32573db0e6d7780af79f38632658ed95': '1524211682,1524211893,1524214666,1524462978',
        'Hm_lpvt_32573db0e6d7780af79f38632658ed95': '1524462978',
        'Hm_lpvt_081e3681cee6a2749a63db50a17625e2': '1524463058',
        'laravel_session': 'eyJpdiI6IkU1N1ZraERnVG12MzI5OXYyd2NDTXc9PSIsInZhbHVlIjoiamhxZGhUNFwvUGtKQ292M0xrYmlLckpsbCtTVFR3WE5YQlNqcis2RXJKU1ZkeXRXWVRnOTlLR2ZRRUNuZFVRTGpBcUVLdmc3eHJ3bGdndDVpb1BmR2FBPT0iLCJtYWMiOiJiMWVjOGJlZmEwNmMxMzY1NTZiZmM1MzQ4MzllMDNjN2YzMjA2YTlkY2U3OWE2ODNiZGM2YWMxN2YzZTAyNmU5In0%3D',
    }

    headers = {
        'Origin': 'https://admin.xiaoe-tech.com',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://admin.xiaoe-tech.com/login_page',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }

    data = [
        ('username', '13253610707'),
        ('password', 'xxxx'), #密码
        ('img_code', '9515'),
    ]

    response = requests.post('https://admin.xiaoe-tech.com/dologin', headers=headers, cookies=cookies, data=data)
    #print(response.text)


def get_coure():
    import requests

    cookies = {
        'XIAOEID': '06c8e4c5459e4dfd844d763a7a8e3782',
        'channel': 'pingpai_area',
        'Hm_lvt_32573db0e6d7780af79f38632658ed95': '1524211682,1524211893,1524214666,1524462978',
        'Hm_lpvt_32573db0e6d7780af79f38632658ed95': '1524462978',
        'tgw_l7_route': '1f4fc3a8216a1a6558ccfd82bd9a54b9',
        'laravel_session': 'eyJpdiI6IlNSRDFDOWNEcVJOSzJnN0ZMYmtnXC9RPT0iLCJ2YWx1ZSI6ImJqZG9HYTI5TzNpQ0FGUlZnNEU5RzhzMDlHNlV5a2p4RHR6TnFDSDlkMFVrOWlPVnVnUElNWmR0UjA2SFFsbGFqUUhINGtzdVNKSnRSSkU4UWxidEFBPT0iLCJtYWMiOiJhNTI4MjAxNzRiZjRlM2MxNGY4MWUzYjM0MzFlOGMzNjAzNmY3NmVkMGRlZGM3MjVmMTY0ZDhlZGJlM2YyNDNlIn0%3D',
    }

    headers = {
        'Origin': 'http://pc-shop.xiaoe-tech.com',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Referer': 'http://pc-shop.xiaoe-tech.com/appgp6EDV1w6936/columnist_detail?id=p_5a98c01c490cc_NGnnmhAC',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }

    data = [
        ('data[page_index]', '0'),
        ('data[page_size]', '100'),
        ('data[order_by]', 'start_at:desc'),
        ('data[resource_id]', 'p_5a98c01c490cc_NGnnmhAC'),
        ('data[state]', '0'),
        ('data[resource_types][]', '1'),
        ('data[resource_types][]', '2'),
        ('data[resource_types][]', '3'),
        ('data[resource_types][]', '4'),
    ]

    response = requests.post('http://pc-shop.xiaoe-tech.com/appgp6EDV1w6936/open/column.resourcelist.get/2.0',
                             headers=headers, cookies=cookies, data=data)

    return response.text

def get_url():
    json_course = get_coure()
    course_dict = json.loads(json_course)
    course = course_dict["data"]
    #print(type(course))
    course_dict = {}
    url_start ="http://pc-shop.xiaoe-tech.com/appgp6EDV1w6936/video_details?id="
    for i in course:
        #获取每一个课程的字典数据
        course_dict[i["title"]] = url_start+i["id"]
    newdic = sorted(course_dict.items(),key = lambda x:x[0],reverse = False)
    print(type(newdic))
    #TODO   写入txt文档，研究字典的写入方法
    os.chdir('C:\\Users\\ly199\\Desktop')
    with open('‪python.txt','w',encoding='utf-8') as file:
        for i in newdic:
            file.write(i[0]+'\t')
            file.write(i[1]+'\n')




if __name__ == "__main__":
    #下面的登录函数非必须，可以直接使用get_coure函数或许课程，里面的cookie和header从浏览器获取即可。
    #xiaoe_login()
    get_coure()
    get_url()

