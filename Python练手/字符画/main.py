# !usr/bin/env python
# -*- coding:utf-8 -*-
# author:chalan630 time:2018/3/5

from PIL import Image
import argparse     # 命令行处理

# 命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('file')     # 输入文件
parser.add_argument('-o', '--output')   # 输出文件

def get_char(r, g, b, alpha = 256):
    gray = int((2126 * r + 7152 * g + 722 * b) / 10000)
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvun"
                      "xrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    index = int((gray / int(alpha + 1)) * len(ascii_char))
    return ascii_char[index]

if __name__ == '__main__':
    args = parser.parse_args()
    IMG = args.file
    out_file_name = args.output
    im = Image.open(IMG)
    width_t = im.size[0]    #获得图片尺寸
    height_t = im.size[1]
    width = int(width_t / 5)    #对原图进行缩放
    height = int(height_t / 5)
    im = im.resize((width, height), Image.NEAREST)
    # print(type(width))
    txt = ""
    for i in range(height):
        for j in range(width):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    print(txt)

    if out_file_name:
        with open(out_file_name, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)
