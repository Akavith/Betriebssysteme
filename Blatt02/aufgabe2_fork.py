import os

def child():
    for i in range(0,200):
        print("Kind mit PID=" + str(os.getpid()))

def parent():
    for i in range(0,200):
        print(pids)

pids = ""
for i in range(0,3):
    newpid = os.fork()
    if(newpid == 0):
        child()
        break
    pids += str(newpid) + ", "
pids = pids[0:-2]
if(newpid != 0):
    parent()



