# -*- coding: utf-8 -*-
# -*- author: 彭慧 -*-

# for i in range(1, 5):
#     for j in range(1, i+1):
#         print('*', end='')
#     print('')


row = int(input("please input the value:"))

# for i in range(row):
#     for j in range(row):
#         if j < row-i-1:
#             print('', end='')
#         else:
#             print('*', end='')
#     print()


# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()

for i in range(row):
    for j in range(row-i-1):
        print(' ', end='')
    for j in range(2*i+1):
        print('*', end='')
    print()
