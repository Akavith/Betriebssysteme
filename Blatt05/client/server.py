import socket, os


ADD = bytes(1);
MUL = bytes(2);
STRADD = bytes(3);

CLOSE = bytes(4);


def add(a, b):
    return bytes(str(int(a) + int(b)), encoding="utf-8")


def mul( a, b):
    return bytes(str(int(a) * int(b)), encoding="utf-8")


def stradd(a, b):
    return a + b


funcArray = [add, mul, stradd]


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8089
serversocket.bind((host, port))

serversocket.listen(2)

buf = b''

words = []


def getNextWord():
    global buf
    global words
    while True:
        if len(words) > 0:
            return words.pop(0)

        data = client.recv(8192)

        buf = buf + data

        print(buf)

        words = buf.split(b'\x00')
        buf = words.pop()





def handleClient(client):
    serversocket.close()
    while True:
        func = getNextWord()
        print(func)

        result = funcArray[func[0] - 1](getNextWord(), getNextWord())
        client.send(result)

    client.close()


while True:
    client, addr = serversocket.accept()
    pid = os.fork()
    if pid == 0:
        handleClient(client)
        break
    else:
        client.close()
