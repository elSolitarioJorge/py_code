# Python的多线程编程可以通过threading模块实现

# import time
# import threading
#
# def sing(msg):
#     while True:
#         print(msg)
#         time.sleep(1)
#
# def dance(msg):
#     while True:
#         print(msg)
#         time.sleep(1)
#
# if __name__ == '__main__':
#     # 唱歌线程
#     sing_thread = threading.Thread(target = sing, args = ("奶龙在唱歌：今夜星光闪闪",))
#     # 跳舞线程
#     dance_thread = threading.Thread(target = dance, kwargs = {"msg": "贝利亚在看奥特之母跳舞"})
#     # 启动线程
#     sing_thread.start()
#     dance_thread.start()

