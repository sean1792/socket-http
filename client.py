import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = input("Please enter the Server IP:")
h=socket.gethostbyname(addr)
print(h)
port = 8000
f = input("enter file name:")
header = 'GET /'
header += f
header+=' HTTP/1.1\r\nHost: addr\r\nConnection: keep-alive\r\n\r\n'
print(header)
s.connect((addr,port))
#print(s.recv(1024).decode())

while True:
    



    s.send(header.ecnode())





    data = s.recv(1024)
    print (data.decode())
    
    if cmd == 'exit':
        print ("Close socket")
        s.close()
        break