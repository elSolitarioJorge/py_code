# Socket客户端编程

# 创建socket对象
import socket
socket_client = socket.socket()
# 连接服务端
socket_client.connect(("localhost", 8888))

while True:
    # 发送消息
    send_msg = input("请输入要发送的消息：")
    if send_msg == 'exit':
        break
    socket_client.send(send_msg.encode("UTF-8"))
    # 接收消息
    recv_data = socket_client.recv(1024)
    # recv方法是阻塞的，即不接收返回，就卡在这里等待
    print(f"收到服务端消息：{recv_data.decode('UTF-8')}")

socket_client.close()