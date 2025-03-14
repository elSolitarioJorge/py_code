# 使用对象组织数据
# 设计类(class)
class Student:
    name = None         # 姓名
    gander = None       # 性别
    nationality = None  # 国籍
    origin = None       # 籍贯
    age = None          # 年龄
# 创建对象
stu1 = Student()
# 对象属性赋值
stu1.name = "奶龙"
stu1.gander = "外星人"
stu1.nationality = "M78星云"
stu1.origin = "光之国"
stu1.age = 1000
# 获取对象信息
print(stu1.name, stu1.gander, stu1.nationality, stu1.origin, stu1.age)

