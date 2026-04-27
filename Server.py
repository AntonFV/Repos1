import socket
import threading
clients =[]
clients_lock = threading.Lock()

def start():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 5001))
    server_socket.listen()
    print('Сервер запущен и ждёт клиента')
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        with clients_lock:
            clients.append(client_socket)
        client_thread.start()
        print('Подключился клиент:', client_address)
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f'Получено сообщение от {client_address}:', data.decode('utf-8'))




def handle_client(client_socket, client_address):
    connected = True
    print(f'Клиент,{client_address} подключен')
    while connected==True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode('utf-8')
        print(f'От {client_address} пришло:', message)
        client_socket.send(message.encode('utf-8'))
        with clients_lock:
            if client_socket in clients:
                clients.remove(client_socket)
                connected=False
                client_socket.close()
                print(f'Клиент {client_address} отключился')
                

    
start()
