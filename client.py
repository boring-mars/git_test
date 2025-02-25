import socket

client = socket.socket()
client.connect(("localhost", 7077))

while True:
    msg = input("Press any key to send data to server")
    client.send(msg.encode("UTF-8"))
    resp = client.recv(1024).decode("UTF-8")
    print(f"Response from server: {resp}")
    if msg == "exit":
        break

client.close()
