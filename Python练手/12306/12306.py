# !usr/bin/env python
# -*- coding:utf-8 -*-
# author:chalan630 time:2018/3/1

"""Train tickets query via command-line.

Usage:
  tickets [-gdtkz] <from> <to> <date>

Options:
  -h,--help    显示帮助菜单
  -g        高铁
  -d        动车
  -t        特快
  -k        快速
  -z        直达

Example:
  tickets 南京 北京 2016-07-01
  tickets -dg 南京 北京 2016-07-01
"""


from docopt import docopt
import stations_name
import requests
from colorama import Fore
from prettytable import PrettyTable

def cli():
    arguments = docopt(__doc__, version='Tickets 1.0')
    from_station = stations_name.get_code(arguments.get('<from>'))     #None为没有获取时的默认值
    to_station = stations_name.get_code(arguments.get('<to>'))
    date = arguments.get('<date>')
    options = ''.join([key for key, value in arguments.items() if value is True])       #参数生效
    url = ('https://kyfw.12306.cn/otn/leftTicket/queryZ?'
           'leftTicketDTO.train_date={}&'
           'leftTicketDTO.from_station={}&'
           'leftTicketDTO.to_station={}&'
           'purpose_codes=ADULT').format(date, from_station, to_station)
    r = requests.get(url)
    raw_trains = r.json()['data']['result']

    pt = PrettyTable()                  #规范表格格式
    pt._set_field_names('车次 车站 时间 历时 商务座 一等座 二等座 硬座 无座 软卧 硬卧 能否网上购票'.split())
    for raw_train in raw_trains:
        data_list = raw_train.split('|')
        train_code = data_list[3]
        initial = train_code[0].lower()

        if not options or initial in options:       #参数生效
            from_station_code = data_list[6]
            from_station_name = stations_name.get_name(from_station_code)
            to_station_code = data_list[7]
            to_station_name = stations_name.get_name(to_station_code)
            start_time = data_list[8]
            arrive_time = data_list[9]
            lishi = data_list[10]
            canWebBuy = data_list[11]
            soft_sleep = data_list[23] or '--'
            no_seat = data_list[26] or '--'
            hard_sleep = data_list[28] or '--'
            hard_seat = data_list[29] or '--'
            second_class_seat = data_list[30] or '--'
            first_class_seat = data_list[31] or '--'
            business_seat = data_list[32] or '--'
            pt.add_row([train_code,
                        '\n'.join([Fore.GREEN + from_station_name + Fore.RESET, Fore.RED + to_station_name + Fore.RESET]),
                        '\n'.join([Fore.GREEN + start_time + Fore.RESET, Fore.RED + arrive_time + Fore.RESET]),
                        lishi,
                        business_seat,
                        first_class_seat,
                        second_class_seat,
                        hard_seat,
                        no_seat,
                        soft_sleep,
                        hard_sleep,
                        canWebBuy
                        ])

    print(pt)

if __name__ == '__main__':
    cli()

    #pprint(stations_name, indent=4)
