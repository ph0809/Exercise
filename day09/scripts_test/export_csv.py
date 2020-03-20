# -*- coding: utf-8 -*-
# -*- author: ph -*-

from bs4 import BeautifulSoup
import os
import time
import csv
import codecs

"""
1.打开文件夹，获取到文件的路径，从而获取到文件的名字，因为文件有多个，使用os模块的函数来解析文件
"""
def open_file(fileName):
    """读取XML内的文件数据并存入CSV格式的文件----可使用EXCEL打开"""
    file_folder = '/Users/diyidan/Desktop/Exercises/Exercise/day09/scripts_test'    # 文件夹的位置
    if os.path.isdir(file_folder):
        for fileName in os.listdir(file_folder):
            print(fileName)
            info(fileName)    # 读取文件名字，fileName就是文件名


def info(fileName):
    """
    2.获取到文件的名字后，使用bs4模块打开文件，由于有多个文件，所以将解析过程写入函数
    """
    soup = BeautifulSoup(open('/Users/diyidan/Desktop/Exercises/Exercise/day09/scripts_test/'+fileName))
    a = soup.find_all('part')
    info = []
    for i in a:
        dt = []
        # dt.append(i.find('id').get_text().strip())
        dt.append(i.find('name').get_text().strip())
        dt.append(i.find('age').get_text().strip())
        dt.append(i.find('sex').get_text().strip())
        # dt.append( i.find('XXX').get_text().strip())
        # dt.append(i.find('XXX').get_text().strip())
        # dt.append(float(i.find('XXX').get_text().strip()) + float(i.find('XXX').get_text().strip()))
        info.append(dt)

        """
        3.将数据写入csv文件，这里的数据都是list格式，并且需要遍历
        """
        with open('/Users/diyidan/Desktop/Exercises/Exercise/day09/scripts_test/Ex_info.csv', 'a', encoding='utf-8') as csvfile:   # 'ab+'去除空白行，又叫换行
            # csvfile.write(codecs.BOM_UTF8)    # 存入表内的文字格式
            # fieldnames = ['name', 'age', 'sex']
            writer = csv.writer(csvfile)    # 存入表时所使用的格式
            writer.writerow(['name', 'age', 'sex'])   # 这里的表头和我们上面获取的数据列一致
            writer.writerows(info)   # 写入表


if __name__ == '__main__':
    open_file('for_xml_test.xml')

