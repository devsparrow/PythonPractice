# https://github.com/Yixiaohan/show-me-the-code  第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import random


list = []
counter = 1
while counter <= 200:
    rd =  random.randint(100000,999999)         # 产生 1 到 10 的一个整数型随机数
    if rd not in list:
        counter += 1
        list.append(rd)


print(list)