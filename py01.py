# print("Hello, world!")
# print("嘿嘿嘿", "牛魔王", sep="|")
# print("快跑 " * 100)
# print(111)
# a = 101
# b = "奶龙"
# c = "牛魔王"
# print(a * 100)
# print(b)
# print(c)
# dog = "猫"
# print(dog)


# a = 1000000000000000000000000000000000000000000000000000000000000000000000000000000
# 鹿 = "马"
# print(鹿)
# print(type(a))
# print(type(鹿))
# print(type(True))
# print(type(1 + 2j))

# name = "奶龙"
# print("你叫" + name + "，今年18岁")
# print("你叫%s，今年18岁" % name)
# print("你叫{0}，今年18岁".format(name))
# print(f"你叫{name}，今年18岁")
# a = 12
# print("%04d" % a)
# b = 3.1415926
# print("%f" % b)
# print("%f" % b)

# money = 50
# print("钱包里有：", money, "元", sep = "")
# money -= 30
# print("买了个原神月卡，钱包里还有：", money, "元", sep = "")
#
# print(type(money))
# print(type("原神"))
# print(type(type(type(1))))

"""
int(x) 将x转换成一个整数
float(x) 将x转换成一个浮点数
str(x) 将x转换成一个字符串
"""

# a = int("12345")
# print(type(a), a)
# b = int(3.1415926)
# print(type(b), b)
# c = float(6)
# print(type(c), c)
# # 想要将字符串转换成数字，必须字符串里全是数字
# d = int("1.1")
# print(type(d), d) # 报错
# e = float("1.1")
# print(type(e), e) # 可以转换
# f = int("abc")
# print(type(f), f) # 报错

# print("1 + 1 =", 1 + 1)
# print("2 - 1 =", 2 - 1)
# print("2 * 3 =", 2 * 3)
# print("4 / 2 =", 4 / 2)
# print("5 // 2 =", 5 // 2)
# print("5 % 2 =", 5 % 2)
# print("2 ** 3 =", 2 ** 3)

# a = """
# 你好
# 我是贝利亚
# """
# print(a)

# a = '"你好，原来你也玩原神"'
# b = "\"你好，原来你也玩原神\""
#
# print(a, b)

# #99乘法表
# i = 1
# while i < 10:
#     j = 1
#     while j <= i:
#         print(f"i * j = {i * j}\t", end="")
#         j += 1
#     print()
#     i += 1
# count = 0
# name = "abhsbdsubdhusbdsocinsodseuousbcuhsbcuesbubsubsube"
# for i in name:
#     if i == "a":
#         count += 1
# print(f"name中有{count}个a")

# for x in range(0, 100, 3):
#     print(x, end = " ")
#
# print("\n")
# print(range(0, 100, 3))
"""
for x in range(1, 10):
    for y in range(1, x + 1):
        print(f"{y} * {x} = {x * y}\t", end="")
    print()
"""
# money = 10000
# for i in range(1, 21):
#     import random
#     score = random.randint(1, 10)
#     if score < 5:
#         print(f"员工{i}绩效分{score}, 不发工资")
#         continue
#     if money >= 1000:
#         print(f"员工{i}绩效分{score}, 发工资1000")
#         money -= 1000
#     else:
#         print(f"钱只有{money}不够了，其他人的先欠着")
#         break

#
# def my_len(str):
#     count = 0
#     for i in str:
#         count += 1
#     print(f"{str}的长度是{count}")
# my_len("你好，世界")
# my_len("我是贝利亚")

# my_list = ["你好", 666, 1.1]
# print(my_list)
# print(type(my_list))


# my_list = [1, 2, 3, 4]
# # print(my_list[0], my_list[1], my_list[2], my_list[3])
# # print(my_list[-1], my_list[-2], my_list[-3], my_list[-4])
# my_list[0] = "111111"
# print(my_list)
# index = my_list.index(2)
# print(index)

"""
mylist = [0, 1, 2]
# 列表.index(元素) 返回元素在列表中的索引
print(mylist.index(1))
# 列表.append(元素) 在列表末尾添加元素
mylist.append(3)
print(mylist)
# 列表.extend(列表) 在列表末尾添加另一个列表
mylist.extend([4, 5, 6])
print(mylist)
# 列表.insert(索引, 元素) 在指定索引处插入元素
mylist.insert(1, 666)
print(mylist)
# 列表.remove(元素) 删除指定元素在列表的第一个匹配项
mylist.remove(666)
print(mylist)
# del 列表[索引] 删除指定索引处的元素
del mylist[0]
print(mylist)
# 列表.pop(索引) 删除指定索引处的元素，并返回该元素
ele = mylist.pop(-1)
print(mylist, f"取出来的元素是{ele}")
# 列表.clear() 清空列表
mylist.clear()
print(mylist)

mylist = [1, 1, 1, 2, 3]
# 列表.count(元素) 返回元素在列表中出现的次数
print(mylist.count(1))
# len(列表) 返回列表的长度
print(len(mylist))

mylist = [2, 6, 7, 3, 1, 0]
# 列表.sort() 对列表进行升序排序
mylist.sort()
print(mylist)
# 列表.reverse() 反转列表
mylist.reverse()
print(mylist)
"""

"""
mylist = [1, 2, 3, 4, 5]
# index = 0;
# while index < len(mylist):
#     print(f"当前索引是{index}, 当前元素是{mylist[index]}")
#     index += 1

for index in range(len(mylist)):
    print(f"当前索引是{index}, 当前元素是{mylist[index]}")
    index -= 1
"""
# t1 = ("a", 1, 3.14)
# t2 = ()
# t3 = tuple()
# print(t1)
# print(type(t1), type(t2), type(t3))
# # 定义单个元素的元组
# # t4 = (1) # 不能这么写
# t4 = (1, ) # 正确写法
# print(t4, type(t4))

# 元组不能修改
# 元组的嵌套
# t5 = ((1, 2, 3), (4, 5, 6))
# for i in range(len(t5)):
#     for j in range(len(t5[i])):
#         print(t5[i][j])

# t6 = (1, 2, 3)
# index = t6.index(1)
# print(index)
# t7 = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
# print(t7.count(1))

# 可以修改元组里面列表的内容
# t9 = (1, 2, [1, 1, 1])
# t9[2].pop(1)
# t9[2].append(101)
# print(t9)

# 字符串也不可修改
# s1 = "hello, world!"
# value1 = s1[2]
# value2 = s1[-1]
# print(f"value1 = {value1}, value2 = {value2}")
#
# value = s1.index("world")
# print(f"在字符串{s1}中查找world，其起始下标是{value}")

# 字符串的替换
# 字符串.replace(被替换的字符串, 替换的字符串) 替换全部，也可以设定替换次数
# 不是修改字符串本身，而是得到一个新的字符串
# s2 = "it is a good day, it is sunny"
# s3 = s2.replace("it", "that")
# print(f"{s2}被修改为{s3}")

# 字符串的分割
# 字符串.split(分隔符) 默认分隔符是空格
# s4 = "hello world it is a good day"
# list4 = s4.split()
# print(f"字符串{s4}被分割为{list4}")

# 字符串的规整
# 字符串.strip() 去掉字符串两端的空格
# 字符串.strip(字符串) 去掉字符串两端的指定字符，按照单个字符去匹配
# s5 = "   1111hello world   "
# print(s5.strip("1"))
# print(s5.strip(" 111"))
#
# # 统计字符串中某字符串出现次数，字符串.count(字符串)
# s6 = "hello world it is a good day"
# print(s6.count("it"))
# # 统计字符串长度，len(字符串)
# print(len(s6))

# # 集合
# my_set = {1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(my_set)  # {1, 2, 3}
# # 添加新元素
# my_set.add("奶龙")
# print(my_set)
# # 移除元素
# my_set.remove(1)
# print(my_set)
# # 随机取出元素
# print(my_set.pop())
# # 清空集合
# my_set.clear()
# print(my_set)

# s1 = {1, 2, 3, 3, 4}
# s2 = {2, 2, 4, 5, 6}
# print(s1)
# print(s2)
# # 取出两个集合的差集
# # 集合1.difference(集合2), 功能：取出集合1和集合2的差集(集合1有而集合2没有的元素)
# # 结果：得到一个新集合, 集合1和集合2的不变
# s3 = s1.difference(s2)
# print(s3)
# # 消除两个集合的差集
# # 集合1.difference_update(集合2)
# # 对比集合1和集合2，在集合1内，删除和集合2相同的元素
# # 结果：集合1被修改，集合2不变
# s1.difference_update(s2)
# print(s1) # {1, 3}
# print(s2) # {2, 4, 5, 6}
# # 合并两个集合
# # 集合1.union(集合2)
# # 将集合1和集合2合成新集合
# # 结果：得到新集合，集合1和集合2不变
# s4 = s1.union(s2)
# print(s4)
# # 统计集合元素数量len()
# print(len(s4))
# # 集合的遍历
# # 集合不支持下标索引，不能用while循环
# # 可以用for循环
# for i in s4:
#     print(f"集合的元素有：{i}")

# 字典 dict  {key: value, key: value, ......, key: value}
# {} / dict()空字典

