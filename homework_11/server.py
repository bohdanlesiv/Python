import socket
import os
import threading

file_name = 'data.txt'
current_path = os.getcwd()

def wrtie_client_msg(msg,addr):
    with open(os.path.join(current_path,file_name),'a+') as f:
        prepared_data = str(addr)+' '+str(msg)+'\n'
        f.write(prepared_data)


sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(7)

def listen_client(con,addr):
    data = con.recv(1024)
    wrtie_client_msg(data,addr)

while True:
    conn, addr = sock.accept()
    #data = conn.recv(1024)
    #wrtie_client_msg(data,addr)
    threading.Thread(target=listen_client, args=(conn,addr)).start()