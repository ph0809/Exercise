# -*- coding: utf-8 -*-
# -*- author: ph -*-

from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
import random
import logging
import itchat
bot = Bot()    # 机器人对象，用于登陆和操作微信账号，涵盖大部分 Web 微信的功能

# linux执行登录请调用下面这一句
# bot = Bot(console_qr=2, cache_path='botoo.pkl')

"""
wxpy是微信网页版登录的接口，目前账号登录不了
报错信息：
<error>
    <ret>1203</ret>
    <message>为了你的帐号安全，此微信号不能登录网页微信。你可以使用Windows微信或Mac微信在电脑端登录。
    Windows微信下载地址：https://pc.weixin.qq.com  Mac微信下载地址：https://mac.weixin.qq.com
    </message>
</error>
"""


def get_news():
    """获取消息"""
    url = 'http://open.iciba.com/dsapi/'   # 金山词霸每日一句，英文和翻译
    r = requests.get(url)
    logging.info('the result of r is %s'.format(r))
    content = r.json()['content']
    note = r.json()['note']
    logging.info('content is %s, note is %s'.format(content, note))
    return content, note


def send_news():
    """发送消息"""
    try:
        print('----------------start------------------')
        contents = get_news()   # contents是一个元组
        # 你的朋友的微信名称，不是备注，也不是微信账号

        # 这是用Bot()
        # my_friend = bot.friends().search('玮')[0]   # 搜索结果是一个数组，[0]表示取拿到的第一个
        # my_friend.send(contents[0])
        # my_friend.send(contents[1])
        # my_friend.send(u'晚安胖子')

        # 这是用itchat
        itchat.auto_login()
        itchat.send(contents[0], '玮')
        logging.info('all the messages sent successfully!!!')
        # 每86400秒（1天），发送一次
        t = Timer(86400, send_news)
        # 为了防止时间太固定，于是决定对其加上随机数
        ran_int = random.randint(0, 100)
        t = Timer(86400+ran_int, send_news)
        print('----------------end---------------------')
        t.start()

    except:
        # 你的微信名称， 不是微信账号
        my_friend = bot.friends().search('jessie')[0]
        my_friend.send(u'今年消息发送失败了')


if __name__ == '__main__':
    send_news()







