# 装饰器其实也是一种闭包，其功能就是在不破坏目标函数原有的代码和功能的前提下，为目标函数增加新功能

# 装饰器的一般写法（闭包）
# def outer(func):
#
#     def inner():
#         print("奶龙睡觉了")
#         func()
#         print("奶龙起床了")
#
#     return inner
#
# def sleep():
#     import random
#     import time
#     print("睡眠中......")
#     time.sleep(random.randint(4, 5))
#
# fn = outer(sleep)
# fn()

# 装饰器的语法糖写法
# def outer(func):
#
#     def inner():
#         print("奶龙睡觉了")
#         func()
#         print("奶龙起床了")
#
#     return inner
# @outer
# def sleep():
#     import random
#     import time
#     print("睡眠中......")
#     time.sleep(random.randint(4, 5))
#
# sleep()

