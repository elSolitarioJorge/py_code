# 设计模式
# 设计模式是一种编程套路，可以极大地方便程序的开发
# 最常见、最经典的设计模式，就是我们所学的面向对象
# 除了面向对象外，在编程中也有很多既定的套路可以方便开发，称之为设计模式：
# 单例、工厂模式
# 建造者、责任链、状态、备忘录、解释器、访问者、观察者、中介、模板、代理模式
# 等等

# 单例模式
# 单例模式是一种常见的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在
# 在整个系统中，某个类只能出现一个实例时，单例模式就能派上用场
# 定义：保证一个类只有一个实例，并提供一个访问它的全局访问点
# 适用场景：当一个类只能有一个实例时，而客户可以从一个众所周知的访问点访问它时
# 节省内存
# 节省创建对象的开销

# 非单例模式演示
# class StrTools:
#     pass
#
# s1 = StrTools()
# s2 = StrTools()
# print(s1)     # <__main__.StrTools object at 0x0000025BAB72A660>
# print(s2)     # <__main__.StrTools object at 0x0000025BAB862490>

# 单例模式演示
# from str_tools import str_tool
#
# s1 = str_tool
# s2 = str_tool
# print(s1)      # <str_tools.StrTools object at 0x000001FB70D0A660>
# print(s2)      # <str_tools.StrTools object at 0x000001FB70D0A660>


