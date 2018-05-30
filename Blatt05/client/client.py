import socket
import time

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))

while 1:

    # command menu for user
    print('Please specify what calculation you want to do:')
    print('\t1)\t\tadd two numbers')
    print('\t2)\t\tmultiply two numbers')
    print('\t3)\t\tappend two strings')
    print('\texit)\tclose the program')

    cmd = input()

    if cmd == 'exit':
        break

    print('Please enter value 1:')
    val1 = input()
    print('Please enter value 2:')
    val2 = input()

    cmd_send = bytes([0])
    if cmd == 2:
        cmd_send = bytes([1])
    elif cmd == 3:
        cmd_send = bytes([2])
    # sending information to client

    clientsocket.send(cmd_send)
    clientsocket.send(bytes(val1, encoding="utf-8"))
    clientsocket.send(bytes([0]))
    clientsocket.send(bytes(val2, encoding="utf-8"))
    clientsocket.send(bytes([0]))
    # receive message

    data = clientsocket.recv(128)
    print("Result: " + data.decode("utf-8") + '\n')


#close program
clientsocket.send(bytes([3]))
clientsocket.close()