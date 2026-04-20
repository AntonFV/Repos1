import socket 
import time
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5001))

while(exit!=1):
    print("Введите сообщение:")
    message=str(input())
    client_socket.send(f'{message}'.encode('utf-8'))
    print("Выйти с сервера(Да/Нет)?")
    answer=str(input())
    if(answer=="Да"):
        exit=1
    time.sleep(1)
client_socket.close()