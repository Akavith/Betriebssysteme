f = open("/etc/passwd",'r')

text = f.readline()

while text:
    array = text.split(":")
    print (array[0] + ", " + array[2])
    text = f.readline()
f.close()