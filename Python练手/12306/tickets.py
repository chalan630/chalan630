# !usr/bin/env python
# -*- coding:utf-8 -*-
# author:chalan630 time:2018/3/2

"""Train tickets query via command-line.

Usage:
    tickets [-gdktz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

"""

from docopt import docopt
import stations_name
from datetime import datetime
import requests
from colorama import Fore
from prettytable import PrettyTable
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



class TrainCollection(object):
    headers = '车次 车站 时间 历时 商务座 一等座 二等座 硬座 无座 软卧 硬卧 能否网上购票'.split()

    def __init__(self, raw_trains, options):
        self.raw_trains = raw_trains
        self.options = options

    def colored(self, color, string):
        return ''.join([getattr(Fore, color.upper()), string, Fore.RESET])

    def get_from_to_station_name(self, data_list):
        from_station_code = data_list[6]
        from_station_name = stations_name.get_name(from_station_code)
        to_station_code = data_list[7]
        to_station_name = stations_name.get_name(to_station_code)
        return '\n'.join([
            self.colored('green',from_station_name),
            self.colored('red',to_station_name)
        ])

    def get_start_arrive_time(self, data_list):
        start_time = data_list[8]
        arrive_time = data_list[9]
        return '\n'.join([
            self.colored('green', start_time),
            self.colored('red', arrive_time)
        ])

    def CanWebBuy(self, data_list):
        if data_list[11] == 'Y':
            return '能'
        else:
            return '不能'

    def parse_train_data(self, data_list):
        return {
            'train_code':data_list[3],
            'from_to_station_name': self.get_from_to_station_name(data_list),
            'start_arrive_time': self.get_start_arrive_time(data_list),
            'lishi': data_list[10],
            'business_seat': data_list[32] or '--',
            'first_class_seat': data_list[31] or '--',
            'second_class_seat': data_list[30] or '--',
            'hard_seat': data_list[29] or '--',
            'no_seat': data_list[26] or '--',
            'soft_sleep': data_list[23] or '--',
            'hard_sleep': data_list[28] or '--',
            'canWebBuy': self.CanWebBuy(data_list)
        }

    def need_print(self, data_list):
        train_code = data_list[3]
        initial = train_code[0].lower()
        return (not self.options or initial in self.options)

    @property
    def trains(self):
        for train in self.raw_trains:
            data_list = train.split('|')
            if self.need_print(data_list):
                yield self.parse_train_data(data_list).values()

    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.headers)
        for train in self.trains:
            pt.add_row(train)
        print(pt)


class Cli(object):
    url_template = (
        'https://kyfw.12306.cn/otn/leftTicket/queryZ?'
        'leftTicketDTO.train_date={}&'
        'leftTicketDTO.from_station={}&'
        'leftTicketDTO.to_station={}&'
        'purpose_codes=ADULT'
    )

    def __init__(self):
        self.arguments = docopt(__doc__, version='Tickets 2.0')
        self.from_station = stations_name.get_code(self.arguments['<from>'])
        self.to_station = stations_name.get_code(self.arguments['<to>'])
        self.date = self.arguments.get('<date>')
        self.check_arguments_validity()
        self.options = ''.join([key for key, value in self.arguments.items() if value is True])

    @property
    def request_url(self):
        return self.url_template.format(self.date, self.from_station, self.to_station)

    def check_arguments_validity(self):
        if self.from_station is None or self.to_station is None:
            print(u'请输入有效的车站名称')
            exit()
        try:
            if datetime.strptime(self.date, '%Y-%m-%d') < datetime.now():
                raise ValueError
        except:
            print(u'请输入有效日期')
            exit()

    def run(self):
        r = requests.get(self.request_url)
        trains = r.json()['data']['result']
        TrainCollection(trains, self.options).pretty_print()

if __name__ == '__main__':
    Cli().run()
