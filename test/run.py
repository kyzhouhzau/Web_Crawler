#! usr/bin/env python3
# -*- coding:utf-8 -*-
from  抓取招聘信息.craw_jobs.抓取招聘信息 import Craw_jobs
from 抓取招聘信息.craw_jobs.db import *
def main(page):
    location = '选择地区'
    workname = '生物信息'
    s = Craw_jobs()
    html = s.get_one_page(location,workname,page)
    if html:
        for item in s.parse_one_page(html):
            print(item)
            save_to_mongo(item)
            s.write_to_file(item)

if __name__ =='__main__':
    for i in range(1,40):
        main(i)