# socket(简称：套接字)是进程之间通信一个工具，进程之间想要进行网络通信需要socket
# socket负责进程之间的网络数据传输，好比数据的搬运工
# 两个进程之间通过Socket进行通信，必须有服务端和客户端
# Socket服务端：等待其他进程的连接、可接收发来的消息、可回复消息
# Socket客户端：主动连接服务端、可以发送消息、可以接收回复

# Socket服务端编程
import socket
# 创建Socket对象
socket_server = socket.socket()
# 绑定socket_server到指定IP和地址
socket_server.bind(("localhost", 8888))

# 服务端开始监听端口
socket_server.listen(1)
# listen方法内接收一个整数参数，表示接收的连接数量
# 接收客户端连接，获得连接对象
# result: tuple = socket_server.accept()
# conn = result[0]           # 客户端和服务端的连接对象
# address = result[1]        # 客户端的地址信息
conn, address = socket_server.accept()
# accept方法返回的是二元元组(连接对象, 客户端地址信息)
# 可以通过变量1,变量2 = socket_server.accept()的形式，直接接收二元元组内的两个元素
# accept()方法是阻塞的方法，等待客户端的链接，如果没有链接，就卡在这一行不再向下执行了
print(f"客户端{address}已连接")

while True:
    # 客户端连接后，通过recv方法，接收客户端发送的消息
    data: str = conn.recv(1024).decode('UTF-8')
    # recv方法接收的参数是缓冲区大小，一般给1024即可
    # recv方法返回的是一个字节数组，也就是bytes对象，不是字符串，可以通过decode方法通过UTF-8编码，将字节数组转换为字符串对象
    print(f"客户端{address}发送的消息是：{data}")
    # 通过conn(客户端当次连接对象)，调用send方法可以回复消息
    msg = input("请输入回复内容：")
    if msg == "exit":
        break
    conn.send(msg.encode('UTF-8')) # encode可以将字符串编码转换为字节数组对象

# conn(客户端当次连接对象)和socket_server对象调用close方法，断开连接
conn.close()
socket_server.close()