# # 定义字典
# d1 = {"奶龙": 99, "贝利亚": 100, "迪迦": 67}
# print(d1)
# # 字典和集合一样，不可以使用下标索引
# # 但字典可以通过key值来获取对应的value
# # 语法：字典[key]
# print(d1["奶龙"])
# print(d1["贝利亚"])
# # 定义嵌套字典
# # 字典的key和value可以是任意数据类型(key不可为字典)
# d2 = {
#     "奶龙": {
#         "语文": 140,
#         "英语": 150,
#         "数学": 149
#     },"贝利亚": {
#         "语文": 120,
#         "英语": 130,
#         "数学": 129
#     },"迪迦": {
#         "语文": 145,
#         "英语": 110,
#         "数学": 139
#     }
# }
# print(f"奶龙期末考试成绩：{d2["奶龙"]}")
# print(f"贝利亚期末考试成绩：{d2["贝利亚"]}")
# print(f"迪迦期末考试成绩：{d2["迪迦"]}")
# print(f"学生的考试信息是：{d2}")
# print(f"奶龙的语文成绩是：{d2["奶龙"]["语文"]}")
# # 增加元素
# d1["泰罗"] = 99
# print(d1)
# # 删除元素
# a = d1.pop("迪迦")
# print(f"删除迪迦的分数：{a}之后，字典里还剩{d1}")
# # 清空元素
# print(d2)
# # 获取全部的key
# print(d1.keys(), type(d1.keys()))
# # 遍历字典
# # for i in d1.keys():
# #     print(d1[i])
# # for key in d1:
# #     print(d1[key])
# # 统计字典元素数量
# print(len(d1))
# ### 容器间可以互相转换
# # 通用排序功能  sorted(容器) 升序  sorted(容器, reverse = True)
# print(sorted(d1))
# print(sorted(d1, reverse = True))

# def test_return():
#     return 1, "奶龙"
# a = test_return()
# b = test_return()
# c, d = test_return()
# print(a)
# print(b)
# print(c)
# print(d)

"""
def fun(x, y, z):
    print(f"x = {x}, y = {y}, z = {z}")
# 位置参数：调用函数时根据函数定义的 参数位置来传递参数
# 关键字参数：函数调用时通过“键 = 值”形式传递参数 fun(y = 1, x = 2, z = 3)
# 可以混用，混用时位置参数必须在关键字参数前面，且匹配参数顺序，但关键字参数之间不存在先后顺序
fun(2, z = 10, y = "泥嚎")
# 缺省参数：缺省参数也叫默认参数，用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值
# 注意：所有位置参数必须出现在默认值参数前，包括函数定义和调用
# 作用：当函数调用时没有传递参数，就会使用默认是用缺省参数对应的值
def fun2(name, age, gender = "男"):
    print(f"姓名：{name}, 年龄：{age}, 性别：{gender}")
fun2("奶龙", 18)
fun2("贝利亚", 20, '女')
# 不定长参数：不定长参数就是函数传入的参数个数不确定，可以是0个、1个或者多个
# 语法：在形参前加一个星号 * 可以接收任意多个位置参数，类型为元组
# 也可以加两个星号 ** ，表示接收任意多个关键字参数，类型为字典
# 注意：如果函数中有其他参数，*args参数必须放在最后

def fun3(*args):
    print(args)
fun3("奶龙")
fun3(1, "泥嚎", "贝利亚", "贝塔", "贝塔", "贝塔", "贝塔")
def fun4(**kwargs):
    print(kwargs)
fun4(name = "奶龙", age = 18, gender = "男")
"""

# # 函数作为参数传递
# def func(compute):
#     result = compute(1, 2)
#     print(f"compute参数的类型是{type(compute)}")
#     print(result)
# def compute(x, y):
#     return x + y
# func(compute)
# # 这是一种计算逻辑的传递，而非数据的传递

