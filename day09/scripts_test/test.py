# -*- coding: utf-8 -*-
# -*- author: ph -*-
# import asyncio
#
# loop = asyncio.get_event_loop()
#
#
# @asyncio.coroutine
# def make_tea(variety):
#     print('Now making %s tea.' % variety)
#     return '%s tea' % variety
#
#
# def confirm_tea(future):
#     print('The %s is made.' % future.result())
#
# # task = asyncio.async(make_tea('green'))
# task = make_tea('green')
# task.add_done_callback(confirm_tea)
#
# loop.run_until_complete(task)

import requests
from bs4 import BeautifulSoup

"""获取ONE上面的每日一句"""
class get_one():
    def get_dictnum_info(self):
        print("获取格言信息。。。")
        user_url = 'http://wufanzhuce.com/'
        resp = requests.get(url=user_url, headers=self.headers)
        soup_text = BeautifulSoup(resp.text, 'lxml')

        every_msg = soup_text.find_all('div', class_='fp_one_cita')[0].find('a').text
        return every_msg

a = get_one()
print(a.get_dictnum_info())