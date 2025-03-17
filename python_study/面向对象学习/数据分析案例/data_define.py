"""
定义数据类
"""

class Student:

    def __init__(self,
                 id: str,
                 name: str,
                 class_: int,
                 chinese: float,
                 math: float,
                 english: float,
                 physics: float,
                 chemistry: float,
                 biology: float,
                 lizong: float,
                 total: float):
        self.id = id               # 学号
        self.name = name           # 姓名
        self.class_ = class_       # 班级
        self.chinese = chinese     # 语文成绩
        self.math = math           # 数学成绩
        self.english = english     # 英语成绩
        self.physics = physics     # 物理成绩
        self.chemistry = chemistry # 化学成绩
        self.biology = biology     # 生物成绩
        self.lizong = lizong       # 理综成绩
        self.total = total         # 总分

    def __str__(self):
        return f"{self.id},{self.name},{self.class_},{self.chinese},{self.math},{self.english},{self.physics},{self.chemistry},{self.biology},{self.lizong},{self.total}"