# 函数定义中：
# def关键字，可以定义有名称的函数
# lambda关键字，可以定义匿名函数(没有名称的函数)
# 有名称的函数，可以基于名称重复使用
# 匿名函数，只能使用一次
# lambda 传入参数: 函数体(一行代码)
# lambda是关键字，表示定义匿名函数
# 传入参数表示匿名函数的形式参数，如：x, y表示接收两个形式参数
# 函数体表示匿名函数的函数体，即函数要执行的操作，只能写一行代码
# def func(compute):
#     result = compute(1, 2)
#     print(f"compute参数的类型是{type(compute)}")
#     print(result)
# func(lambda x, y: x + y)
# 匿名函数用于临时构建一个函数，只用一次的场景，只能写一行代码
# 文件操作
# open()打开函数
# open(name, mode, encoding)
# name：文件路径
# mode：打开文件的模式，r表示只读，w表示写入，a表示追加
# encoding：文件的编码格式，默认为utf-8
# f = open("test.txt", 'r', encoding='utf-8')
# encoding的顺序不是第三位，所以不能用位置参数，用关键字参数来指定
# print(type(f))
# read()方法，读取文件内容
# 文件对象.read(num) num表示读取的字符个数（字节），如果不指定，则表示读取全部内容
# readlines()方法，读取文件内容，按行返回一个列表
# print(f"读取5个字节的结果是：{f.read(5)}") # 我是奶龙！
# print(f"读取全部内容的结果是：{f.read()}") # 我才是奶龙！
# 多次调用 read 方法，会从上次读取的位置继续读取
# lines = f.readlines() # 读取文件全部内容，并封装到列表中
# print(f"lines的类型是{type(lines)}")
# print(f"读取全部内容的结果是：{lines}")
# readline()方法，一次读取一行内容
# f = open("test.txt", 'r', encoding='utf-8')
# line1 = f.readline()
# line2 = f.readline()
# print(f"第一行内容：{line1}")
# print(f"第二行内容：{line2}")
# for line in f:
#     print(f"读取一行内容：{line}")
# 关闭文件 close()方法
# 最后通过close，关闭文件对象，也就是关闭程序对文件的占用
# f.close()
# with open可以在操作完成后自动关闭文件，避免遗忘close
# with open("test.txt", 'r', encoding='utf-8') as f: # f是文件对象
#     for line in f:
#         print(f"读取一行内容：{line}")

# 小练习：统计文件中奶龙出现的次数
# f = open("test.txt", 'r', encoding='utf-8')
# 方法1
# content = f.read()
# count = content.count("奶龙")
# print(content)
# print(f"文件中奶龙出现的次数是：{count}")
# f.close()

# 写入文件
# write()方法，写入文件内容
# 直接调用write()，内容并未真正写入文件，而是会先积攒在程序内存中，称之为缓冲区
# flush()方法，将缓冲区的内容写入文件
# 这样做是避免频繁操作硬盘，导致效率下降
# w 模式，如果文件不存在，会自动创建文件，如果文件存在，会覆盖文件
# f = open("test2.txt", 'w', encoding='utf-8')
# f.write("泥嚎，贝利亚！")
# # f.flush()
# f.close() # close()是内置了flush()的功能的
# import time
# time.sleep(3) # 睡眠

# a 模式，如果文件不存在，会自动创建文件，如果文件存在，会在文件末尾追加内容
# f = open("test.txt", 'a', encoding='utf-8')
# f.write("\n奶龙！奶龙！奶龙！奶龙！奶龙！奶龙！奶龙！奶龙！奶龙！\n你是奶龙，我不是奶龙！\n")
# import time
# time.sleep(3)
# f.close()

# 捕获异常
# try:
#     可能发生错误的代码
# except:
#     如果出现异常执行的代码
#
# try:
#     f = open("test2.txt", 'r', encoding='utf-8')
# except:
#     print("出现异常，因为文件不存在，将用w模式创建文件")
#     f = open("test2.txt", 'w', encoding='utf-8')
#
# 捕获指定异常

# try:
#     print(name)
# except NameError as e:  # 捕获NameError这种异常
#     print("出现异常，因为变量未定义")
#     print(e)  # 打印异常信息
#     print(type(e))

# 捕获多个异常
# 当捕获多个异常时，可以把要捕获的异常类型的名字，放到except后面，
# 并用元组的方式书写，多个异常类型之间用括号括起来，并且用逗号分隔
# try:
#     1 / 0
# except (NameError, ZeroDivisionError) as e:  # 捕获NameError和ZeroDivisionError这两种异常
#     print("出现异常，因为变量未定义 或者 除以0")

# 捕获所有异常
# try:
#     #print(name)
#     #1 / 0
#     f = open("test3.txt", "r", encoding="utf-8")
# except Exception as e:  # 捕获所有异常
#     print("出现异常")
#     print(e)
# else: # 如果没有异常，执行else中的代码，可选
#     print("没有异常，好开心！")
# finally: # 无论是否出现异常，都会执行finally中的代码，可选
#     print("无论是否出现异常，都会执行finally中的代码")
# print("-----------------------------------------")

# 异常具有传递性
# def func1():
#     print("func1() start")
#     1 / 0
#     print("func1() end")
# def func2():
#     print("func2() start")
#     func1()
#     print("func2() end")
# def main():
#     try:
#         func2()
#     except Exception as e:
#         print(f"出现异常，异常信息：{e}")
# main()

