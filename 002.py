#做为 Apple Store App 独立开发者，
# 你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
import random as rd
import pymysql as sql

list = ['1','2','3','4','5','6','7','8','9','10','1','2','3','4','5','6','7','8','9','10','a','b','c']
list1 = []
for i in range(0,200):
    rd.shuffle(list)
    list1.append("".join(list))



