from socket import socket
import os
server = socket()
server.bind(("localhost",9999))
server.listen()
while True:
    conn,addr = server.accept()
    while True:
        print("new conn:",addr)
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        print("执行命令:",data.decode())
        cmd_res = os.popen(data.decode()).read()
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output..."
        conn.send(cmd_res.encode())
        
server.close()

