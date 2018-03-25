import itchat
from itchat.content import *
import urllib
import json

@itchat.msg_register(itchat.content.TEXT)   #itchat默认


def text_reply(msg):
    info = msg['Text'].encode('UTF-8')
    url = 'http://www.tuling123.com/openapi/api'
    data = {"key":"apikey","info":info,"userid":"username"}
    data = urllib.parse.urlencode(data).encode(encoding='UTF8')
    request = urllib.request.Request(url, data)
    response = urllib.request.urlopen(request)
    re_info_str = response.read()
    re_info_dict = json.loads(re_info_str)    #str转成dict
    print ('Reply message is:',re_info_dict)
    if re_info_dict['code'] == 100000:  #返回数据格式为文本类
        itchat.send(re_info_dict['text'], msg['FromUserName']) #itchat信息发送     回复信息与回复者用户名
#   return '%s' % re_info_dict['text']

itchat.auto_login(hotReload = True, enableCmdQR = 1) #登陆

#mps = itchat.get_mps()
#print(mps)

itchat.run()    #运行
