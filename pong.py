import socket
port=int(1234)
Addressplayer = ('0.0.0.0', port)
serveraddress=('localhost',3000)
def pong():
    try:
        with socket.socket() as s:
                s.connect(serveraddress)
                message='{"response": "pong"}'
                s.send(message.encode())
    except:
        print('ping sans pong :(')