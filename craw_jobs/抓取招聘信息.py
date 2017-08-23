#! usr/bin/env python3
# -*- coding:utf-8 -*-
from urllib.parse import urlencode
import requests
from requests.exceptions import RequestException
import json
from pyquery import PyQuery as pq
import re
from 抓取招聘信息.craw_jobs import db
class Craw_jobs(object):
    def get_one_page(self,location,workname,page):
        data = {
    
            'jl':location,
            'kw':workname,
            'p':page,
            'isadv':0
        }
    
        base_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?'
        url = base_url + urlencode(data)
        headers = {
    
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/59.0.3071.86 Safari/537.36'
        }
        try:
            response = requests.get(url,headers=headers,timeout = 4)
            if response.status_code==200:
                return response.text
            return None
        except RequestException:
            return None
    
    def parse_one_page(self,html):
        doc = pq(html)
        tables = doc('.newlist').items()
        for table in tables:
            yield {
                '岗位':table.find('.zwmc a').text(),
                '公司':table.find('.gsmc a').text(),
                '规模':re.search('<li.*?newlist_deatil_two.*?<span>(.*?)</span><span>(.*?)</span><span>(.*?)</span>.*?</li>',html,re.S).group(3)[5:],
                '月薪':table.find('.zwyx').text(),
                '工作地点':table.find('.gzdd').text(),
                '岗位要求':table.find('.newlist_deatil_last').text()[5:].strip()
            }
    
    def write_to_file(self,content):
        with open('生物信息招聘信息.txt','a',encoding='utf-8') as wf:
            wf.write(str(content)+'\n')
    
    

    


