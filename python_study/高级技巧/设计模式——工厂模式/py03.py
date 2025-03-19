# 工厂模式
# 当需要大量创建一个类的实例时，可以使用工厂模式
# 即从原生的使用类的构造去创建对象的形式
# 迁移到，基于工厂提供的方法去创建对象的形式

# 示例
# class Person:
#     pass
#
# class Worker(Person):
#     pass
#
# class Student(Person):
#     pass
#
# class Teacher(Person):
#     pass
#
# worker = Worker()
# student = Student()
# teacher = Teacher()

# 使用工厂模式
# class Person:
#     pass
#
# class Worker(Person):
#     pass
#
# class Student(Person):
#     pass
#
# class Teacher(Person):
#     pass
#
# class Factory:
#     def get_person(self, p_type):
#         if p_type == 'w':
#             return Worker()
#         elif p_type == 's':
#             return Student()
#         else:
#             return Teacher()
#
# factory = Factory()
# worker = factory.get_person('w')
# student = factory.get_person('s')
# teacher = factory.get_person('t')

# 使用工厂类的get_person()方法去创建具体的对象
# 优点：
# 大批量创建对象的时候有统一的入口，易于代码维护
# 当发生修改，仅修改工厂类的创建方法即可
# 符合现实世界的模式，即由工厂来制作产品（对象）


