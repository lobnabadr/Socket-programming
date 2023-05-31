import socket
import random

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host='127.0.0.1'
    port=7002
    s.bind((host,port))
    s.listen(5)
    c,add=s.accept()
    print('connection established with: '+add[0])
    colors=['brown','orange','red','purple','blue','pink','black','green','gray','yellow']
    
    while True:
        textcolor=colors[random.randint(0, len(colors)-1)]
        textword=colors[random.randint(0, len(colors)-1)]
        while( textcolor==textword):
             textword=colors[random.randint(0, len(colors)-1)]
        sentmessage=  textcolor[0]+textword[0]
        c.send(sentmessage.encode('ascii'))
        recievemessage=c.recv(2048).decode('ascii')
    s.close()
except socket.error as e:
    print(e)
except KeyboardInterrupt:
    print('end chat')