# 模块
# 导入方式
# [from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]
# 导入Python内置的time模块(time.py这个代码文件)
# import time
# time.sleep(5) # 通过 . 就可以使用模块内部的全部功能（类、函数、变量）
# 只导入time模块中的sleep函数
from time import sleep
# 使用 * 导入time模块中的全部功能
# from time import *
# sleep(5)  # 可以直接使用
# as定义别名
# 模块定义别名
# import time as t
# t.sleep(5)
# 功能定义别名
# from time import sleep as s
# s(5)
# 自定义模块
import my_module
# my_module.test(1, 2)
# 注意事项：当导入多个模块的时候，且模块内有同名功能，当调用这个同名功能时，调用到的是后面导入的模块的功能
# __main__ 变量
# __all__ 变量
# 如果一个模块文件中有'__all__'变量，那么from 模块名 import *，只能导入这个变量里面列出的功能
from my_module import *
# from my_module import test # 可以手动导入
# test(1, 2)

# Python中的包
# 从物理上看， 包就是一个文件夹，该文件夹下包含了一个__init__.py文件，__init__.py文件是必须的，但内容可以为空
# 该文件夹可用于包含多个模块文件
# 从逻辑上看， 包就是包含了一组功能相近的模块文件的文件，本质依然是模块
# 作用：当我们的模块文件越来越多时，包可以帮助我们管理这些模块，包的作用就是包含多个模块，包的本质依然是模块
# 步骤：
# 1. 创建一个文件夹，文件夹的名字就是包的名字
# 2. 在文件夹内创建一个__init__.py文件，__init__.py文件是必须的，但内容可以为空
# 3. 在文件夹内创建一个模块文件，模块文件的名字就是模块的名字
# 4. 在模块文件中定义功能
# 5. 在其他文件中通过import 包名.模块名 来导入这个模块，然后就可以使用这个模块中的功能了
# 注意事项：
# 1. __init__.py文件的作用是，当导入包的时候，Python解释器会自动去运行__init__.py文件中的代码
# 2. __init__.py文件中定义的变量和功能，都是包的变量和功能，当导入包的时候，包的变量和功能就可以直接使用
# 3. __init__.py文件中定义的变量和功能，都是包的变量和功能，当导入包中的模块的时候，包的变量和功能也可以直接使用
# 4. __init__.py文件中定义的变量和功能，都是包的变量和功能，当导入包中的模块中的功能的时候，包的变量和功能也可以直接使用
# 导入包
# import 包名.模块名
# 包名.模块名.目标
# import my_package.my_module1
# import my_package.my_module2
# my_package.my_module1.func1()
# my_package.my_module2.func2()
# from my_package import my_module1, my_module2
# my_module1.func1()
# my_module2.func2()
# from my_package.my_module1 import func1
# from my_package.my_module2 import func2
# func1()
# func2()
# __all__ 变量
# from my_package import *
# my_module1.func1()
# my_module2.func2()

# 第三方包（非Python官方包）
# 科学计算常用：numpy包
# 数据分析常用：pandas包
# 大数据计算常用的：pyspark、apache-flink包
# 等
# 这些第三方包，Python官方没有提供，需要我们手动下载安装
# 安装第三方包的命令：
# 方法：pip install 包名
# 如果太慢，可用下面命令在指定网址下载
# 方法：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名
# pycharm中安装第三方包：
# 方法：File -> Settings -> Project -> Project Interpreter -> + -> 搜索包名 -> install package
# 如果太慢
# 选项：输入网址 https://pypi.tuna.tsinghua.edu.cn/simple

# 小练习：
# 自定义包'my_utils'
# 包中包含两个模块：str_util.py、file_util.py
# str_util模块中定义两个功能：
# str_reverse(s)：字符串反转
# substr(s, x, y)，按照x,y，对字符串切片
# file_util模块中定义两个功能：
# print_file_info(file_name),接收传入文件的路径，打印文件全部信息，
# 如文件不存在则捕获异常，输出提示信息，通过finally关闭文件
# append_to_file(file_name, data),接收文件路径及传入数据，将数据追加到文件中
# from my_utils import str_util, file_util
# print(str_util.str_reverse('uoy evol i'))
# print(str_util.substr('hello, world', 0, 5))
# file_util.print_file_info('C:/code/python_code/python_study/test.txt')
# file_util.append_to_file('C:/code/python_code/python_study/test.txt', '泥嚎，奶龙！')
# file_util.print_file_info('C:/code/python_code/python_study/test.txt')
# file_util.print_file_info('test.txt')
