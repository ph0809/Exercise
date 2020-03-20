# -*- coding: utf-8 -*-
# -*- author: ph -*-
"""获取当前文件路径以及父文件路径的方法"""
import os


def TestPrtPwd():
    path1 = os.path.realpath(__file__)
    print("当前文件的路径：", path1)

    parent = os.path.dirname(os.path.realpath(__file__))
    print("获取父目录：", parent)

    grader = os.path.dirname(parent)
    print("获取父目录的父目录：", grader)

    print("获取文件名：", os.path.basename(path1))

    pwd = os.getcwd()
    print("当前运行文件路径" + pwd)

    # 当前文件的父路径
    father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
    print("当前文件的父路径", father_path)

    # 当前文件的两级目录
    grader_father = os.path.abspath(os.path.dirname(pwd) + os.path.sep + "..")
    print("当前文件的两级目录", grader_father)


if __name__ == '__main__':
    TestPrtPwd()

