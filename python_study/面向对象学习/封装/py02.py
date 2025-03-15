# 面向对象编程，是许多编程语言都支持的一种编程思想
# 简单理解：基于模板（类）去创建实体（对象），使用对象完成功能开发
# 面向对象三大特性：封装、继承、多态
# 封装：将属性和方法封装到类中，通过对象调用
#
# 对用户隐藏的属性和行为：
# 现实世界中的事物，有属性和行为
# 但不代表这些属性和行为都是开放给用户使用的
# 作为现实事物在程序中映射的类，也应该支持
#
# 类中提供了私有成员的形式来支持：
# 定义私有成员：
# 私有成员变量：变量名以__开头
# 私有成员方法：方法名以__开头
# 私有成员只能在类内部使用，不能在类外部使用
# class Phone:
#     __current_voltage = 1 # 当前电压
#
#     def __keep_single_core(self):
#         print("使用单核运行")
#     # 私有成员无法被类对象使用，但是可以被其他成员使用
#     def call_by_5g(self):
#         if self.__current_voltage > 5:
#             print("5g通话已开启")
#         else:
#             self.__keep_single_core()
#             print("当前电量不足，无法开启5g通话，并已开启单核模式")
#
# phone = Phone()
# # print(phone.__current_voltage) # 报错，无法访问
# # phone.__keep_single_core()     # 报错，无法访问
# phone.call_by_5g()

# 私有成员的意义：
# 在类中提供仅供内部使用的属性和方法、而不对外开放（类对象无法使用）

# 设计一个类，用来描述手机
# class Phone:
#     # 提供私有成员变量：__is_5g_enable
#     __is_5g_enable = False
#
#     # 提供私有成员方法：__check_5g()
#     def __check_5g(self):
#         if self.__is_5g_enable:
#             print("5g开启")
#         else:
#             print("5g关闭，使用4g网络")
#     def call_by_5g(self):
#         self.__check_5g()
#         print("正在通话中")
# phone = Phone()
# phone.call_by_5g()
