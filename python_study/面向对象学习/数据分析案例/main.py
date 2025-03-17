"""
面向对象，数据分析案例，主业务逻辑代码
实现步骤：
1.设计一个类，可以完成数据的封装
2.设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
3.读取文件，生产数据对象
4.进行数据需求的逻辑计算
5.通过PyEcharts进行图形绘制
"""

from file_define import FileReader, TextFileReader, JsonFileReader
from data_define import Student
from pyecharts.charts import Bar          # 构建柱状图
from pyecharts.options import *           # 配置项
from pyecharts.globals import ThemeType   # 主题类型

text_file_reader = TextFileReader("students.csv")
json_file_reader = JsonFileReader("students.jsonl")

class1_students: list[Student] = json_file_reader.read_data()
class_other_students: list[Student] = text_file_reader.read_data()

# 将两个班学生合并为1个list来存储
all_students: list[Student] = class1_students + class_other_students

# 统计每个班总分大于500的人数
students_dict = {}
for student in all_students:
    if student.class_ not in students_dict:
        students_dict[student.class_] = 0
    if student.total > 500:
        students_dict[student.class_] += 1

# 可视化图开发
bar = Bar(init_opts = InitOpts(theme = ThemeType.LIGHT))

bar.add_xaxis(list(students_dict.keys()))    # 添加x轴数据
bar.add_yaxis("总分大于500的人数", list(students_dict.values()))    # 添加y轴数据
bar.set_global_opts(title_opts = TitleOpts(title = "各班总分大于500的人数"))    # 设置标题

bar.render("各班总分大于500的人数柱状图.html")