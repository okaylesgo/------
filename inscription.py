import socket
import asyncio
import json
port=int(1234)
Addressplayer = ('0.0.0.0', port)
serveraddress=('localhost',3000)
def inscription():
        print('test')
        with socket.socket() as s:
            s.connect(serveraddress)
            inscription={"request": "subscribe","port": port,"name":'akachar Ali',"matricules":["20004",'20009']}
            message=json.dumps(inscription)
            s.send(message.encode())
            message=s.recv(2048).decode()
            print(message)
            if message=='{"response": "ok"}':
                print('OK ON COMMENCE')
            else:
                raise ValueError("Inscription Error: " + message)
