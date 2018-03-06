# !usr/bin/env python
# -*- coding:utf-8 -*-
# author:chalan630 time:2018/3/2

import requests
import re
from pprint import pprint


def main():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9047'
    r = requests.get(url, verify=False)
    pattern = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'   #正则表达式
    station_name = dict(re.findall(pattern, r.text))
    print(station_name.keys())
    print(station_name.values())
    #pprint(station_name, indent=4)

if __name__ == '__main__':
    main()