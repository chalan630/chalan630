# 12306火车票查询

## 预期目标
- [x] 完整的CLI操作逻辑
- [x] 封装成类

## 知识点
### 列表解析式
[轻松学会Python列表解析式](http://codingpy.com/article/python-list-comprehensions-explained-visually/)  

### docopt和argparse的选择

#### argparse

```Python
import argparse
parser = argparse.ArgumentParser()
parser.parse_args()
```
自带`--help`参数  
```
E:\>test.py --help
usage: test.py [-h]

optional arguments:
  -h, --help  show this help message and exit
```
添加参数方式：  
```Python
创建 ArgumentParser() 对象
调用 add_argument() 方法添加参数
使用 parse_args() 解析添加的参数

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-s", type=int, help="计算一个数的平方")
args = parser.parse_args()

print(args.s**2)
```

>	带短横线和不带短横线的参数区别（个人理解）
	1.带短横线的参数数值紧跟在后，不带的本身内容就是参数值。
	2.带短横线的参数是可选参数，不带的是必须参数
	
#### docopt

官方[github](https://github.com/docopt/docopt)
```
"""Naval Fate.
Usage:
  naval_fate.py ship new <name>...
  naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
  naval_fate.py ship shoot <x> <y>
  naval_fate.py mine (set|remove) <x> <y> [--moored|--drifting]
  naval_fate.py -h | --help
  naval_fate.py --version
Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Naval Fate 2.0')
    print(arguments)
```

`Usage`
大写或者由尖括号括起来的是参数
带一个或者两个短横线是选项，-a -b -c 可以写成 -abc
方括号里的是必选元素，圆括号里的是可选元素，|分隔开互斥元素（多个里选一个），...代表一个或者多个元素。

`Options`
这一部分里的选项另起一行，以短横线开始。
用两个空格分隔开选项和描述。
想添加默认值，则在描述结束后添加 [default: <my-default-value>]


```
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
```
