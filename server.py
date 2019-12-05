import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
adr = socket.gethostbyname(socket.gethostname())
#print('port:',end='')
#port=int(input())
port=8000

file = open('index.html', 'r')
content = file.read()
file.close()
print(content)











s.bind((adr, port))
s.listen()
print("Start listening")


print("Server start at :",s.getsockname())
conn, adr = s.accept()

#index_content = 
index_content = 'HTTP/1.x 200 ok\r\nContent-Type: text/html\r\n\r\n'

print ('Connect by',conn.getsockname())
#conn.send("Hello, say something".encode())
file = open('index.html', 'r')
index_content += file.read()
file.close()

while True:
	data = conn.recv(1024)
	print(data.decode())
	#conn.send("Server received your message".encode()) 
	conn.send(index_content.encode())
	if data == 'exit':
		conn.close()
		print("Client aborted the connection")