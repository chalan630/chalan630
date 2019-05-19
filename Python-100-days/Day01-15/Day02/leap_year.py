"""
输入年份 如果是闰年输出True 否则输出False

Version: 0.1
"""

year = int(input("请输入年份："))
is_leap = (year % 4 == 0 & \
	year % 100 != 0 | year % 400 == 0)
if is_leap:
	print('是闰年')
else:
	print('不是闰年')
