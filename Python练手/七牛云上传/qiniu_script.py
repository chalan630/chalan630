# !usr/bin/env python
# -*- coding:utf-8 -*-
# author:chalan630 time:2018/3/6

import qiniu
import os
import sys
import urllib
import subprocess

# 七牛云SDK
access_key = ""
secret_key = ""

# 构建鉴权对象
q = qiniu.Auth(access_key, secret_key)

# 要上传的空间
bucket_name = ""

# 外链格式字典
bucket_url = {
    "": ""
}

# 主程序

# 图片文件特征
flag = ("jpeg", "jpg", "png", "gif", "bmp")

result_file = "上传结果.txt"
if os.path.exists(result_file):
    os.remove(result_file)

class Qiniu(object):
    def __init__(self, AccessKey, SecretKey):
        self.AccessKey = AccessKey
        self.SecretKey = SecretKey
        self._q = qiniu.Auth(self.AccessKey, self.SecretKey)

    def upload_file(self, bucket_name, up_filename, file_path):
        token = self._q.upload_token(bucket_name, up_filename, 3600)
        ret, info = qiniu.put_file(token, up_filename, file_path)
        url = self.get_file_url(bucket_name, up_filename)
        return ret, info, url

    def get_file_url(self, bucket_name, up_filename):    # 根据规则生成url
        if not bucket_name in bucket_url.keys():
            raise AttributeError("空间名不正确！")
        url_prefix = bucket_url[bucket_name]
        url = url_prefix + urllib.parse.quote(up_filename)
        return url

def save(filename, url):
    line = "[%s](%s)\n" % (filename, url)
    # 如果是图片则生成图片的markdown格式引用
    if filename.split('.')[1] in flag:
        line = "!" + line
    with open(result_file, "a", encoding="utf-8") as f:
        f.write(line)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("请选择要上传的图片")
        sys.exit(0)
    files = sys.argv[1:]        # 支持多文件同时上传

    q = Qiniu(access_key, secret_key)
    for file in files:
        if os.path.isdir(file):
            """
            sys.argv[1][-3:]
            list = sys.argv[1].split('.')
            list[1]
            """
            print("不支持目录上传！")
        if os.path.isfile(file):
            name = file.split('.')[0].split('\\')[-1]
            fullname = file.split('\\')[-1]
            suffix = file.split('.')[1]
            prefix = "img/" if suffix in flag else"file/"
            up_filename = prefix + name
            ret, info, url = q.upload_file(bucket_name, up_filename, file)
            print("已上传：%s" %name)
            save(fullname, url)
    subprocess.call(result_file, shell=True)
