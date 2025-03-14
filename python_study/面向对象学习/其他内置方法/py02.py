# 魔术方法
# __init__ 构造方法
# __str__  字符串方法
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# student = Student('奶龙', 18)
# print(student)      # <__main__.Student object at 0x000001D3A8B7E6A0>
# print(str(student)) # <__main__.Student object at 0x000001D3A8B7E6A0>
# 当类对象需要被转换为字符串时，会输出如上结果（内存地址）
# 内存地址没有多大作用，我们可以通过__str__方法，控制类转换为字符串的行为
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"Student类对象，name = {self.name}，age = {self.age}"
# student = Student('奶龙', 18)
# print(student)      # Student类对象，name = 奶龙，age = 18
# print(str(student)) # Student类对象，name = 奶龙，age = 18

# __lt__    小于、大于符号比较
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# stu1 = Student("奶龙", 18)
# stu2 = Student("贝利亚", 19)
# print(stu1 > stu2) # TypeError
# 直接对两个对象进行比较是不可以的，但是在类中实现__lt__方法，即可同时完成小于符号和大于符号两种比较
# __le__    小于等于、大于等于符号比较
# __eq__    等于符号比较
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __lt__(self, other):
#         return self.age < other.age
#
#     def __le__(self, other):
#         return self.age <= other.age
#     def __eq__(self, other):
#         return self.age == other.age
# stu1 = Student("奶龙", 18)
# stu2 = Student("贝利亚", 19)
# stu3 = Student("迪迦", 18)
# print(stu1 < stu2)  # True
# print(stu1 > stu2)  # False
# print(stu1 <= stu2) # True
# print(stu1 == stu3) # True
