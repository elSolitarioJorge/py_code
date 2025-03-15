# 类型注解
# 在代码涉及数据交互的地方，提供对数据类型的注解（显示的说明）
# 作用：提高代码可读性，方便他人阅读，方便自己后期维护
# 语法：在变量名后面添加冒号，然后指定数据类型
# 变量: 类型
# 注意：类型注解不会影响代码的运行，只是起到提示作用
# 基础数据类型注解
# a: int = 10
# b: float = 3.14
# c: str = "hello"
# d: bool = True
# 类对象类型注解
# class Student:
#     pass
# stu: Student = Student()
# 基础容器类型注解
# my_list: list = [1, 2, 3]
# my_tuple: tuple = (1, 2, 3)
# my_set: set = {1, 2, 3}
# my_dict: dict = {"name": "张三", "age": 18}
# my_str: str = "hello"
# 容器类型详细注解
# my_list: list[int] = [1, 2, 3]
# my_tuple: tuple[int, str, float] = (1, "hello", 3.14)
# my_set: set[int] = {1, 2, 3}
# my_dict: dict[str, int] = {"name": "张三", "age": 18}
# 注意：
# 元组类型设置类型注解，需要将每个元素都标记出来
# 字典类型设置类型注解，需要将键和值都标记出来

# 也可以在注释中进行类型注解
# 语法：   # type: 类型
# a = 10  # type: int
# b = 3.14  # type: float
# c = "hello"  # type: str
# d = True  # type: bool

# 一般，无法直接看出来变量类型时会添加变量的类型注解
# a: int = random.randint(1, 100)
# b: dict = json.loads(data)
# c: Student = func()

# 注：类型注解只是提示性的，不会对代码运行造成影响
# a: int = "hello" 不会报错

# 函数（方法）的类型注解
# def 函数方法名(形参名: 类型, 形参名: 类型, ...) -> 返回值类型:
# def func(x: int, y: int) -> int:
#     return x + y

# Union类型注解
# Union[类型1, 类型2, ...]
# from typing import Union
# my_list: list[Union[int, str]] = [1, "hello"]
# def func(x: Union[int, str]) -> Union[int, str]:
