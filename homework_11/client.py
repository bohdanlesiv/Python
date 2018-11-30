import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

text ='Hi i am here2'
sock.send(text.encode())


