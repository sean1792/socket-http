import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
adr = socket.gethostbyname(socket.gethostname())
#print('port:',end='')
#port=int(input())
port=8000

file = open('index.html', 'r')
content = file.read()
file.close()
#print(content)
try:
	file=open('index2.html', 'r')
	print(file.read())
	file.close()
except :
	print('Error')




s.bind((adr, port))
while True:
	s.listen()
	print("Start listening")
	


	print("Server start at :",s.getsockname())
	#if(input()=='quit'):
		#break
	conn, adr = s.accept()

	index404 = 'HTTP/1.1 404 Not Found\r\nConnection: close\r\n\r\n'
	index_content = 'HTTP/1.1 200 ok\r\nConnection: close\r\n\r\n'

	print ('Connect by',conn.getsockname())
#conn.send("Hello, say something".encode())
	#file = open('index.html', 'r')
	#index_content += file.read()
	#file.close()

	while True:
		data = conn.recv(1024)
		print(data.decode())
		#m = data.split()[0]
		s = data.decode().split()[1]
		print(s)
		if s=='/':
			#print('s=/')
			try:
				file=open('index.html', 'r')
				d=file.read()
				file.close()
				print('readf')
				receive = index_content+d
			except :
				print('Error')
				receive = index404
		else:
			try:
				file=open(s, 'r')
				d=file.read()
				file.close()
				print('readf')
				receive = index_content+d
			except :
				receive = index404
				print('Error')
		#print(m,s)
		#print('test')
		#print(data)
		while data.endswith=='\r\n\r\n':
			print('True')
			break
	#conn.send("Server received your message".encode()) 
		conn.send(receive.encode())
		print('send!')
		print(receive)
	conn.close()
	print('connection closed')
		#if data == 'exit':
			#conn.close()
			#print("Client aborted the connection")

