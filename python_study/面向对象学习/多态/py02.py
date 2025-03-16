# 多态，指的是：多种状态，即完成某个行为时，使用不同的对象会得到不同的状态
# 多态的体现：一个对象可以有多种形态
# 同样的行为（函数），传入不同的对象，得到不同的状态
# 多态常作用在继承关系上
# 比如：
# 函数（方法）形参声明接受父类对象
# 实际调用时，传入子类对象
# class Animal:
#     def speak(self):
#         pass
#
# class Dog(Animal):
#     def speak(self):
#         print("汪汪汪")
#
# class Cat(Animal):
#     def speak(self):
#         print("喵喵喵")
#
# def make_noise(animal: Animal):
#     animal.speak()
#
# dog = Dog()
# cat = Cat()
# make_noise(dog)
# make_noise(cat)

# 抽象类（接口）
# 含有抽象方法的类称之为抽象类
# 抽象方法：方法体是空实现的（pass）称之为抽象方法
# 配合多态，完成
# 抽象的父类设计（设计标准）
# 具体的子类实现（实现标准）

# class AC:
#     def cool_wind(self):
#         """制冷"""
#         pass
#     def warm_wind(self):
#         """制热"""
#         pass
#     def blow(self):
#         """吹风"""
#         pass
#
# class GreeAC(AC):
#     def cool_wind(self):
#         print("格力空调制冷")
#     def warm_wind(self):
#         print("格力空调制热")
#     def blow(self):
#         print("格力空调吹风")
#
# class HaierAC(AC):
#     def cool_wind(self):
#         print("海尔空调制冷")
#     def warm_wind(self):
#         print("海尔空调制热")
#     def blow(self):
#         print("海尔空调吹风")
#
# def use_ac(ac: AC):
#     ac.cool_wind()
#     ac.warm_wind()
#     ac.blow()
#
# gree = GreeAC()
# haier = HaierAC()
# use_ac(gree)
# use_ac(haier)

# 抽象类多用于做顶层设计（设计标准），以便子类做具体实现
# 也是对子类的一种软性约束，要求子类必须复写（实现）父类的一些方法
# 配合多态使用，获得不同的工作状态
