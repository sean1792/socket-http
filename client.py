import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#addr = input("Please enter the Server IP:")
addr ='192.168.1.9'
h=socket.gethostbyname(addr)
print(h)
port = 8000
#f = input("enter file name:")
f='index.html'
header = 'GET /'
header += f
header+=' HTTP/1.1\r\nHost: '+addr+'\r\nConnection: close\r\n\r\n'
print(header)
s.connect((addr,port))
#print(s.recv(1024).decode())

while True:
    



    s.send(header.encode())




    data = s.recv(1024)
    file=open('example.html','w')
    print (data.decode())
    print(data)
    g= data.decode().split('\r\n\r\n')[1]
    file.write(g)
    print('\n\n\n\n\n\n')
    print(g)
    #print (data.decode().split()[5])
    #a=input('stop(y/n)?')
    a='y'
    if a=='y':
        break
s.close()