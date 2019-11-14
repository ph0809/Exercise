
# -*- coding: utf-8 -*-
# -*- author: ph -*-
class Game:
    top_score = 0

    def __init__(self, name):
        self.name = name

    @staticmethod
    def show_top():   # 静态函数
        print("显示游戏规则")

    @classmethod      # 类函数
    def show_top_score(cls):
        print("历史最高分：%s" % cls.top_score)

    def start_game(self):     # 实例函数
        print("%s start game" % self.name)