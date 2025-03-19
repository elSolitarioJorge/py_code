# 闭包
# 在函数嵌套的前提下，内部函数使用了外部函数的变量，
# 并且外部函数返回了内部函数，我们把这个使用外部函数变量的内部函数称为闭包

# 简单闭包
# def outer(logo):
#
#     def inner(msg):
#         print(f"<{logo}>{msg}<{logo}>")
#
#     return inner
#
# fn1 = outer("贝利亚")
# fn1("奶龙")
# fn1("快跑")
#
# fn2 = outer("奶龙")
# fn2("打死贝利亚")
# fn2("贝利亚似了")

# nonlocal关键字修改外部函数的值
# def outer(num1):
#
#     def inner(num2):
#         nonlocal num1
#         num1 += num2
#         print(num1)
#
#     return inner
#
# fn = outer(10)
# fn(10)
# fn(10)
# fn(10)
# fn(10)

# 使用闭包实现ATM小案例
# def account_create(initial_account = 0):
#
#     def atm(num, deposit = True):
#         nonlocal initial_account
#         if deposit:
#             initial_account += num
#             print(f"存款：+{num}，账户余额：{initial_account}")
#         else:
#             initial_account -= num
#             print(f"取款：-{num}，账户余额：{initial_account}")
#
#     return atm
#
# atm = account_create()
# atm(1000)
# atm(800)
# atm(1200, False)

# 闭包注意事项
# 优点：使用闭包可以让我们得到：
# 无需定义全局变量即可实现通过函数，持续的访问、修改某个值
# 闭包使用的变量的作用域在函数内，难以被错误的调用修改
# 缺点：
# 由于内部函数持续引用外部函数的值，所以会导致这一部分内存空间不被释放，一直占用内存
