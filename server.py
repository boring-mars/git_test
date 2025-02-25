import socket

server = socket.socket()
server.bind(("localhost", 7077))
server.listen(1)

conn, addr = server.accept()
print(f"The client info: {addr}")

while True:
    data = conn.recv(1024).decode("UTF-8")
    print(f"The data from client: {data}")
    conn.send("Received by server".encode("UTF-8"))
    if data == "exit":
        break

conn.close()
server.close()
