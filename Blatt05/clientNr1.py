# Echo client program
import socket
import struct

def changeToBinary(string):
    return struct.pack('<i',string)


HOST = 'localhost'    # The remote host
PORT = 33002              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(changeToBinary(input()))
data = s.recv(1024)
s.close()
print 'Received', repr(data)
data = struct.unpack('<i',data)[0]
if(isinstance(data,int)):
    print data,'is an int btw.'
#print 'Unpacking it to int', struct.unpack('<i',data)[0]