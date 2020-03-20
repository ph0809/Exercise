# -*- coding: utf-8 -*-
# -*- author: ph -*-

import xlsxwriter
import pandas as pd


"""
DataFrame有四个重要的属性
index:行索引
columns:列索引
values:值的二维数组
name:名字
"""

"""将数据以Excel的形式导出"""
def write_as_excel():
    # 输入数据
    df = pd.DataFrame({'name': ['meat', 'rice'], 'price': [12, 3], 'quantity': [10, 100]})

    # 创建xlsx文件
    workbook = xlsxwriter.Workbook('products.xlsx')

    # 新增工作簿
    worksheet = workbook.add_worksheet()

    # 设置单元格格式   字体加粗，字体蓝色，背景紫色
    format_columname = workbook.add_format({'bold': True, 'font_color': 'blue', 'bg_color': 'purple'})
    # 设置价格的数值格式，并添加下划线
    format_price = workbook.add_format({'num_format': '$#,##0', 'underline': True})
    # 设置字体
    format_products = workbook.add_format({'font_name': 'Times New Roman'})

    # 向工作表中写入数据
    for col in range(len(df.columns)):   # 只是第一行的数据
        worksheet.write(0, col, df.columns[col], format_columname)   # 行、列、数据、数据格式

    # 分别写入元素
    for row in range(2):
        worksheet.write(row+1, 0, df.name[row])
    for row in range(2):
        worksheet.write(row+1, 1, df.price[row], format_price)
    for row in range(2):
        worksheet.write(row+1, 2, df.quantity[row], format_products)

    workbook.close()


if __name__ == '__main__':
    write_as_excel()
