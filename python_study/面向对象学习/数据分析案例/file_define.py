"""
文件相关的类定义
"""
from data_define import Student
import json

# 先定义一个抽象类用来做顶层设计，确定有哪些功能需要实现
class FileReader:

    def read_data(self) -> list[Student]:
        """读取文件数据，读到的每一条数据都转换为Student对象，将他们封装到list内返回"""
        pass

class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path     # 定义成员变量记录文件路径

    # 复写（实现抽象方法）父类的方法
    def read_data(self) -> list[Student]:
        f = open(self.path, "r", encoding = "UTF-8")

        student_list: list[Student] = []
        for line in f.readlines():
            line = line.strip()   # 消除每一行读取到的'\n'
            data_list = line.split(",")
            student = Student(data_list[0], data_list[1], int(data_list[2]), float(data_list[3]), float(data_list[4]), float(data_list[5]), float(data_list[6]), float(data_list[7]), float(data_list[8]), float(data_list[9]), float(data_list[10]))
            student_list.append(student)

        f.close()
        return student_list


class JsonFileReader(FileReader):

    def __init__(self, path):
        self.path = path  # 定义成员变量记录文件路径

    # 复写（实现抽象方法）父类的方法
    def read_data(self) -> list[Student]:
        f = open(self.path, "r", encoding="UTF-8")

        student_list: list[Student] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            student = Student(data_dict["id"], data_dict["name"], int(data_dict["class_"]), float(data_dict["chinese"]), float(data_dict["math"]), float(data_dict["english"]), float(data_dict["physics"]), float(data_dict["chemistry"]), float(data_dict["biology"]), float(data_dict["lizong"]), float(data_dict["total"]))
            student_list.append(student)

        f.close()
        return student_list

if __name__ == "__main__":
    text_file_reader = TextFileReader("students.csv")
    json_file_reader = JsonFileReader("students.jsonl")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()
    for l in list1:
        print(l)
    for l in list2:
        print(l)







