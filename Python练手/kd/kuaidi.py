# !usr/bin/env python
# -*- coding:utf-8 -*-
# author:chalan630 time:2018/3/13

import requests
from prettytable import PrettyTable

# 从快递100获得快递公司代码
url_one = 'https://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text={}'
url_two = 'https://www.kuaidi100.com/query?type={}&postid={}'

class MyKuaidi:
    headers = "时间 状态".split()

    def __init__(self, number):
        self.number = number

    def get_comCode(self):
        url = url_one.format(self.number)
        r = requests.get(url)
        company_code = r.json()['auto'][0]['comCode']
        return company_code

    def print_info(self):
        pt = PrettyTable()
        pt._set_field_names(self.headers)
        url = url_two.format(self.get_comCode(), self.number)
        r = requests.get(url)
        contexts = r.json()['data']
        for sub in range(len(contexts)):
            info = contexts[sub]
            time = info['time']
            context = info['context']
            pt.add_row([time, context])
        print(pt)

if __name__ == '__main__':
    number = input('请输入快递单号:')
    MyKuaidi(number).print_info()

