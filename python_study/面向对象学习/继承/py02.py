# 单继承
# class 类名(父类名):
#
# class Phone:
#     IMEI = None
#     producer = "苹果"
#
#     def call_by_4g(self):
#         print("4g通话")
#
# class Phone2025(Phone):
#     face_id = "1001"
#
#     def call_by_5g(self):
#         print("5g通话")
#
# phone = Phone2025()
# print(phone.producer)
# phone.call_by_4g()
# phone.call_by_5g()
# # 多继承
# # class 类名(父类1, 父类2, ...):
# class NFCReader:
#     nfc_type = "第五代"
#     producer = "小米"
#
#     def read_card(self):
#         print("NFC读卡")
#
#     def write_card(self):
#         print("NFC写卡")
#
# class RemoteControl:
#     rc_type = "红外遥控"
#
#     def control(self):
#         print("红外遥控开启")
#
# class MyPhone(Phone, NFCReader, RemoteControl):
#     pass
#
# phone = MyPhone()
# print(phone.producer)
# phone.call_by_4g()
# phone.read_card()
# phone.control()

# 复写
# 子类继承父类的成员属性和成员方法后，如果对其“不满意”，那么可以进行复写
# 即在子类中重新定义同名的属性和方法
# 调用父类同名成员
# 一旦复写父类成员，那么类对象调用成员的时候，就会调用复写后的新成员
# 如果需要使用被复写的父类成员，有特殊的调用方式：
# 父类名.成员变量
# 父类名.成员方法(self)
# 使用super()函数调用父类成员
# super()函数会自动找到当前类的直接父类
# super()函数返回一个父类对象，通过这个父类对象可以调用父类成员
# super().成员变量
# super().成员方法()

