import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
adr = socket.gethostbyname(socket.gethostname())
#print('port:',end='')
#port=int(input())
port=80

#port = 5566

s.bind((adr, port))
s.listen()
print("Start listening")


print("Server start at :",s.getsockname())
conn, adr = s.accept()

print ('Connect by',conn.getsockname())
conn.send("Hello, say something".encode())

while True:
	data = conn.recv(5)
	print(data.decode())
	conn.send("Server received your message".encode()) 

	if data == 'exit':
		conn.close()
		print("Client aborted the connection")