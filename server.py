import socket
#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#adr = socket.gethostbyname(socket.gethostname())
port=8000
receive = ''
fp = open('index.html', 'r')
	#index_content += file.read()
print(fp.read())
fp.close()
#s.bind((adr, port))
while True:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	adr = socket.gethostbyname(socket.gethostname())
	s.bind((adr, port))
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
	file = open('index.html', 'r')
	#index_content += file.read()
	print(file.read())
	file.close()

	#while True:
	data = conn.recv(1024)
	print(data.decode())
		#m = data.split()[0]
	s = data.decode().split()[1]
		#print(s.strip('/'))
	if s=='/':
		print('s=/')
		try:
			file=open('index.html', 'r')
			d=file.read()
			file.close()
			print('readf')
			receive = index_content+d
			print(receive)
		except :
			print('Error')
			receive = index404
	else:
		print(s.strip('/'))
		try:
			file=open(s.strip('/'), 'r')
			print("?")
			d=file.read()
			file.close()
			print('readf')
			receive = index_content+d
			print(receive)
		except :
			receive = index404
			print('Error')
	conn.send(receive.encode())
	print('send!')
	print(receive)
	conn.close()
	print('connection closed')

